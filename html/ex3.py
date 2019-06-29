#! /usr/bin/python3
import sys, webbrowser, requests, bs4
print('googling')
res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1: ]))
res.raise_for_status
soup=bs4.BeautifulSoup(res.text)
elems=soup.select('.r a')
numopen=min(5,len(elems))
for i in range(numopen):
    webbrowser.open('http://google.com'+elems[i].get('href'))

