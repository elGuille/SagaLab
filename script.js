document.addEventListener('DOMContentLoaded', function () {
    // Navigation toggle functionality
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // Smooth scrolling for anchor links with offset
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.getBoundingClientRect().top + window.pageYOffset - 80;
                window.scrollTo({ top: offsetTop, behavior: 'smooth' });
            }
        });
    });

    // Logo click to scroll to top
    const homeLogo = document.getElementById('home-logo');
    if (homeLogo) {
        homeLogo.addEventListener('click', function (e) {
            e.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Mobile Apps Data
    const mobileApps = [
        {
            name: 'Dora AI Video Generator',
            category: 'Video Creation',
            // App Store frame, chosen 6 Sep 2026 (decision D4). The old
            // composite showed a gorilla and a skateboarding dog: two outputs
            // and no hint of what a person does to get them. This one shows
            // the typed prompt and the video it produced, which is the whole
            // product in one picture. Marta rejected the animals and the
            // before/after frames explicitly.
            image: 'images/dora/02.webp',
            description: 'Upload a photo, describe the shot, get a finished video back in a couple of minutes. On the web, on iPhone, and soon on Android — and from inside the AI assistant you already use.',
            link: 'https://doravideo.com/?utm_source=sagalab&utm_medium=homepage&utm_campaign=dora',
            cta: 'Open Dora',
            appStoreFeatured: false,
            // Dora ships on three surfaces. The card used to send everyone to
            // the MCP page, which reads as a developer product and lost the
            // App Store link entirely. Android goes in when Play approves it.
            secondaryLinks: [
                { label: 'iPhone app', href: 'https://apps.apple.com/app/id6754180384' },
                { label: 'Use it in ChatGPT, Claude or Cursor', href: 'ai-video-generator.html?utm_source=sagalab&utm_medium=homepage&utm_campaign=dora_agents' }
            ]
        },
        {
            name: 'Pinku Private AI',
            category: 'Productivity',
            image: 'images/pinku.webp',
            description: 'On-device AI assistant running Llama, Qwen, and DeepSeek locally. Zero data collection, works offline.',
            link: 'https://apps.apple.com/us/app/pinku-private-ai/id6754878073',
            cta: 'Get Pinku',
            appStoreFeatured: true
        },
        {
            name: 'Keeper: Private Folder',
            category: 'Security',
            image: 'images/photolock.webp',
            description: 'Encrypted photo and document vault with biometric authentication.',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722',
            cta: 'Secure Files',
            appStoreFeatured: false
        },
        {
            name: '3 Tasks: Daily Productivity',
            category: 'Productivity',
            image: 'images/3tasks.webp',
            description: 'A simple three-task daily system. Do less, focus on what matters.',
            link: 'https://apps.apple.com/au/app/3-tasks-daily-productivity/id1553693943',
            cta: 'Download App',
            appStoreFeatured: true
        },
        {
            name: 'Brainy: AI Helper',
            category: 'Productivity',
            image: 'images/brainyapp.webp',
            description: 'AI assistant for writing, brainstorming, and creative tasks.',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372',
            cta: 'Get Help',
            appStoreFeatured: true,
            customClass: 'brainy-app'
        },
        {
            name: 'Crypton: Crypto Tracker',
            category: 'Finance',
            image: 'images/crypton.webp',
            description: 'Real-time crypto tracking with price alerts and portfolio insights.',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286',
            cta: 'Track Portfolio',
            appStoreFeatured: false
        },
        {
            name: 'Focus Meditation',
            category: 'Health & Wellness',
            image: 'images/drop.webp',
            description: 'Guided meditations and sleep sounds. Reduce stress, sleep better.',
            link: 'https://apps.apple.com/au/app/drop-relax-focus-sleep-well/id1462269642',
            cta: 'Start Meditating',
            appStoreFeatured: true
        }
    ];

    // Render Apps
    //
    // Dora is the business; the other six are shipped work. Rendering all
    // seven as identical full-height rows gave a paused meditation app the
    // same weight as the product that pays, and left the page mostly
    // whitespace. Dora keeps the big row, the rest go in a compact grid.
    const APPLE_ICON = `
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                                <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
                            </svg>`;

    const externalAttrs = (href) =>
        href.startsWith('http') ? ' target="_blank" rel="noopener noreferrer"' : '';

    const combinedGrid = document.querySelector('.combined-apps-grid');
    if (combinedGrid) {
        const [lead, ...rest] = mobileApps;

        const leadHtml = `
            <div class="app-showcase-row">
                <div class="app-showcase-content">
                    <span class="app-showcase-category">${lead.category}</span>
                    <h3 class="app-showcase-title">${lead.name}</h3>
                    <p class="app-showcase-desc">${lead.description}</p>
                    <div class="app-showcase-actions">
                        <a href="${lead.link}"${externalAttrs(lead.link)} class="app-showcase-btn">
                            ${lead.cta}
                        </a>${(lead.secondaryLinks || []).map((l) => `
                        <a href="${l.href}"${externalAttrs(l.href)} class="app-showcase-link">${l.label}</a>`).join('')}
                    </div>
                </div>
                <div class="app-showcase-visual">
                    <img src="${lead.image}" alt="${lead.name} interface" class="app-showcase-img">
                </div>
            </div>`;

        const restHtml = `
            <section class="also-shipped">
                <h2 class="also-shipped__title">Also shipped</h2>
                <p class="also-shipped__lead">Six more apps on the App Store. Each one started as a way to try something we wanted to understand.</p>
                <div class="also-shipped__grid">
                    ${rest.map((app) => `
                    <a class="also-shipped__card" href="${app.link}"${externalAttrs(app.link)}>
                        <img src="${app.image}" alt="${app.name}" loading="lazy" class="also-shipped__img">
                        <span class="also-shipped__cat">${app.category}</span>
                        <h3 class="also-shipped__name">${app.name}</h3>
                        <p class="also-shipped__desc">${app.description}</p>
                        <span class="also-shipped__cta">${app.link.includes('apps.apple.com') ? APPLE_ICON : ''}${app.cta}</span>
                    </a>`).join('')}
                </div>
            </section>`;

        combinedGrid.innerHTML = leadHtml + restHtml;
    }

    // Scroll animations with IntersectionObserver
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe app rows after render
    setTimeout(() => {
        const rows = document.querySelectorAll('.app-showcase-row');
        if (rows.length > 0) {
            // Animate first row immediately
            rows[0].classList.add('animate');
        }
        rows.forEach((row, index) => {
            if (index > 0) {
                row.style.transitionDelay = `${index * 0.03}s`;
                observer.observe(row);
            }
        });
    }, 50);

    // Dark Mode Toggle
    window.toggleTheme = function () {
        const isDark = document.body.classList.toggle('dark-mode');
        const icon = document.getElementById('nav-theme-icon');
        const iconPath = icon.querySelector('path');

        if (isDark) {
            // Sun icon for dark mode
            iconPath.setAttribute('d', 'M12 17.5c3.038 0 5.5-2.462 5.5-5.5S15.038 6.5 12 6.5 6.5 8.962 6.5 12s2.462 5.5 5.5 5.5zm0-13V3m0 18v-1.5m6.364-13.864L17.657 6.343M6.343 17.657l-.707.707m12.728 0l.707.707M6.343 6.343l-.707-.707M21 12h1.5M3 12H1.5');
            localStorage.setItem('theme', 'dark');
        } else {
            // Moon icon for light mode
            iconPath.setAttribute('d', 'M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z');
            localStorage.setItem('theme', 'light');
        }
    };

    // Initialize theme from saved preference or system preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches && !savedTheme)) {
        document.body.classList.add('dark-mode');
        const icon = document.getElementById('nav-theme-icon');
        if (icon) {
            const iconPath = icon.querySelector('path');
            if (iconPath) {
                iconPath.setAttribute('d', 'M12 17.5c3.038 0 5.5-2.462 5.5-5.5S15.038 6.5 12 6.5 6.5 8.962 6.5 12s2.462 5.5 5.5 5.5zm0-13V3m0 18v-1.5m6.364-13.864L17.657 6.343M6.343 17.657l-.707.707m12.728 0l.707.707M6.343 6.343l-.707-.707M21 12h1.5M3 12H1.5');
            }
        }
    }

    // REMOVED: Neural Network Canvas implementation for simplification
});
