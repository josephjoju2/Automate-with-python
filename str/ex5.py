#! /usr/bin/python3
import sys,pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv)<2:
    print('you have to print the account')
    sys.exit()

acc=sys.argv[1]
if acc in PASSWORDS:
    password=PASSWORDS[acc]
    pyperclip.copy(password)
else:
    print('there is no such account present')


