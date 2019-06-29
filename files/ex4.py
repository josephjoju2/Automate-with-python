import os

total=0
for filename in os.listdir('..'):#list the subfiles as a list
    print(filename+': '+str(os.path.getsize(os.path.join('..',filename))))
    total=total+os.path.getsize(os.path.join('..',filename))

print('total bytes : '+str(total))



