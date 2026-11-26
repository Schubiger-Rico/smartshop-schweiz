# «Laden wählen»: Neuer Laden zuoberst, Suche über alle, «Alle anzeigen» nach ABC
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n19',greet:'off'},mine:[{name:'Bäckerei Gabriel',lat:1,lon:1},{name:'Schubiger',lat:1,lon:1}]}))");pg.reload()
    pg.click('[data-a=storepick]')
    order=pg.evaluate("[document.querySelector('#nsn'),document.querySelector('#stq')].map(function(e){return Math.round(e.getBoundingClientRect().top)})")
    print('new above search',order[0]<order[1],'list hidden',pg.locator('#stres [data-a=storeset]:visible').count()==0)
    pg.type('#stq','bä');print('search',pg.locator('#stres [data-a=storeset]:visible').all_inner_texts())
    pg.fill('#stq','');pg.type('#stq','zzz');print('none msg',pg.locator('#stnone').is_visible())
    pg.fill('#stq','');pg.click('[data-a=storeall]')
    rows=pg.evaluate("Array.from(document.querySelectorAll('#stres .abc')).slice(0,4).map(function(g){return g.querySelector('b').textContent+': '+Array.from(g.querySelectorAll('.btn')).map(function(x){return x.textContent}).join(', ')})")
    print('abc',rows)
    pg.screenshot(path='/tmp/claude-0/shots/s35.png')
    pg.click('#stres [data-n=Volg]');print('chosen','Volg' in pg.inner_text('#app'))
    c.close();b.close()
print(errs)
