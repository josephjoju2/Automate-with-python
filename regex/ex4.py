import re
batregex=re.compile(r'bat(wo)*man')#zero or more using *
mo=batregex.search('there is a batman')
print(mo.group())
mo1=batregex.search('batwowoman')
print(mo1.group())


bregex=re.compile(r'bat(wo)+man')#one or more using +
mo2=bregex.search('batman and batwoman')
print(mo2.group())
