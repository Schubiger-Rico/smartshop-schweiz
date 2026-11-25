# Begrüssung: 3 s, Tageszeit, keine Wiederholung im Monat, Kurz/Aus
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.add_init_script("(function(){var D=Date,f=new D(2026,10,25,8,15);window.Date=function(a){return arguments.length?new (Function.prototype.bind.apply(D,[null].concat([].slice.call(arguments)))):new D(f.getTime()+(D.now()-window.__t0))};window.__t0=D.now();Date.now=function(){return f.getTime()+(D.now()-window.__t0)};Date.prototype=D.prototype;Date.UTC=D.UTC;Date.parse=D.parse})()")
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true,name:'Rico'},set:{newsSeen:'n16'}}))");pg.reload();pg.wait_for_timeout(300)
    g=pg.locator('#greet');print('shown',g.count(),pg.inner_text('#greet') if g.count() else '')
    pg.wait_for_timeout(4700);print("gone after 4s",pg.locator('#greet').count()==0)
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify(Object.assign(JSON.parse(localStorage.getItem('sebu.v1')),{set:Object.assign(JSON.parse(localStorage.getItem('sebu.v1')).set,{greet:'short'})})))");pg.reload();pg.wait_for_timeout(300)
    print('short',pg.inner_text('#greet'))
    pg.click('#greet');print('tap closes',pg.locator('#greet').count()==0)
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify(Object.assign(JSON.parse(localStorage.getItem('sebu.v1')),{set:Object.assign(JSON.parse(localStorage.getItem('sebu.v1')).set,{greet:'off'})})))");pg.reload();pg.wait_for_timeout(300)
    print('off',pg.locator('#greet').count()==0)
    pg.screenshot(path='/tmp/claude-0/shots/s28b.png')
    c.close();b.close()
s=open('index.html').read();import re
for k in 'mtan':
    m=re.search(k+r":\[('(?:[^'\\]|\\.)*'(?:,'(?:[^'\\]|\\.)*')*)\]",s[s.index('var GREET='):]);l=re.findall(r"'((?:[^'\\]|\\.)*)'",m.group(1));print(k,len(l),'unique',len(set(l))==31,'no ß',all('ß' not in x for x in l))
print(errs)
