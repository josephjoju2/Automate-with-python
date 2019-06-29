birthday={'Joju':'dec 16','Bini':'june 24'}
while True:
    print('enter name to find bday (blank to quit)')
    name=input()
    if name=='':
        break
    if name in birthday:
        print('the bday of '+name+' is on '+birthday[name])        
    else:
        print('the bday of '+name+' is not present')
        print('enter the bday')
        birthday[name]=input()
        print(birthday) 
