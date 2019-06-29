import re
phoneregex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1=phoneregex.search('my number is 333-4444')
print(mo1.group())
mo2=phoneregex.search('mynumber is 212-122-3323')
print(mo2.group())
