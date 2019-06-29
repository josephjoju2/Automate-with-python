import re
namesregex=re.compile(r'Agent \w+')
k=namesregex.sub('CENSORED','Agent colson killed nobody')#first argument is substituted to the second
print(k)
