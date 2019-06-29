import re
heroregex=re.compile(r'batman|tina fey')
mo1=heroregex.search('we see in the batmobile, batman and tina fey')
print(mo1.group())

mo2=heroregex.search('we see in the batmobile, tina fey and batman')

print(mo2.group())

regex=re.compile(r'bat(man|mobile|girl)')
mo3=regex.search('we see in the batmobile, batman and tina fey')
print(mo3.group())
print(mo3.group(1))




