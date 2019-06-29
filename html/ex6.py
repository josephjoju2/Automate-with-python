import bs4
examplefile=open('example.html')
beautifulsoup=bs4.BeautifulSoup(examplefile)
pelems=beautifulsoup.select('p')
print(type(pelems))
for i in range(len(pelems)):
    print(pelems[i].get('class'))
