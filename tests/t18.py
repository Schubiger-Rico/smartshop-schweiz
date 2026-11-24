# Spracheingabe: Mengen vor/nach dem Produkt, Füllwörter, Korrektur
from playwright.sync_api import sync_playwright
import os
errs=[]
MOCK="""window.webkitSpeechRecognition=function(){var me=this;this.start=function(){setTimeout(function(){me.onresult({results:[[{transcript:window.__tx}]]});me.onend&&me.onend()},30)};this.abort=function(){}};window.SpeechRecognition=window.webkitSpeechRecognition;"""
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
cases=['Brot 1 Stück und Mehl 1 Kilo stopp und Käse','Brot und 1Stk und 1kg stopp','Mehl ein Kilo und Milch 2 Liter','zwei Kilo Äpfel, Butter bitte','Eier 6 fertig']
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)));pg.add_init_script(MOCK)
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    for c in cases:
        pg.evaluate("window.__tx=%r"%c);pg.click('[data-a=voice]');pg.wait_for_timeout(200)
        rows=[[pg.locator('.sheet [data-vi="%d"][data-f=%s]'%(i,f)).input_value() for f in 'nqu'] for i in range(pg.locator('.sheet [data-f=n]').count())]
        print(c,'→',rows);pg.click('[data-a=shclose]',position={'x':5,'y':5}) if False else pg.evaluate("document.querySelector('.sheet [data-a=shclose]')&&document.querySelector('.sheet [data-a=shclose]').click()")
        if pg.locator('.sheet').count():pg.mouse.click(5,5)
    pg.evaluate("window.__tx='Brot und Käse'");pg.click('[data-a=voice]');pg.wait_for_timeout(200)
    pg.fill('.sheet [data-vi="1"][data-f=n]','Bergkäse');pg.fill('.sheet [data-vi="1"][data-f=q]','2');pg.click('[data-a=vdel][data-v="0"]')
    pg.click('[data-a=voiceadd]');print('added',[(i['name'],i['qty'],i['unit']) for i in st(pg)['items']])
    b.close()
print(errs)
