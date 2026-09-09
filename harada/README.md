# Método Harada — plan personal

> ⚠️ **PRIVACIDAD — LEE ESTO PRIMERO**
>
> Este repositorio se publica como sitio estático en **GitHub Pages** (`CNAME` → `aisagalab.com`,
> `robots.txt` permite indexar todo). **Si esta carpeta llega a `main`, su contenido queda
> accesible públicamente** en `https://aisagalab.com/harada/…` y es indexable.
>
> Esta carpeta contiene análisis personal de tu pasado, tus objetivos y tu diario.
> Recomendación: **no fusionar a `main`**. Mantenla en la rama `claude/harada-method-9h9taj`,
> o muévela a un repositorio privado. Ver [Cómo mantener esto privado](#cómo-mantener-esto-privado).

---

## Qué es el Método Harada

Lo desarrolló **Takashi Harada**, profesor de secundaria en un instituto público de la zona
más deprimida de Osaka. En siete años convirtió a un equipo de atletismo sin recursos en
campeón nacional trece veces. Su tesis: el rendimiento excepcional no viene del talento,
sino de un **sistema de autogestión** que se puede enseñar.

El objetivo final del método no es cumplir una meta. Es fabricar una **persona autosuficiente**
(自立型人間, _jiritsu-gata ningen_): alguien capaz de fijarse objetivos, desglosarlos, ejecutar
a diario y corregirse sin que nadie le empuje. La meta concreta es el vehículo, no el destino.

Tres ideas que lo diferencian de casi cualquier otro sistema de productividad:

1. **El objetivo tiene cuatro caras, no una.** Si tu meta solo te beneficia a ti, el método
   dice que no aguantarás el esfuerzo. Debe servir también a otros.
2. **El desglose es exhaustivo, no priorizado.** 64 acciones concretas. No eliges "las 3 más
   importantes" — mapeas todo el territorio primero.
3. **Lo que se mide es la rutina, no el resultado.** El resultado no está bajo tu control
   directo. El porcentaje de cumplimiento de tus rutinas diarias, sí.

---

## Las seis piezas

| # | Pieza | Archivo | Cuándo se toca |
|---|-------|---------|----------------|
| 1 | Propósito y objetivo cuatripartito | [`01-proposito-y-objetivo.md`](01-proposito-y-objetivo.md) | Una vez. Revisión trimestral. |
| 2 | Análisis del pasado y activos | [`02-analisis-del-pasado.md`](02-analisis-del-pasado.md) | Una vez, antes de fijar el objetivo. |
| 3 | Open Window 64 (carta de 64 casillas) | [`03-open-window-64.md`](03-open-window-64.md) | Una vez. Revisión mensual. |
| 4 | Hoja de rutinas diarias | [`04-rutinas-diarias.md`](04-rutinas-diarias.md) | **Todos los días.** |
| 5 | Diario (日誌 _nisshi_) | [`05-diario.md`](05-diario.md) | **Todos los días, 5 min.** |
| 6 | Revisiones semanal / mensual / trimestral | [`06-revisiones.md`](06-revisiones.md) | Domingo, fin de mes, fin de trimestre. |

Además, dos anexos que **no son piezas del método**:

- [`07-principios.md`](07-principios.md) — los trece principios de Sam Altman
  (*How to Be Successful*, 2019) traducidos a candidatos de pilar y de casilla del 64.
  Materia prima para las piezas 01 y 03, no un paso más. Incluye las tres tensiones reales
  con Harada, sin disimularlas.
- [`tracker.html`](tracker.html) — herramienta local autocontenida (abre el archivo en el
  navegador) con la carta de 64 editable, el marcador de rutinas con racha, el diario y
  export/import en JSON. Guarda en `localStorage`, no envía nada a ningún servidor.

---

## El orden importa

No empieces por la carta de 64. Es el error más común y produce 64 acciones bonitas al
servicio de un objetivo que no aguanta seis meses.

```
02 Análisis del pasado   →  qué sé de mí, qué me ha funcionado, con qué cuento
        ↓
01 Propósito y objetivo  →  para qué, y qué número con qué fecha
        ↓
03 Open Window 64        →  8 pilares × 8 acciones          ←  07 Principios
        ↓                                                       (banco de ideas)
04 Rutinas               →  las 8-10 acciones del 64 que se hacen a diario
        ↓
05 Diario  +  06 Revisiones   →  el bucle que lo sostiene
```

**Tiempo de preparación realista:** 3–4 horas, mejor repartidas en dos sesiones con una
noche de por medio. Sesión 1: piezas 02 y 01. Duermes. Sesión 2: piezas 03 y 04.

**Tiempo de ejecución diario:** 5–10 minutos (marcar rutinas + diario). Ni uno más.
Si tu sistema de seguimiento cuesta más de 10 minutos al día, lo abandonarás en tres semanas.

---

## El bucle, una vez montado

- **Cada día (5–10 min, noche).** Marcas rutinas: `○` hecha, `△` a medias, `×` no.
  Escribes tres líneas en el diario. Se acabó.
- **Cada domingo (15 min).** Calculas el % de cumplimiento de la semana. Miras qué rutina
  falló y **por qué** — casi siempre es diseño, no voluntad: la rutina es demasiado grande,
  está mal colocada en el día, o depende de otra persona.
- **Fin de mes (45 min).** % del mes. Mides la métrica principal. Revisas los 64: tachas lo
  hecho, rotas 1–2 rutinas si alguna ya es automática o ya no sirve.
- **Fin de trimestre (90 min).** La pregunta incómoda: ¿sigue siendo este el objetivo correcto?
  Cambiar de objetivo con datos en la mano es disciplina. Cambiarlo en un mal martes es fuga.

---

## Los números que importan

Harada trabajaba con estos umbrales. Son los que usa el `tracker.html`:

- **≥ 80 % de cumplimiento mensual** de rutinas → el sistema funciona, no toques nada.
- **60–79 %** → las rutinas son demasiado ambiciosas. Reduce el tamaño, no la frecuencia.
- **< 60 %** → problema de diseño, no de disciplina. Vuelve a la pieza 03: probablemente
  los pilares no se corresponden con tu vida real.

Y el que más duele: **una rutina fallada tres días seguidos no es una rutina fallada, es una
rutina mal elegida.** Cámbiala en la revisión semanal en lugar de arrastrarla con culpa.

---

## Cómo mantener esto privado

Tres opciones, de más a menos segura:

1. **Repositorio privado aparte** (recomendada si vas en serio con el diario).
   ```bash
   mkdir ~/harada-personal && cp -r harada/* ~/harada-personal/
   cd ~/harada-personal && git init && git add . && git commit -m "harada: plan personal"
   # y lo subes a un repo privado
   ```
2. **No fusionar nunca a `main`.** Vive solo en la rama `claude/harada-method-9h9taj`.
   El contenido de una rama no publicada no lo sirve GitHub Pages, pero **sí es visible en
   GitHub** para quien tenga acceso al repo.
3. **Si acaba en `main` de todas formas:** ya se ha añadido `Disallow: /harada/` al
   `robots.txt` raíz y `noindex` al `tracker.html`. Eso evita el indexado en buscadores,
   **no** el acceso directo por URL. Es una tirita, no una cerradura.

---

## Fuentes

- Takashi Harada, *The Harada Method: The Spirit of Self-Reliance* (Ed. inglesa, PHP Institute).
- Norman Bodek & Takashi Harada, *How to Do the Harada Method*.
- El Open Window 64 es una aplicación del **Mandal-Art** de Matsumura Yasuo (1979).
  Es la misma rejilla que Shohei Ohtani rellenó a los 16 años en el instituto Hanamaki
  Higashi con el objetivo central "ser elegido nº 1 por 8 equipos en el draft".
