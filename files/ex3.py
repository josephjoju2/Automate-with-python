import os
path=os.getcwd()
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.getsize(path))
print(os.listdir('..'))
