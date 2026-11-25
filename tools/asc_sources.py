"""Weekly App Store traffic sources per app -> data/search-terms/appstore-sources.csv.

Reads ASC_KEY_ID, ASC_ISSUER_ID and ASC_PRIVATE_KEY_B64 from the environment.
Apple does not expose search terms; this records where users come from
(App Store search, browse, web referrer, app referrer) and in which countries.
"""
import base64, csv, gzip, io, json, os, time, urllib.request, urllib.error
from collections import defaultdict
import jwt

B = "https://api.appstoreconnect.apple.com"
KEY = base64.b64decode(os.environ["ASC_PRIVATE_KEY_B64"]).decode()
TOK = jwt.encode({"iss": os.environ["ASC_ISSUER_ID"], "iat": int(time.time()), "exp": int(time.time()) + 1100,
                  "aud": "appstoreconnect-v1"}, KEY, algorithm="ES256", headers={"kid": os.environ["ASC_KEY_ID"]})
REPORT = "App Store Discovery and Engagement Standard"
WEEKS = 4


def get(path):
    req = urllib.request.Request(path if path.startswith("http") else B + path, headers={"Authorization": "Bearer " + TOK})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError:
        return {"data": []}


def rows_for(app_id):
    reqs = [r for r in get(f"/v1/apps/{app_id}/analyticsReportRequests")["data"] if r["attributes"]["accessType"] == "ONGOING"]
    for rq in reqs:
        reps = get(f"/v1/analyticsReportRequests/{rq['id']}/reports?filter[name]=" + urllib.parse.quote(REPORT))["data"]
        for rp in reps:
            insts = get(f"/v1/analyticsReports/{rp['id']}/instances?filter[granularity]=WEEKLY&limit=50")["data"]
            insts.sort(key=lambda i: i["attributes"]["processingDate"], reverse=True)
            for inst in insts[:WEEKS]:
                for seg in get(f"/v1/analyticsReportInstances/{inst['id']}/segments")["data"]:
                    raw = gzip.decompress(urllib.request.urlopen(seg["attributes"]["url"]).read()).decode()
                    yield from csv.DictReader(io.StringIO(raw), delimiter="\t")
        return


import urllib.parse
apps = get("/v1/apps?fields[apps]=name&limit=200")["data"]
agg = defaultdict(lambda: [0, 0])  # (app, week, source, event) -> counts
terr = defaultdict(int)
for a in apps:
    for r in rows_for(a["id"]):
        k = (a["attributes"]["name"], r["Date"][:10], r["Source Type"], r["Event"])
        agg[k][0] += int(r["Counts"] or 0); agg[k][1] += int(r["Unique Counts"] or 0)
        if r["Source Type"] == "App Store search" and r["Event"] == "Impression":
            terr[(a["attributes"]["name"], r["Territory"])] += int(r["Counts"] or 0)

os.makedirs("data/search-terms", exist_ok=True)
with open("data/search-terms/appstore-sources.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["app", "date", "source_type", "event", "counts", "unique_counts"])
    for k in sorted(agg): w.writerow([*k, *agg[k]])
with open("data/search-terms/appstore-search-territories.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["app", "territory", "search_impressions_last_weeks"])
    for (app, t), n in sorted(terr.items(), key=lambda x: (x[0][0], -x[1])): w.writerow([app, t, n])
print(f"{len(agg)} source rows, {len(terr)} territory rows")
