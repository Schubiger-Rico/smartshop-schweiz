from playwright.sync_api import sync_playwright
import os,json
errs=[]
def ov(route):
    q=route.request.post_data or ''
    body={'elements':[{'type':'node','lat':47.0005,'lon':8.0,'tags':{'shop':'doityourself','name':'Jumbo'}},{'type':'node','lat':47.0,'lon':8.0,'tags':{'shop':'supermarket','name':'Coop Test','brand':'Coop'}}]}
    route.fulfill(status=200,body=json.dumps(body),content_type='application/json')
with sync_playwright() as p:
    b=p.chromium.launch();c=b.new_context(viewport={'width':390,'height':800},geolocation={'latitude':47.0,'longitude':8.0},permissions=['geolocation'])
    c.route('https://overpass-api.de/**',ov);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{gps:'ask',radius:100}}))");pg.reload()
    pg.fill('#dn','Schrauben');print('chip',pg.locator('[data-a=typesug]').count());pg.click('[data-a=typesug]')
    pg.click('[data-a=add]');print('switcher',pg.locator('[data-a=ltab]').count())
    pg.fill('#dn','Milch');pg.click('[data-a=shopsel][data-id=draft]');pg.click('[data-a=shtog][data-v=Lidl]');pg.click('[data-a=shok]');pg.click('[data-a=add]')
    print('food cards',pg.locator('.card[data-swk=i]').count(),pg.inner_text('#app').count('🏪 Lidl'))
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=gps]');pg.click('[data-a=gpsnow]');pg.wait_for_timeout(1500)
    pg.click('#hamb');pg.click('[data-a=nav][data-v=list]');pg.wait_for_timeout(300)
    print('typban',pg.locator('[data-a=typego]').count(),'pend',pg.locator('[data-a=yes]').count())
    pg.click('[data-a=yes]');pg.wait_for_timeout(200);print('after yes: food',pg.locator('.card[data-swk=i]').count(),'other',pg.locator('[data-a=other]').count())
    pg.click('[data-a=typego]');print('more cards',pg.locator('.card[data-swk=i]').count());pg.screenshot(path='s7.png')
    pg.click('[data-a=typeno]') if pg.locator('[data-a=typeno]').count() else None
    print('typban after dismiss',pg.locator('[data-a=typego]').count())
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=types]');pg.fill('#tn','Zoo');pg.click('[data-a=typeadd]');print('types ok',pg.locator('[data-typ]').count())
    b.close()
print(errs)
