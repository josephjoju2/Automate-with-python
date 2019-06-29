eggfile=open('egg.txt','w')
eggfile.write('hello world \n')
eggfile.close()


eggfile=open('egg.txt','a')
eggfile.write('im just kidding \n')
eggfile.close()



eggfile=open('egg.txt')
print(eggfile.read())

