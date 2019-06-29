import bs4
examplefile=open('example.html')
examplesoup=bs4.BeautifulSoup(examplefile.read())
elems=examplesoup.select('#author')
type(elems[0])
