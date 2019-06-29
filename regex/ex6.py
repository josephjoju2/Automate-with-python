import re
phoneregex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
listofnumbers=phoneregex.findall('my numbers are 232-232-3241 and also 231-313-2345')
print(listofnumbers)


groupregex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
tupleofnumbers=groupregex.findall('my numbers are 222-321-2345 and 321-123-3232')#returns with a list of tuples 
print(tupleofnumbers)
