# Erinnerung an andere Läden + Neu in sEBU
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html')
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},items:[{id:'c',name:'Mehl',qty:1,unit:'kg',stores:['Coop'],cat:'m3'}],set:{rem:{open:true,start:true,end:true,always:false}}}))");pg.reload()
    print('news banner',pg.locator('[data-a=newsopen]').count())
    print('rem banner on open',pg.inner_text('#app').count('Für andere Läden noch'))
    pg.click('[data-a=remx]');print('after x',pg.inner_text('#app').count('Für andere Läden noch'))
    pg.click('[data-a=newsopen]');print('news rows',pg.locator('.sheet .row').count(),'show btns',pg.locator('.sheet [data-a=newsshow]').count())
    pg.click('[data-a=newsshow][data-v=n03]');pg.wait_for_timeout(300);print('mini tour',pg.inner_text('.tc .small.mute'),'hl',pg.locator('.hl').count())
    pg.click('[data-a=tnext]');pg.wait_for_timeout(200);print('tour ended',pg.locator('.tc').count()==0,'news seen',st(pg)['set']['newsSeen'],'banner gone',pg.locator('[data-a=newsopen]').count()==0)
    # start shopping in Migros (simulated) -> start reminder
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.shop={store:'Migros',chain:'Migros',t:Date.now(),seq:[]};localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload()
    print('start reminder',pg.inner_text('#app').count('Für andere Läden noch'))
    # per-product ask when assigning store
    pg.fill('#dn','Reis');pg.click('[data-a=shopsel][data-id=draft]');pg.click('[data-a=shtog][data-v=Lidl]');pg.click('[data-a=shok]')
    print('ask sheet',pg.locator('[data-remp]').count())
    pg.click('[data-remp=always]');pg.click('[data-remp=end]');pg.click('[data-a=remok]');pg.click('[data-a=add]')
    r=[i for i in st(pg)['items'] if i['name']=='Reis'][0].get('rem');print('item rem',r)
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.shop=null;s.set.rem={open:false,start:false,end:false,always:false};localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload()
    print('always stays (Reis, no x)',pg.inner_text('#app').count('Reis (Lidl)'),pg.locator('[data-a=remx]').count())
    pg.click('[data-a=remoff]');pg.wait_for_timeout(200);print('remoff gone',pg.inner_text('#app').count('Reis (Lidl)'),'still on list',[i['name'] for i in st(pg)['items']].count('Reis'))
    b.close()
print(errs)
