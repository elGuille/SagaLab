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
            image: 'images/dora.webp',
            description: 'Create any type of video with AI using top-tier models like Sora, Kling, Luma, Nano Banana Pro, Seedance, and Grok. Transform your imagination into cinematic reality in seconds.',
            link: 'https://apps.apple.com/us/app/id6754180384',
            cta: 'Make Videos',
            appStoreFeatured: true
        },
        {
            name: 'Pinku Private AI',
            category: 'Productivity',
            image: 'images/pinku.webp',
            description: 'Your personal AI assistant that runs entirely on-device. Fast, private conversations powered by advanced language models with zero data collection. Works offline with complete privacy.',
            link: 'https://apps.apple.com/us/app/pinku-private-ai/id6754878073',
            cta: 'Get Pinku',
            appStoreFeatured: true
        },
        {
            name: '3 Tasks: Daily Productivity',
            category: 'Productivity',
            image: 'images/3tasks.webp',
            description: 'Achieve more by doing less. Focus on what matters most with a simple three-task daily system that boosts productivity and reduces overwhelm.',
            link: 'https://apps.apple.com/au/app/3-tasks-daily-productivity/id1553693943',
            cta: 'Download App',
            appStoreFeatured: true
        },
        {
            name: 'Brainy: AI Helper',
            category: 'Productivity',
            image: 'images/brainyapp.webp',
            description: 'Your personal AI assistant for writing, brainstorming, and creative tasks. Powered by advanced language models.',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372',
            cta: 'Get Help',
            appStoreFeatured: true
        },
        {
            name: 'Crypton: Crypto Tracker',
            category: 'Finance',
            image: 'images/crypton.webp',
            description: 'Stay ahead of crypto markets with real-time tracking and portfolio insights. Monitor trends and manage your digital assets with confidence.',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286',
            cta: 'Track Portfolio',
            appStoreFeatured: false
        },
        {
            name: 'Focus Meditation',
            category: 'Health & Wellness',
            image: 'images/drop.webp',
            description: 'Find inner peace with guided meditations and sleep sounds. Reduce stress, improve focus, and sleep better.',
            link: 'https://apps.apple.com/au/app/drop-relax-focus-sleep-well/id1462269642',
            cta: 'Start Meditating',
            appStoreFeatured: true
        },
        {
            name: 'Keeper: Private Folder',
            category: 'Security',
            image: 'images/photolock.webp',
            description: 'Protect your private moments with military-grade encryption. Keep your photos, videos, and documents completely secure.',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722',
            cta: 'Secure Files',
            appStoreFeatured: false
        }
    ];

    // Render Apps
    const combinedGrid = document.querySelector('.combined-apps-grid');
    if (combinedGrid) {
        combinedGrid.innerHTML = mobileApps.map((app, index) => {
            const layoutClass = index % 2 === 0 ? 'app-showcase-row' : 'app-showcase-row reverse';
            return `
            <div class="${layoutClass}">
                <div class="app-showcase-content">
                    <span class="app-showcase-category">${app.category}</span>
                    <h3 class="app-showcase-title">${app.name}</h3>
                    <p class="app-showcase-desc">${app.description}</p>
                    <div class="app-showcase-actions">
                        <a href="${app.link}" target="_blank" class="app-showcase-btn" rel="noopener noreferrer">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.05 20.28c-.98.95-2.05.8-3.08.35-1.09-.46-2.09-.48-3.24 0-1.44.62-2.2.44-3.06-.35C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
                            </svg>
                            ${app.cta}
                        </a>
                    </div>
                </div>
                <div class="app-showcase-visual">
                    <img src="${app.image}" alt="${app.name} interface" loading="lazy" class="app-showcase-img">
                </div>
            </div>
            `;
        }).join('');
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

    // Neural Network Canvas
    class NeuralNetwork {
        constructor(canvasId) {
            this.canvas = document.getElementById(canvasId);
            if (!this.canvas) return;

            this.ctx = this.canvas.getContext('2d');
            this.nodes = [];
            this.mouse = { x: -1000, y: -1000 };
            this.connectionDistance = 220;
            this.nodeCount = 100;
            this.mouseInfluenceRadius = 250;
            this.time = 0;

            this.resizeCanvas();
            this.initNodes();
            this.animate();

            window.addEventListener('resize', () => this.resizeCanvas());
            document.addEventListener('mousemove', (e) => {
                const rect = this.canvas.getBoundingClientRect();
                this.mouse.x = e.clientX - rect.left;
                this.mouse.y = e.clientY - rect.top;
            });
        }

        resizeCanvas() {
            this.canvas.width = window.innerWidth;
            this.canvas.height = window.innerHeight;
        }

        initNodes() {
            this.nodes = [];
            for (let i = 0; i < this.nodeCount; i++) {
                this.nodes.push({
                    x: Math.random() * this.canvas.width,
                    y: Math.random() * this.canvas.height,
                    vx: (Math.random() - 0.5) * 0.3,
                    vy: (Math.random() - 0.5) * 0.3,
                    radius: 2.5 + Math.random() * 3,
                    baseOpacity: 0.5 + Math.random() * 0.35
                });
            }
        }

        animate() {
            this.time++;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

            const isDark = document.body.classList.contains('dark-mode');

            // Update nodes
            this.nodes.forEach(node => {
                node.x += node.vx;
                node.y += node.vy;

                if (node.x < 0) node.x = this.canvas.width;
                if (node.x > this.canvas.width) node.x = 0;
                if (node.y < 0) node.y = this.canvas.height;
                if (node.y > this.canvas.height) node.y = 0;

                node.vx += Math.sin(this.time * 0.01 + node.x * 0.01) * 0.001;
                node.vy += Math.cos(this.time * 0.01 + node.y * 0.01) * 0.001;

                const speed = Math.sqrt(node.vx * node.vx + node.vy * node.vy);
                if (speed > 0.5) {
                    node.vx = (node.vx / speed) * 0.5;
                    node.vy = (node.vy / speed) * 0.5;
                }
            });

            // Draw connections
            for (let i = 0; i < this.nodes.length; i++) {
                for (let j = i + 1; j < this.nodes.length; j++) {
                    const dx = this.nodes[i].x - this.nodes[j].x;
                    const dy = this.nodes[i].y - this.nodes[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < this.connectionDistance) {
                        const opacity = (1 - distance / this.connectionDistance) * 0.35;
                        this.ctx.strokeStyle = isDark
                            ? `rgba(50, 180, 255, ${opacity})`
                            : `rgba(30, 150, 255, ${opacity})`;
                        this.ctx.lineWidth = 1;
                        this.ctx.beginPath();
                        this.ctx.moveTo(this.nodes[i].x, this.nodes[i].y);
                        this.ctx.lineTo(this.nodes[j].x, this.nodes[j].y);
                        this.ctx.stroke();
                    }
                }
            }

            // Draw nodes
            this.nodes.forEach(node => {
                const dx = node.x - this.mouse.x;
                const dy = node.y - this.mouse.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                const influence = Math.max(0, 1 - distance / this.mouseInfluenceRadius);
                const pulsate = 0.5 + Math.sin(this.time * 0.02 + node.x * 0.01) * 0.5;

                const baseOpacity = node.baseOpacity * pulsate;
                const totalOpacity = Math.min(0.8, baseOpacity + influence * 0.5);

                this.ctx.fillStyle = isDark
                    ? `rgba(80, 200, 255, ${totalOpacity})`
                    : `rgba(50, 150, 255, ${totalOpacity})`;
                this.ctx.beginPath();
                this.ctx.arc(node.x, node.y, node.radius + influence * 1.5, 0, Math.PI * 2);
                this.ctx.fill();
            });

            requestAnimationFrame(() => this.animate());
        }
    }

    new NeuralNetwork('neural-network-canvas');
});
