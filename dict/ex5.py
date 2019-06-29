allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}
def totalbrought(guest,item):
    total=0
    for l,m in guest.items():
        total+=m.get(item,0)
    return total
print(totalbrought(allGuests,'apples'))
     
