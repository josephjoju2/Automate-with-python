import shelve
shelffile=shelve.open('mydata')
cats=['gundu','manikutty','kingini','peekiri']
shelffile['cats']=cats
shelffile.close()


