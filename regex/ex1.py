import re
phoneregex=re.compile(r'(\(\d{3}\)) (\d\d\d-\d\d\d\d)')
mo = phoneregex.search('my phone number is (123) 345-4565 budds')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
areacode, mainno=mo.groups()
print('area code: '+areacode)
print('main number: '+mainno)
