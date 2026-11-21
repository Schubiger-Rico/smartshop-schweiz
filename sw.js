var C='sebu-v2',F=['./','./index.html','./manifest.json','./icon-180.png'];
self.addEventListener('install',function(e){e.waitUntil(caches.open(C).then(function(c){return c.addAll(F)}).then(function(){return self.skipWaiting()}))});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(k){return Promise.all(k.filter(function(x){return x!==C}).map(function(x){return caches.delete(x)}))}).then(function(){return self.clients.claim()}))});
self.addEventListener('fetch',function(e){var r=e.request,u=new URL(r.url);if(r.method!=='GET')return;
 if(/googleapis|gstatic/.test(u.host)||u.origin===location.origin){/* eigene Dateien immer frisch beim Server nachfragen (still, ohne Internet aus dem Speicher) */
  var q=u.origin===location.origin?fetch(r.url,{cache:'no-cache',credentials:'same-origin'}):fetch(r);
  e.respondWith(q.then(function(x){var y=x.clone();caches.open(C).then(function(c){c.put(r,y)});return x}).catch(function(){return caches.match(r).then(function(m){return m||caches.match('./index.html')})}))}});
