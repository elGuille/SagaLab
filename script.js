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
    
    // Optimized smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.getBoundingClientRect().top + window.pageYOffset - 80;
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
            const mailtoLink = `mailto:sagalabs@proton.me?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;
            
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
        };
    };
    
    // Direct messaging app links
    const whatsappBtn = document.getElementById('whatsapp-link');
    
    
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

    // Enhanced app data with benefit-focused descriptions
    const aiTools = [
        {
            name: 'Foro: AI Forum',
            category: 'AI Research',
            image: 'images/foro.png',
            description: 'Watch AI agents discuss any topic in real-time. Perfect for research, brainstorming, and exploring complex ideas with 100+ AI models including local ones for complete privacy.',
            link: 'https://github.com/Saga-Labs/foro',
            isGitHub: true,
            cta: 'Try Foro AI',
            techStack: ['Python', 'LangChain', 'OpenAI', 'Anthropic', 'Ollama', 'Streamlit']
        },
        {
            name: 'AI Trading Bot',
            category: 'AI Research',
            image: 'images/bot-running-screenshot.png',
            gallery: ['images/telegram-notifications.png', 'images/bot-running-screenshot.png'],
            description: 'Boost trading performance with AI-powered automation. Advanced strategies, real-time analysis, and risk management on CoW Protocol with instant Telegram notifications.',
            link: 'https://github.com/Saga-Labs/ai-trading-bot',
            isGitHub: true,
            cta: 'Start Trading',
            techStack: ['Python', 'OpenAI', 'CoW Protocol', 'Web3', 'Telegram API', 'DeFi']
        },
        {
            name: 'Rebalancer: Portfolio Bot',
            category: 'AI Research',
            image: 'images/balancero-telegram.jpeg',
            gallery: ['images/balancero-telegram.jpeg', 'images/balancero.png'],
            description: 'Automatically optimize your crypto portfolio on Base. Track performance vs HODL with custom allocations, supporting cbBTC, WETH, cbXRP, cbADA, DOGE, AAVE.',
            link: 'https://github.com/Saga-Labs/rebalancer',
            isGitHub: true,
            cta: 'Optimize Portfolio',
            techStack: ['Python', 'Base', 'Web3.py', 'Telegram API', 'Smart Contracts']
        },
        {
            name: 'Macro Crypto Dashboard',
            category: 'AI Research',
            image: 'images/macro-dashboard1.png',
            description: 'Make informed trading decisions with institutional-grade market analysis. Real-time macro indicators, sentiment analysis, and advanced charting tools.',
            link: 'https://github.com/Saga-Labs/macro-crypto-dashboard',
            isGitHub: true,
            cta: 'View Dashboard',
            techStack: ['Python', 'Streamlit', 'CoinGecko API', 'Pandas', 'Plotly']
        }
    ];
    
    const mobileApps = [
        {
            name: 'Dora Make Videos with Sora 2',
            category: 'Video Creation',
            image: 'images/dora.png',
            description: 'Make stunning videos with OpenAI\'s powerful Sora 2. Transform your imagination into reality with AI-powered video generation in seconds.',
            link: 'https://apps.apple.com/us/app/id6754180384',
            cta: 'Make Videos',
            techStack: ['SwiftUI', 'Sora 2', 'OpenAI', 'Video Processing', 'iOS'],
            appStoreFeatured: true
        },
        {
            name: '3 Tasks: Daily Productivity',
            category: 'Productivity',
            image: 'images/3tasks.png',
            description: 'Achieve more by doing less. Focus on what matters most with a simple three-task daily system that boosts productivity and reduces overwhelm.',
            link: 'https://apps.apple.com/au/app/3-tasks-daily-productivity/id1553693943',
            cta: 'Download App',
            techStack: ['Swift', 'SwiftUI', 'CloudKit', 'WidgetKit', 'iOS'],
            appStoreFeatured: true
        },
        {
            name: 'Brainy: AI Helper',
            category: 'Productivity',
            image: 'images/brainyapp.png',
            description: 'Your personal AI assistant for writing, brainstorming, and creative tasks. Powered by advanced language models.',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372',
            cta: 'Get Help',
            techStack: ['Swift', 'OpenAI', 'Claude API', 'Core ML', 'iOS'],
            appStoreFeatured: true
        },
        {
            name: 'Crypton: Crypto Tracker',
            category: 'Finance',
            image: 'images/crypton.png',
            description: 'Stay ahead of crypto markets with real-time tracking and portfolio insights. Monitor trends and manage your digital assets with confidence.',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286',
            cta: 'Track Portfolio',
            techStack: ['Swift', 'CoinGecko API', 'Charts', 'Push Notifications', 'iOS'],
            appStoreFeatured: false
        },
        {
            name: 'Focus Meditation',
            category: 'Health & Wellness',
            image: 'images/drop.png',
            description: 'Find inner peace with guided meditations and sleep sounds. Reduce stress, improve focus, and sleep better.',
            link: 'https://apps.apple.com/au/app/drop-relax-focus-sleep-well/id1462269642',
            cta: 'Start Meditating',
            techStack: ['Swift', 'AVFoundation', 'HealthKit', 'Core Audio', 'iOS'],
            appStoreFeatured: true
        },
        {
            name: 'Keeper: Private Folder',
            category: 'Security',
            image: 'images/photolock.png',
            description: 'Protect your private moments with military-grade encryption. Keep your photos, videos, and documents completely secure.',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722',
            cta: 'Secure Files',
            techStack: ['Swift', 'CryptoKit', 'PhotoKit', 'Biometrics', 'iOS'],
            appStoreFeatured: false
        }
    ];

    // Render Combined Apps section (AI Tools + Mobile Apps)
    const combinedAppsGrid = document.querySelector('.combined-apps-grid');
    if (combinedAppsGrid) {
        // Combine all apps - Mobile Apps first, then AI Tools
        const allApps = [...mobileApps, ...aiTools];

        combinedAppsGrid.innerHTML = allApps.map((app, index) => `
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
                    ${app.appStoreFeatured ? `
                        <div class="app-store-badge">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
                            </svg>
                            <span>APP STORE FEATURED</span>
                        </div>
                    ` : ''}
                    <a href="${app.link}" target="_blank" class="download-btn">
                        ${app.isGitHub ? `
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                            </svg>
                        ` : `
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
                            </svg>
                        `}
                        ${app.cta}
                    </a>
                </div>
            </div>
        `).join('');
    }

    // Optimized Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.15,
        rootMargin: '0px 0px -30px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                observer.unobserve(entry.target); // Stop observing once animated
            }
        });
    }, observerOptions);

    // Wait for content to be rendered, then observe elements
    setTimeout(() => {
        const apps = document.querySelectorAll('.app');

        // Animate the first product immediately without scroll
        if (apps.length > 0) {
            apps[0].classList.add('animate');
        }

        // Observe remaining products
        apps.forEach((app, index) => {
            if (index > 0) {
                observer.observe(app);
            }
        });

        // Add staggered animation delays
        apps.forEach((app, index) => {
            app.style.transitionDelay = `${index * 0.025}s`;
        });
    }, 100);
});
