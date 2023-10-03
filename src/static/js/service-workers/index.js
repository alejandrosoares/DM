const staticPath = 'static/js/';

const SERVICE_WORKERS_PATH = [
    staticPath + 'service-workers/assetCache.js',
]


function loadServiceWorkers() {
    if ('serviceWorker' in navigator) {
        SERVICE_WORKERS_PATH.forEach(swPath => {
            navigator.serviceWorker.register(swPath)
                .then(registration => {
                    console.log('Service Worker registered:', registration);
                })
                .catch(error => {
                    console.error('Error registering Service Worker:', error);
                });
        })
    }
}


export default loadServiceWorkers;