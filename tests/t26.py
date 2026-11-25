# Mehrere Einkaufslisten: anlegen, wechseln, dringend überall, automatisch per Standort, löschen
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n14'},mine:[{name:'Aligro Schlieren',lat:47.2,lon:8.9}]}))");pg.reload()
    print('no bar with one list',pg.locator('#lbar').count()==0)
    pg.fill('#dn','Milch');pg.click('[data-a=add]')
    pg.fill('#dn','Pflaster');pg.click('[data-a=urgtog][data-id=draft]');pg.click('[data-a=add]')
    pg.click('#hamb');pg.click('.menu [data-v=lists]')
    pg.fill('#lnn','Aligro');pg.click('[data-a=listadd]')
    sid=[l['id'] for l in st(pg)['lists'] if l['name']=='Aligro'][0]
    pg.select_option('[data-chg=lstore][data-id="%s"]'%sid,'Aligro Schlieren')
    print('lists',[(l['name'],l.get('store')) for l in st(pg)['lists']])
    pg.click('[data-a=nav][data-v=list] >> nth=0');pg.wait_for_timeout(200)
    pg.click('[data-a=listset][data-v="%s"]'%sid)
    pg.fill('#dn','Rapsöl 5 Liter');pg.click('[data-a=add]')
    a=pg.inner_text('#app');print('aligro shows own + urgent',('Rapsöl' in a,'Pflaster' in a,'Milch' in a))
    pg.click('[data-a=listset][data-v=L0]');a=pg.inner_text('#app');print('allgemein',('Rapsöl' in a,'Pflaster' in a,'Milch' in a),'count chip','Aligro (1)' in a)
    # Löschen
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=lists]')
    pg.click('[data-a=listdel][data-id="%s"]'%sid);pg.click('[data-a=listdelgo]')
    s2=st(pg);print('deleted',len(s2['lists']),'items back',[i['name'] for i in s2['items'] if not i.get('list')])
    c.close()
    # automatisch per Standort
    c=b.new_context(viewport={'width':390,'height':800},geolocation={'latitude':47.2,'longitude':8.9},permissions=['geolocation']);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.route('**/overpass**',lambda r:r.fulfill(status=200,content_type='application/json',body='{"elements":[]}'))
    pg.route('**/api/interpreter**',lambda r:r.fulfill(status=200,content_type='application/json',body='{"elements":[]}'))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n14',gps:'auto',geoAsked:true},mine:[{name:'Aligro Schlieren',lat:47.2,lon:8.9}],lists:[{id:'L0',name:'Allgemein'},{id:'LA',name:'Aligro',store:'Aligro Schlieren'}],items:[{id:'a',name:'Thon',qty:1,unit:'Stk.',list:'LA'},{id:'b',name:'Brot',qty:1,unit:'Stk.'}]}))");pg.reload();pg.wait_for_timeout(2500)
    s3=st(pg);a=pg.inner_text('#app');print('auto open',s3.get('curList'),'Thon' in a,'Brot' in a)
    pg.screenshot(path='/tmp/claude-0/shots/s26.png')
    c.close();b.close()
print(errs)
