import pprint
spam={'name':'pooka','age':5}
spam.setdefault('colour','black')
print(spam)
string='i am a happy programmer'
count={}
for i in string:
    count.setdefault(i,0)
    count[i]+=1
pprint.pprint(count)
#setdefault only works if there is no key persent    
