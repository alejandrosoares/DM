const CACHE_NAME = 'asset-cache-v1';


function fetchResource(event) {
  const response = cacheOrFetch(event);
  event.respondWith(response);
}


async function cacheOrFetch(event) {
  let response = await caches.match(event.request);
  if (response) return response;

  response = await fetch(event.request);
  if (
    !response ||
    response.status !== 200 ||
    response.type !== 'basic' ||
    !isAssetCSS(event.request.url)
  ) {
    return response;
  }

  const clonedResponse = response.clone();
  addCache(event.request, clonedResponse);

  return response;
}


function isAssetCSS(url) {
  const assetsRegExp = /.png|.gif|.jpg|.jpeg|.css|.js/g;
  return assetsRegExp.test(url);
}


function addCache(request, response) {
  caches.open(CACHE_NAME).then(cache => {
    cache.put(request, response);
  })
}


function clearCache(event) {
  const deletePromise = caches.delete(CACHE_NAME);
  event.waitUntil(deletePromise);
}


self.addEventListener('fetch', fetchResource);
self.addEventListener('activate', clearCache);
