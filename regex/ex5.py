import re
greedyregex=re.compile(r'(ha){3,5}')
mo1=greedyregex.search('hahahahaha')
print(mo1.group())


nongreedyregex=re.compile(r'(ha){3,5}?')
mo2=nongreedyregex.search('hahahaha')
print(mo2.group())
