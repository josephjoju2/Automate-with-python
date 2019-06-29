import re
atregex=re.compile(r'.at')
al=atregex.findall('The cat in the hat sat on the flat mat.')
print(al)


everyregex=re.compile(r'.*',re.DOTALL)#.*read everything except \n
p=everyregex.search('Serve the public trust.\nProtect the innocent.\nsss..')
p.group()
print(p)
