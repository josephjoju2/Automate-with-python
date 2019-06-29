spam={'colour':'red','age':42}
for i in spam.values():
    print(i)    
for v in spam.keys():
    print(v)
for k in spam.items():
    print(k)
for l,m in spam.items():
    print('the key is '+str(l)+' the value is '+str(m)) 
