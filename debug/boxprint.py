def box(sym,height,width):
    if len(sym)!=1:
        raise Exception('symbol should have only one chara')
    if height<=2:
        raise Exception('height should be more than 2')
    if width<=2:
        raise Exception('width should be greater than 2')
    print(sym*width)
    for i in range(height-2):
        print(sym+(' '*(width-2))+sym)
    print(sym*width)

for sym,h,w in(('#',3,6),('*',5,8),('gg',2,7)):
    try:
        box(sym,h,w)
    except Exception as error:
        print('an exception happened:'+str(error))
        
