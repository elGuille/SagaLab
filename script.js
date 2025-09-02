document.addEventListener('DOMContentLoaded', function() {
    // Navigation toggle functionality
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking on a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed nav
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Contact form functionality - now uses mailto
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const name = formData.get('name');
            const email = formData.get('email');
            const subject = formData.get('subject');
            const message = formData.get('message');
            
            // Create email body
            const emailBody = `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`;
            const mailtoLink = `mailto:shogn@icloud.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;
            
            // Open email client
            window.location.href = mailtoLink;
            
            // Show success message
            const submitBtn = contactForm.querySelector('.submit-btn');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> Email Opened!';
            submitBtn.style.background = 'linear-gradient(135deg, #34d399 0%, #10b981 100%)';
            
            // Reset form and button after 3 seconds
            setTimeout(() => {
                contactForm.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.style.background = 'linear-gradient(135deg, #007AFF 0%, #5856D6 100%)';
            }, 3000);
        });
    }
    
    // Obfuscated contact info for privacy
    const getContactInfo = () => {
        const base = '16469329487';
        const tg = 'sagalab';
        return {
            telegram: tg,
            whatsapp: base,
            signal: base
        };
    };
    
    // Direct messaging app links
    const signalBtn = document.getElementById('signal-link');
    const whatsappBtn = document.getElementById('whatsapp-link');
    
    if (signalBtn) {
        signalBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const contacts = getContactInfo();
            const message = 'Hi! I found your website and would like to get in touch.';
            navigator.clipboard.writeText(message).then(() => {
                alert(`Message copied to clipboard!\n\nPlease open Signal and send this message to: +${contacts.signal}`);
            }).catch(() => {
                alert(`Please contact us via Signal at: +${contacts.signal}\n\nMessage: ${message}`);
            });
        });
    }
    
    if (whatsappBtn) {
        whatsappBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const contacts = getContactInfo();
            const message = 'Hi! I found your website and would like to get in touch.';
            window.open(`https://wa.me/${contacts.whatsapp}?text=${encodeURIComponent(message)}`, '_blank');
        });
    }
    
    // Telegram direct link
    const telegramBtn = document.getElementById('telegram-link');
    if (telegramBtn) {
        telegramBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const message = 'Hi! I found your website and would like to get in touch.';
            window.open(`https://t.me/sagalab?text=${encodeURIComponent(message)}`, '_blank');
        });
    }
    
    // Logo click to scroll to top
    const homeLogo = document.getElementById('home-logo');
    if (homeLogo) {
        homeLogo.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // Add footer links if they don't exist
    const footer = document.querySelector('footer .container');
    if (footer && !footer.querySelector('.footer-links')) {
        const footerContent = footer.innerHTML;
        footer.innerHTML = `
            ${footerContent}
            <div class="footer-links">
                <a href="terms.html">Terms of Service</a>
                <a href="privacy.html">Privacy Policy</a>
            </div>
        `;
    }

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
    // Enhanced app data with benefit-focused descriptions
    const aiTools = [
        {
            name: 'Foro: AI Forum',
            category: 'AI Research',
            image: 'images/foro.png',
            description: 'Watch AI agents discuss any topic in real-time. Perfect for research, brainstorming, and exploring complex ideas with 100+ AI models including local ones for complete privacy.',
            link: 'https://github.com/Saga-Labs/foro',
            isGitHub: true,
            cta: 'Try Foro AI'
        },
        {
            name: 'AI Trading Bot',
            category: 'AI Research',
            image: 'images/bot-running-screenshot.png',
            gallery: ['images/telegram-notifications.png', 'images/bot-running-screenshot.png'],
            description: 'Boost trading performance with AI-powered automation. Advanced strategies, real-time analysis, and risk management on CoW Protocol with instant Telegram notifications.',
            link: 'https://github.com/Saga-Labs/ai-trading-bot',
            isGitHub: true,
            cta: 'Start Trading'
        },
        {
            name: 'Rebalancer: Portfolio Bot',
            category: 'AI Research',
            image: 'images/balancero-telegram.jpeg',
            gallery: ['images/balancero-telegram.jpeg', 'images/balancero.png'],
            description: 'Automatically optimize your crypto portfolio on Base. Track performance vs HODL with custom allocations, supporting cbBTC, WETH, cbXRP, cbADA, DOGE, AAVE.',
            link: 'https://github.com/Saga-Labs/rebalancer',
            isGitHub: true,
            cta: 'Optimize Portfolio'
        },
        {
            name: 'Macro Crypto Dashboard',
            category: 'AI Research',
            image: 'images/macro-dashboard1.png',
            description: 'Make informed trading decisions with institutional-grade market analysis. Real-time macro indicators, sentiment analysis, and advanced charting tools.',
            link: 'https://github.com/Saga-Labs/macro-crypto-dashboard',
            isGitHub: true,
            cta: 'View Dashboard'
        }
    ];
    
    const mobileApps = [
        {
            name: '3 Tasks: Daily Productivity',
            category: 'Productivity',
            image: 'images/3tasks.png',
            description: 'Achieve more by doing less. Focus on what matters most with a simple three-task daily system that boosts productivity and reduces overwhelm.',
            link: 'https://apps.apple.com/au/app/3-tasks-daily-productivity/id1553693943',
            cta: 'Download App'
        },
        {
            name: 'Drop: Relax Focus & Sleep',
            category: 'Health & Fitness',
            image: 'images/drop.png',
            description: 'Find inner peace with guided meditations. Designed to help you relax, focus better, and sleep soundly. Perfect for busy minds seeking calm.',
            link: 'https://apps.apple.com/au/app/drop-relax-focus-sleep-well/id1462269642',
            cta: 'Start Meditating'
        },
        {
            name: 'Only Gallery',
            category: 'Utilities',
            image: 'images/photolock.png',
            description: 'Protect your private moments with military-grade encryption. Keep your personal photos and videos secure from prying eyes.',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722',
            cta: 'Secure Photos'
        },
        {
            name: 'Crypton: Crypto Tracker',
            category: 'Finance',
            image: 'images/crypton.png',
            description: 'Stay ahead of crypto markets with real-time tracking and portfolio insights. Monitor trends and manage your digital assets with confidence.',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286',
            cta: 'Track Portfolio'
        },
        {
            name: 'Brainy: Imagine AI Art',
            category: 'Productivity',
            image: 'images/brainyapp.png',
            description: 'Transform your ideas into stunning AI-generated artwork. Create unique digital art pieces with the power of artificial intelligence.',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372',
            cta: 'Create Art'
        }
    ];

    // Render AI Tools section
    const aiToolsGrid = document.querySelector('.ai-tools-grid');
    if (aiToolsGrid) {
        aiToolsGrid.innerHTML = aiTools.map((app, index) => `
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
                    <p class="description">${app.description}</p>
                    <a href="${app.link}" target="_blank" class="download-btn">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                        </svg>
                        ${app.cta}
                    </a>
                </div>
            </div>
        `).join('');
    }
    
    // Render Mobile Apps section
    const mobileAppsGrid = document.querySelector('.mobile-apps-grid');
    if (mobileAppsGrid) {
        mobileAppsGrid.innerHTML = mobileApps.map((app, index) => `
            <div class="app" data-index="${index + 4}">
                <div class="app-image">
                    <img src="${app.image}" alt="${app.name}" loading="lazy">
                </div>
                <div class="app-content">
                    <div class="category">${app.category}</div>
                    <h3>${app.name}</h3>
                    <p class="description">${app.description}</p>
                    <a href="${app.link}" target="_blank" class="download-btn">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                        </svg>
                        ${app.cta}
                    </a>
                    <a href="#" id="signal-link" class="msg-btn signal-btn">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.94-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/>
                        </svg>
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
                }, index * 25);
            }
        });
    }, observerOptions);

    // Wait for content to be rendered, then observe elements
    setTimeout(() => {
        document.querySelectorAll('.app').forEach(app => {
            observer.observe(app);
        });

        // Add staggered animation delays
        document.querySelectorAll('.app').forEach((app, index) => {
            app.style.transitionDelay = `${index * 0.025}s`;
        });
    }, 100);
});
