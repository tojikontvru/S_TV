const CACHE_NAME='stv-v1';
const ASSETS=['/S_TV/','/S_TV/index.html','/S_TV/manifest.json'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE_NAME).then(c=>c.addAll(ASSETS)));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE_NAME).map(k=>caches.delete(k)))));self.clients.claim()});
self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(resp=>{if(resp.status===200){const clone=resp.clone();caches.open(CACHE_NAME).then(c=>c.put(e.request,clone))}return resp}).catch(()=>caches.match('/S_TV/index.html'))))});
