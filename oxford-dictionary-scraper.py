import requests
from bs4 import BeautifulSoup
x=input("Search a term : ")
x=x.replace("What do you mean by","")
x=x.replace("Define","")
x=x.replace("?","")
x=x.replace(".","")
x=x.strip()
x=x.lower()
r = requests.get("http://www.oxforddictionaries.com/definition/english/"+x)
html=r.content
bsObj = BeautifulSoup(html,"html.parser")
bsObj = bsObj.select('div.senseInnerWrapper span.definition')
for link in bsObj:
    m=link.get_text()
    m=m[:-1]
    print(m+'.')
    break
