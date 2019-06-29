def spam(num):
    try:
        return 42/num
    except ZeroDivisionError:
        print('error occured')
print(spam(3))
print(spam(4))
print(spam(0))
print(spam(1))
