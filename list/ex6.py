import copy
spam=[1,2,3,4]
cheese=spam
print(cheese)
cheese[1]='cat'
print(spam)



spams=[4,5,6,7]
cake=copy.copy(spams)
cake[2]='dog'
print(cake)
print(spams)
#for lists inside list use copy.deepcopy()
