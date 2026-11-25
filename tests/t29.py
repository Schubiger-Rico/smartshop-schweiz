# Suche bei «Wo kaufst du das?», Überschrift Geschäfte, Menüpunkt Geschäfte
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n17',greet:'off'},items:[{id:'a',name:'Thon',qty:1,unit:'Stk.',stext:'Aligro'}]}))");pg.reload()
    pg.click('[data-a=shopsel][data-id=draft]')
    print('heading','Geschäfte' in pg.inner_text('.sheet'),'old gone','Lebensmittel-Läden' not in pg.inner_text('.sheet'))
    pg.type('#shq','al')
    vis=pg.evaluate("Array.from(document.querySelectorAll('.sheet [data-a=shtog]')).filter(function(e){return e.offsetParent}).map(function(e){return e.textContent})")
    print('filtered',vis,'focus',pg.evaluate("document.activeElement.id"))
    pg.screenshot(path='/tmp/claude-0/shots/s30.png')
    pg.fill('#shq','');pg.type('#shq','zzq');print('none -> heading hidden',pg.evaluate("Array.from(document.querySelectorAll('.sheet h3.shg')).every(function(e){return !e.offsetParent})"))
    pg.click('.sheet [data-a=shclose] >> nth=-1')
    pg.click('#hamb');print('menu',pg.inner_text('.menu [data-v=shops]').replace('\n',' '))
    pg.click('.menu [data-v=shops]');print('title','Geschäfte' in pg.inner_text('h2'))
    c.close();b.close()
print(errs)
