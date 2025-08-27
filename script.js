document.addEventListener('DOMContentLoaded', function() {
    // Theme handling
    const THEME_KEY = 'theme';
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');

    const getStoredTheme = () => {
        const t = localStorage.getItem(THEME_KEY);
        return t === 'dark' || t === 'light' ? t : null;
    };

    const getPreferredTheme = () => {
        const stored = getStoredTheme();
        if (stored) return stored;
        return prefersDark && prefersDark.matches ? 'dark' : 'light';
    };

    const applyTheme = (theme) => {
        const isDark = theme === 'dark';
        document.body.classList.toggle('dark', isDark);
        const btn = document.querySelector('.theme-toggle');
        if (btn) {
            btn.setAttribute('aria-pressed', String(isDark));
            btn.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';
        }
    };

    // Initialize theme
    let currentTheme = getPreferredTheme();
    applyTheme(currentTheme);

    // Listen for system changes only if user hasn't chosen explicitly
    if (!getStoredTheme() && prefersDark) {
        prefersDark.addEventListener('change', (e) => {
            currentTheme = e.matches ? 'dark' : 'light';
            applyTheme(currentTheme);
        });
    }

    // Toggle button handler
    const toggleBtn = document.querySelector('.theme-toggle');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            currentTheme = document.body.classList.contains('dark') ? 'light' : 'dark';
            localStorage.setItem(THEME_KEY, currentTheme);
            applyTheme(currentTheme);
        });
    }
    const apps = [
        {
            name: 'Foro: AI Forum',
            category: 'AI Research',
            image: 'images/foro.png',
            description: 'Watch two AI agents discuss any topic with four unique modes: **Dialog**, **Debate**, **Brainstorm**, and **Prediction**. Supports 100+ models including local ones for complete privacy.',
            link: 'https://github.com/Saga-Labs/foro',
            isGitHub: true
        },
        {
            name: 'AI Trading Bot',
            category: 'AI Research',
            image: 'images/bot-running-screenshot.png',
            gallery: ['images/telegram-notifications.png', 'images/bot-running-screenshot.png'],
            description: 'Intelligent cryptocurrency trading bot powered by advanced AI algorithms. Uses **CoW Protocol** with optimized limit orders for maximum efficiency. Features automated trading strategies, real-time market analysis, risk management, and comprehensive performance tracking with Telegram notifications.',
            link: 'https://github.com/Saga-Labs/ai-trading-bot',
            isGitHub: true
        },
        {
            name: 'Rebalancer: Crypto Portfolio Bot',
            category: 'Finance',
            image: 'images/balancero-telegram.jpeg',
            gallery: ['images/balancero-telegram.jpeg', 'images/balancero.png'],
            description: 'Automated portfolio rebalancing bot on Base using CoW Protocol. Maintains custom target allocations, tracks performance vs HODL, and sends Telegram alerts. Currently supports cbBTC, WETH, cbXRP, cbADA, cbDOGE, and AAVE — with more coins coming soon.',
            link: 'https://github.com/Saga-Labs/rebalancer',
            isGitHub: true
        },
        {
            name: 'Macro Crypto Dashboard',
            category: 'Finance',
            image: 'images/macro-dashboard1.png',
            description: 'Comprehensive cryptocurrency market analysis dashboard featuring real-time macro indicators, market sentiment analysis, and advanced charting tools. Track key metrics, correlations, and market trends to make informed trading decisions with institutional-grade data visualization.',
            link: 'https://github.com/Saga-Labs/macro-crypto-dashboard',
            isGitHub: true
        },
        {
            name: '3 Tasks: Daily Productivity',
            category: 'Productivity',
            image: 'images/3tasks.png',
            description: 'Focus on what matters most with a simple three-task daily system. Boost your productivity by limiting your daily goals to just three meaningful tasks.',
            link: 'https://apps.apple.com/au/app/3-tasks-daily-productivity/id1553693943'
        },
        {
            name: 'Drop: Relax Focus & Sleep',
            category: 'Health & Fitness',
            image: 'images/drop.png',
            description: 'Find inner peace with guided meditations designed to help you relax, focus better, and sleep soundly. Perfect for busy minds seeking calm.',
            link: 'https://apps.apple.com/au/app/drop-relax-focus-sleep-well/id1462269642'
        },
        {
            name: 'Only Gallery',
            category: 'Utilities',
            image: 'images/photolock.png',
            description: 'Keep your private photos and videos secure with advanced encryption. Your personal memories stay private and protected from prying eyes.',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722'
        },
        {
            name: 'Crypton: Crypto Tracker',
            category: 'Finance',
            image: 'images/crypton.png',
            description: 'Track your cryptocurrency investments with real-time prices and portfolio insights. Stay informed about market trends and manage your crypto assets.',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286'
        },
        {
            name: 'Brainy: Imagine AI Art',
            category: 'Productivity',
            image: 'images/brainyapp.png',
            description: 'Transform your ideas into stunning AI-generated artwork. Create unique digital art pieces with the power of artificial intelligence.',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372'
        },
        {
            name: 'Chat with Fast AI',
            category: 'Productivity',
            image: 'images/chatai.png',
            description: 'Experience lightning-fast AI conversations that help you brainstorm, solve problems, and get instant answers to your questions.',
            link: 'https://apps.apple.com/au/app/chat-with-fast-ai/id1662608035'
        }
    ];

    const appGrid = document.querySelector('.app-grid');
    if (appGrid) {
        appGrid.innerHTML = apps.map((app, index) => `
            <div class="app ${app.isGitHub ? 'github-project' : ''}" data-index="${index}">
                <div class="app-image">
                    ${app.gallery && app.gallery.length ? `
                        <div class="dual-shot">
                            <img class="shot primary" src="${app.gallery[0]}" alt="${app.name} screenshot 1" loading="lazy">
                            <img class="shot secondary" src="${app.gallery[1] || app.gallery[0]}" alt="${app.name} screenshot 2" loading="lazy">
                        </div>
                    ` : `
                        <img src="${app.image}" alt="${app.name}" loading="lazy">
                    `}
                </div>
                <div class="app-content">
                    <div class="category">${app.category}</div>
                    <h3>${app.name}</h3>
                    <p class="description">${app.description.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')}</p>
                    <a href="${app.link}" target="_blank" class="download-btn">
                        ${app.isGitHub ? 
                            '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg> View on GitHub' : 
                            '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg> View on App Store'
                        }
                    </a>
                </div>
            </div>
        `).join('');
    }

    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('animate');
                }, index * 50);
            }
        });
    }, observerOptions);

    // Observe all app elements
    document.querySelectorAll('.app').forEach(app => {
        observer.observe(app);
    });

    // Add staggered animation delays
    document.querySelectorAll('.app').forEach((app, index) => {
        app.style.transitionDelay = `${index * 0.05}s`;
    });
});
