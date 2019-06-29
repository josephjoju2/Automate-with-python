#!/usr/bin/python3
import sys, webbrowser, pyperclip
if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
else:
    address=' '.join(pyperclip.paste())
webbrowser.open('https://www.google.com/maps/place/'+address)


