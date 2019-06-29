import re
nameregex=re.compile(r'Agent (\w)\w*')
l=nameregex.sub(r'\1*****','Agent gghjbg said to Agent boby')

print(l)
