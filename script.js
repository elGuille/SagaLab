document.addEventListener('DOMContentLoaded', function() {
    const apps = [
        {
            name: 'Brainy: Imagine AI Art',
            category: 'Productivity',
            image: 'images/Brainy.png',
            link: 'https://apps.apple.com/au/developer/saga-ltd/id1142866018'
        },
        {
            name: 'Chat with Fast AI',
            category: 'Productivity',
            image: 'images/Chat AI.png',
            link: 'https://apps.apple.com/au/developer/saga-ltd/id1142866018'
        },
        {
            name: 'Drop: Relax Focus & Sleep',
            category: 'Health & Fitness',
            image: 'images/Drop meditation.png',
            link: 'https://apps.apple.com/au/developer/saga-ltd/id1142866018'
        },
        {
            name: 'Crypton - Crypto Tracker',
            category: 'Finance',
            image: 'images/Crypto.png',
            link: 'https://apps.apple.com/au/developer/saga-ltd/id1142866018'
        },
        {
            name: '3 Tasks - Daily Productivity',
            category: 'Productivity',
            image: 'images/3 Tasks - Daily.png',
            link: 'https://apps.apple.com/au/developer/saga-ltd/id1142866018'
        },
        {
            name: 'Only Gallery - Keeper',
            category: 'Utilities',
            image: 'images/Photo locker.png',
            link: 'https://apps.apple.com/au/developer/saga-ltd/id1142866018'
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