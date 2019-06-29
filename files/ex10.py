import pprint
cats= [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileobj=open('catfile.py','w')
fileobj.write('cats ='+pprint.pformat(cats))
fileobj.close()
