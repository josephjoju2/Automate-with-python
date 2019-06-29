import os
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('/home/linux/pramod/str/ex2.py','.'))
print(os.getcwd())
