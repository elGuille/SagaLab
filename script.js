document.addEventListener('DOMContentLoaded', function() {
    const apps = [
        {
            name: '3 Tasks - Daily Productivity',
            category: 'Productivity',
            image: 'images/3 Tasks - Daily.png',
            link: 'https://apps.apple.com/au/app/3-tasks-daily-productivity/id1553693943'
        },
        {
            name: 'Drop: Relax Focus & Sleep',
            category: 'Health & Fitness',
            image: 'images/Drop meditation.png',
            link: 'https://apps.apple.com/au/app/drop-relax-focus-sleep-well/id1462269642'
        },
        {
            name: 'Only Gallery - Keeper',
            category: 'Utilities',
            image: 'images/Photo locker.png',
            link: 'https://apps.apple.com/au/app/only-gallery-keeper/id1532670722'
        },
        {
            name: 'Crypton - Crypto Tracker',
            category: 'Finance',
            image: 'images/Crypto.png',
            link: 'https://apps.apple.com/au/app/crypton-crypto-tracker/id1143691286'
        },
        {
            name: 'Brainy: Imagine AI Art',
            category: 'Productivity',
            image: 'images/Brainy.png',
            link: 'https://apps.apple.com/au/app/brainy-imagine-ai-art/id1667947372'
        },
        {
            name: 'Chat with Fast AI',
            category: 'Productivity',
            image: 'images/Chat AI.png',
            link: 'https://apps.apple.com/au/app/chat-with-fast-ai/id1662608035'
        }
    ];

    const appGrid = document.querySelector('.app-grid');
    if (appGrid) {
        appGrid.innerHTML = apps.map(app => `
            <a href="${app.link}" target="_blank" class="app">
                <img src="${app.image}" alt="${app.name}">
                <div class="app-info">
                    <h3>${app.name}</h3>
                    <p>${app.category}</p>
                </div>
            </a>
        `).join('');
    }
}); 