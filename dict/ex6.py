import pprint
stuff={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print('inventory: ')
total=0
inventory={}
for k,v in stuff.items():
    total+=v
    temp=k
    k=v
    v=temp
    inventory[k]=v
pprint.pprint(inventory)
print('total items: '+str(total))
