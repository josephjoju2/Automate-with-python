import bs4
examplefile=open('example.html')
examplesoup=bs4.BeautifulSoup(examplefile)
spanelem=examplesoup.select('span')[0]
print(spanelem)
print(spanelem.get('id'))
print(spanelem.attrs)
