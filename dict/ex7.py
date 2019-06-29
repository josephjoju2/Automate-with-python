import pprint
dragonLoot = ['gold coin', 'dagger','ruby', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
def addtoinventory(inventory,addeditems):
    for i in addeditems:
        if i in inventory:
           
            inventory[i]+=1
        else:
            
            inventory.setdefault(i,1)
    return inventory
pprint.pprint(addtoinventory(inv,dragonLoot))
