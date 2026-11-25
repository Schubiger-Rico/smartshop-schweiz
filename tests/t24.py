# Heute nicht, Nach dem Einkaufen erinnern, Standort für eigene Läden, Preise
from playwright.sync_api import sync_playwright
import os,datetime
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();c=b.new_context(viewport={'width':390,'height':800},geolocation={'latitude':47.2,'longitude':8.9},permissions=['geolocation']);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html')
    today=pg.evaluate("(function(){var d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')})()")
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n11',rem:{open:false,start:false,end:true,always:false}},items:[{id:'a',name:'Balsamico',qty:1,unit:'Stk.',stores:['Coop'],today:'%s'},{id:'b',name:'Wurst',qty:1,unit:'Stk.',stext:'Metzgerei Müller'}]}))"%today);pg.reload()
    print('today banner',pg.inner_text('#app').count('Heute noch'))
    pg.click('[data-a=remind]');print('remNext set',[i.get('remNext') for i in st(pg)['items'] if i['id']=='a'])
    pg.click('[data-a=todayno]');print('today hidden',pg.inner_text('#app').count('Heute noch'))
    # loc banner for Metzgerei
    print('loc banner',pg.inner_text('#app').count('Metzgerei Müller»?'))
    pg.click('.ban [data-a=locsave]');pg.wait_for_timeout(500);print('mine',[m['name'] for m in st(pg)['mine']])
    # shop start+end -> remNext banner
    pg.click('[data-a=shopstart]');pg.wait_for_timeout(100);pg.click('[data-a=shopend]');pg.wait_for_timeout(200)
    print('remnext banner',pg.locator('[data-a=remnextok]').count())
    pg.click('[data-a=remnextok]')
    # price on check
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.set.priceCheck=true;s.items.push({id:'m',name:'Milch',qty:1,unit:'lt'});localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload()
    pg.locator('.card[data-swk=i]',has_text='Milch').locator('[data-a=check]').click();print('price sheet',pg.locator('#prc').count())
    pg.fill('#prc','1,95');pg.click('[data-a=pricesave]');print('price stored',st(pg).get('prices'))
    pg.fill('#dn','Milch');pg.click('[data-a=add]');print('row shows price',pg.inner_text('#app').count('💰 1.95'))
    # edit price
    pg.locator('.card[data-swk=i]',has_text='Milch').locator('.nm').click();pg.fill('#ep','2.10');pg.click('[data-a=esave]')
    print('edited',st(pg)['prices']['milch'][0]['p'])
    b.close()
print(errs)
