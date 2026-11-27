from playwright.sync_api import sync_playwright
import os,json
errs=[]
st={'ob':{'done':True},'items':[{'id':'a','name':'Milch','stores':['Migros'],'cat':'x'},{'id':'b','name':'Eier','stores':['Hofladen'],'cat':'x'}],
 'mine':[{'name':'Hofladen','lat':47.1,'lon':8.1,'r':25,'hint':'geradeaus'}]}
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("s=>localStorage.setItem('sebu.v1',JSON.stringify(s))",st);pg.reload()
    pg.click('#shopbtn');print('shop',pg.locator('[data-a=shopend]').count())
    pg.click('[data-a=shopend]')
    print('banner',pg.locator('[data-a=remind]').count(),pg.locator('[data-a=todayall]').count(),pg.locator('[data-a=endno]').count(),'nav',pg.locator('.navb').count())
    print(pg.locator('.navb').first.get_attribute('href') if pg.locator('.navb').count() else None)
    pg.click('[data-a=todayall]');print('today set',pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1')).items.filter(i=>i.today).length"))
    pg.evaluate("s=>localStorage.setItem('sebu.v1',JSON.stringify(s))",st);pg.reload()
    pg.click('#shopbtn');pg.click('[data-a=shopend]');pg.click('[data-a=enddone]')
    s2=pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))");print('erledigt: left',[i['name'] for i in s2['items']],'banner gone',pg.locator('[data-a=enddone]').count()==0)
    b.close()
print(errs)
