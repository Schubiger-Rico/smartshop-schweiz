# Neuer Laden hier, Standort-Erklärung, Hilfe bei gesperrtem Standort
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch()
    # erlaubt
    c=b.new_context(viewport={'width':390,'height':800},geolocation={'latitude':47.2,'longitude':8.9},permissions=['geolocation']);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n13'}}))");pg.reload()
    pg.click('[data-a=storepick]');pg.fill('#nsn','Hofladen Huber');pg.click('[data-a=storenew]');pg.wait_for_timeout(500)
    print('saved',[m['name'] for m in st(pg)['mine']],'current',pg.inner_text('#app').count('📍 Hofladen Huber'))
    c.close()
    # noch nicht gefragt -> Erklärung
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n13',gps:'auto'}}))");pg.reload();pg.wait_for_timeout(300)
    print('no auto prompt at open',pg.locator('[data-a=geogo]').count()==0)
    pg.click('[data-a=gpsrefresh]');pg.wait_for_timeout(300);print('intro shown',pg.locator('[data-a=geogo]').count())
    c.close()
    # gesperrt -> Hilfe
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("navigator.permissions.query=function(){return Promise.resolve({state:'denied'})}")
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n13'}}))");pg.reload()
    pg.click('[data-a=gpsrefresh]');pg.wait_for_timeout(300);print('help shown',pg.inner_text('.sheet').count('Ortungsdienste'))
    c.close();b.close()
print(errs)
