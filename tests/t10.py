# «Welcher Laden?» bei zwei fast gleich nahen Läden
from playwright.sync_api import sync_playwright
import os,json
errs=[]
def ov(route):
    body={'elements':[{'type':'node','lat':47.0,'lon':8.0,'tags':{'shop':'supermarket','name':'Migros Test','brand':'Migros'}},{'type':'node','lat':47.00005,'lon':8.0,'tags':{'shop':'supermarket','name':'Coop Test','brand':'Coop'}}]}
    route.fulfill(status=200,body=json.dumps(body),content_type='application/json')
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();c=b.new_context(viewport={'width':390,'height':800},geolocation={'latitude':47.0,'longitude':8.0,'accuracy':10},permissions=['geolocation'])
    c.route('https://overpass-api.de/**',ov);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{gps:'auto',radius:'auto'}}))");pg.reload()
    pg.wait_for_timeout(1500)
    print('pick banner',pg.locator('[data-a=pick]').count(),'(2)','cur none',pg.locator('[data-a=yes]').count())
    print(pg.locator('#pickban').inner_text().replace('\n',' | '))
    pg.click('[data-a=pick][data-v="1"]');pg.wait_for_timeout(200)
    print('chosen banner',pg.inner_text('#app').count('📍 Coop Test'),'learned',st(pg)['learn'].get('pick'))
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.shop=null;localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload();pg.wait_for_timeout(1500)
    print('2nd time no question',pg.locator('[data-a=pick]').count(),'auto Coop',pg.inner_text('#app').count('📍 Coop Test'))
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.learn.pick={};s.shop=null;localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload();pg.wait_for_timeout(1500)
    pg.click('[data-a=pickno]');pg.wait_for_timeout(200);print('after Keiner',pg.locator('[data-a=pick]').count(),pg.locator('.ban').all_inner_texts())
    pg.screenshot(path='s10.png')
    b.close()
print(errs)
