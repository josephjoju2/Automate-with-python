import re
regex=re.compile(r'\d+\s\w+')
find=regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids')
print(find)


notvowelregex=re.compile(r'[^aeiouAEIOU]')
vowelregex=re.compile(r'[aeiouAEIOU]')
vow=vowelregex.findall('Robocop eats baby food. BABY FOOD.')
print(vow)
notvow=notvowelregex.findall('Robocop eats baby food. BABY FOOD.')
print(notvow)
