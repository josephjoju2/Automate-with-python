def spam(num):
    return 42/num
try:
    print(spam(3))
    print(spam(4))
    print(spam(0))
    print(spam(1))
except:
    print('error occured')
