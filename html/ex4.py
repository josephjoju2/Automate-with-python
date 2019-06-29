import requests, sys, webbrowser
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playfile=open('romeoandjuliet.txt','wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)
playfile.close()
