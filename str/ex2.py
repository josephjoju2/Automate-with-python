picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def picnicbox(picnicitems,leftwidth,rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'-'))
    for k,v in picnicitems.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth,'.'))

picnicbox(picnicItems,20,12)     
