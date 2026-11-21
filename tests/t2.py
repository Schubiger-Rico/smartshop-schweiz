from playwright.sync_api import sync_playwright
import os,json
store={}
def handler(route):
    r=route.request;k=r.url.split('/lists/')[1]
    if r.method=='PUT':store[k]=r.post_data;route.fulfill(status=200,body=r.post_data,content_type='application/json')
    else:route.fulfill(status=200,body=store.get(k,'null'),content_type='application/json')
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();ctxs=[b.new_context(viewport={'width':390,'height':700}) for _ in range(2)];pgs=[]
    for c in ctxs:
        c.route('https://fake-rtdb.firebasedatabase.app/**',handler);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)));pgs.append(pg)
        pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{fbUrl:'https://fake-rtdb.firebasedatabase.app'}}))");pg.reload()
    a,bb=pgs
    a.fill('#dn','Milch');a.click('[data-a=add]')
    a.click('#hamb');a.click('[data-a=nav][data-v=settings]');a.click('[data-a=sub][data-v=share]');a.click('[data-a=sharenew]');a.wait_for_timeout(1500)
    code=a.inner_text('.ban div[style*=font-size]');print('code',code)
    bb.click('#hamb');bb.click('[data-a=nav][data-v=settings]');bb.click('[data-a=sub][data-v=share]');bb.fill('#shc',code);bb.click('[data-a=sharejoin]');bb.wait_for_timeout(1500)
    bb.click('#hamb');bb.click('[data-a=nav][data-v=list]');print('B items',bb.locator('.card[data-swk=i]').count())
    bb.fill('#dn','Brot');bb.click('[data-a=add]');bb.wait_for_timeout(1500)
    a.click('#hamb');a.click('[data-a=nav][data-v=list]');a.wait_for_timeout(6000);print('A items',a.locator('.card[data-swk=i]').count())
    b.close()
print(errs)
