import re
robregex=re.compile(r'robocop',re.I)#re.I will get everycase
find=robregex.findall('robocop Robocop the ROBOCOP')
print(find)
