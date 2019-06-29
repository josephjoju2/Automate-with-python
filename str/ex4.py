import pyperclip
text=pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)-1):    # loop through all indexes in the "lines" 
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print(pyperclip.paste())

