import shelve
shelfile=shelve.open('mydata')
print(shelfile['cats'])

print(list(shelfile.keys()))


print(list(shelfile.values()))

shelfile.close()
