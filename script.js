document.addEventListener('DOMContentLoaded', function() {
    const apps = [
        {
            name: '3 Tasks - Daily Productivity',
            category: 'Productivity',
            image: 'images/3%20tasks.png',
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
            name: 'Only Gallery - Keeper',
            category: 'Utilities',
            image: 'images/photo%20lock.png',
            description: 'Keep your private photos and videos secure with advanced encryption. Your personal memories stay private and protected from prying eyes.',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722'
        },
        {
            name: 'Crypton - Crypto Tracker',
            category: 'Finance',
            image: 'images/crypton.png',
            description: 'Track your cryptocurrency investments with real-time prices and portfolio insights. Stay informed about market trends and manage your crypto assets.',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286'
        },
        {
            name: 'Brainy: Imagine AI Art',
            category: 'Productivity',
            image: 'images/brainy.png',
            description: 'Transform your ideas into stunning AI-generated artwork. Create unique digital art pieces with the power of artificial intelligence.',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372'
        },
        {
            name: 'Chat with Fast AI',
            category: 'Productivity',
            image: 'images/chat%20ai.png',
            description: 'Experience lightning-fast AI conversations that help you brainstorm, solve problems, and get instant answers to your questions.',
            link: 'https://apps.apple.com/au/app/chat-with-fast-ai/id1662608035'
        }
    ];

    const appGrid = document.querySelector('.app-grid');
    if (appGrid) {
        appGrid.innerHTML = apps.map((app, index) => `
            <div class="app" data-index="${index}">
                <div class="app-image">
                    <img src="${app.image}" alt="${app.name}" loading="lazy">
                </div>
                <div class="app-content">
                    <div class="category">${app.category}</div>
                    <h3>${app.name}</h3>
                    <p class="description">${app.description}</p>
                    <a href="${app.link}" target="_blank" class="download-btn">
                        Learn More
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
                }, index * 200);
            }
        });
    }, observerOptions);

    // Observe all app elements
    document.querySelectorAll('.app').forEach(app => {
        observer.observe(app);
    });

    // Add staggered animation delays
    document.querySelectorAll('.app').forEach((app, index) => {
        app.style.transitionDelay = `${index * 0.1}s`;
    });
});
