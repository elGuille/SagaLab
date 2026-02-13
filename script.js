document.addEventListener('DOMContentLoaded', function () {
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
        contactForm.addEventListener('submit', function (e) {
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
        whatsappBtn.addEventListener('click', function (e) {
            e.preventDefault();
            const contacts = getContactInfo();
            const message = 'Hi! I found your website and would like to get in touch.';
            window.open(`https://wa.me/${contacts.whatsapp}?text=${encodeURIComponent(message)}`, '_blank');
        });
    }

    // Telegram direct link
    const telegramBtn = document.getElementById('telegram-link');
    if (telegramBtn) {
        telegramBtn.addEventListener('click', function (e) {
            e.preventDefault();
            const message = 'Hi! I found your website and would like to get in touch.';
            window.open(`https://t.me/sagalab?text=${encodeURIComponent(message)}`, '_blank');
        });
    }

    // Logo click to scroll to top
    const homeLogo = document.getElementById('home-logo');
    if (homeLogo) {
        homeLogo.addEventListener('click', function (e) {
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
    // AI Tools section removed
    const aiTools = [];

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
            name: 'Pinku Private AI',
            category: 'Productivity',
            image: 'images/pinku.png',
            description: 'Your personal AI assistant that runs entirely on-device. Fast, private conversations powered by advanced language models with zero data collection. Works offline with complete privacy.',
            link: 'https://apps.apple.com/us/app/pinku-private-ai/id6754878073',
            cta: 'Get Pinku',
            techStack: ['SwiftUI', 'Llama', 'Qwen', 'DeepSeek', 'On-device ML', 'iOS'],
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
        // Only show Mobile Apps
        const allApps = [...mobileApps];

        combinedAppsGrid.innerHTML = allApps.map((app, index) => `
            <div class="app" data-index="${index}">
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
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
                            </svg>
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

    // ===== DARK MODE TOGGLE =====
    function toggleTheme() {
        const isDark = document.body.classList.toggle('dark-mode');
        const icon = document.getElementById('nav-theme-icon');
        const iconPath = icon.querySelector('path');

        if (isDark) {
            // Sun icon
            iconPath.setAttribute('d', 'M12 17.5c3.038 0 5.5-2.462 5.5-5.5S15.038 6.5 12 6.5 6.5 8.962 6.5 12s2.462 5.5 5.5 5.5zm0-13V3m0 18v-1.5m6.364-13.864L17.657 6.343M6.343 17.657l-.707.707m12.728 0l.707.707M6.343 6.343l-.707-.707M21 12h1.5M3 12H1.5');
            localStorage.setItem('theme', 'dark');
        } else {
            // Moon icon
            iconPath.setAttribute('d', 'M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z');
            localStorage.setItem('theme', 'light');
        }
    }

    // Initialize theme from saved preference
    window.toggleTheme = toggleTheme;
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

    // ===== NEURAL NETWORK CANVAS =====
    class NeuralNetwork {
        constructor(canvasId) {
            this.canvas = document.getElementById(canvasId);
            if (!this.canvas) return;

            this.ctx = this.canvas.getContext('2d');
            this.width = this.canvas.offsetWidth;
            this.height = this.canvas.offsetHeight;

            this.nodes = [];
            this.mouse = { x: this.width / 2, y: this.height / 2 };
            this.connectionDistance = 250;
            this.nodeCount = 120;
            this.mouseInfluenceRadius = 300;
            this.time = 0;

            this.resizeCanvas();
            this.initNodes();
            this.animate();

            window.addEventListener('resize', () => this.resizeCanvas());
            document.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        }

        resizeCanvas() {
            this.width = this.canvas.width = this.canvas.offsetWidth;
            this.height = this.canvas.height = this.canvas.offsetHeight;
        }

        initNodes() {
            this.nodes = [];
            for (let i = 0; i < this.nodeCount; i++) {
                this.nodes.push({
                    x: Math.random() * this.width,
                    y: Math.random() * this.height,
                    vx: (Math.random() - 0.5) * 0.3,
                    vy: (Math.random() - 0.5) * 0.3,
                    radius: 3 + Math.random() * 3.5,
                    baseOpacity: 0.55 + Math.random() * 0.35
                });
            }
        }

        handleMouseMove(e) {
            const rect = this.canvas.getBoundingClientRect();
            this.mouse.x = e.clientX - rect.left;
            this.mouse.y = e.clientY - rect.top;
        }

        animate() {
            this.time++;
            this.ctx.clearRect(0, 0, this.width, this.height);

            // Update nodes
            this.nodes.forEach(node => {
                node.x += node.vx;
                node.y += node.vy;

                // Bounce off edges with smooth wrapping
                if (node.x < 0) node.x = this.width;
                if (node.x > this.width) node.x = 0;
                if (node.y < 0) node.y = this.height;
                if (node.y > this.height) node.y = 0;

                // Add subtle sine wave motion
                node.vx += Math.sin(this.time * 0.01 + node.x * 0.01) * 0.001;
                node.vy += Math.cos(this.time * 0.01 + node.y * 0.01) * 0.001;

                // Limit velocity
                const speed = Math.sqrt(node.vx * node.vx + node.vy * node.vy);
                if (speed > 0.5) {
                    node.vx = (node.vx / speed) * 0.5;
                    node.vy = (node.vy / speed) * 0.5;
                }
            });

            // Draw connections
            this.nodes.forEach((node1, i) => {
                this.nodes.forEach((node2, j) => {
                    if (i < j) {
                        const dx = node1.x - node2.x;
                        const dy = node1.y - node2.y;
                        const distance = Math.sqrt(dx * dx + dy * dy);

                        if (distance < this.connectionDistance) {
                            const opacity = (1 - distance / this.connectionDistance) * 0.4;
                            const isDark = document.body.classList.contains('dark-mode');
                            const color = isDark
                                ? `rgba(50, 180, 255, ${opacity})`
                                : `rgba(30, 170, 255, ${opacity})`;

                            this.ctx.strokeStyle = color;
                            this.ctx.lineWidth = 1;
                            this.ctx.beginPath();
                            this.ctx.moveTo(node1.x, node1.y);
                            this.ctx.lineTo(node2.x, node2.y);
                            this.ctx.stroke();
                        }
                    }
                });
            });

            // Draw nodes
            this.nodes.forEach(node => {
                const dx = node.x - this.mouse.x;
                const dy = node.y - this.mouse.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                const influence = Math.max(0, 1 - distance / this.mouseInfluenceRadius);
                const pulsate = 0.5 + Math.sin(this.time * 0.02 + node.x * 0.01) * 0.5;

                const isDark = document.body.classList.contains('dark-mode');
                const baseOpacity = node.baseOpacity * pulsate;
                const totalOpacity = Math.min(0.85, baseOpacity + influence * 0.5);
                const color = isDark
                    ? `rgba(80, 200, 255, ${totalOpacity})`
                    : `rgba(50, 180, 255, ${totalOpacity})`;

                this.ctx.fillStyle = color;
                this.ctx.beginPath();
                this.ctx.arc(node.x, node.y, node.radius + influence * 1.5, 0, Math.PI * 2);
                this.ctx.fill();
            });

            requestAnimationFrame(() => this.animate());
        }
    }

    // Initialize neural network
    new NeuralNetwork('neural-network-canvas');
});
