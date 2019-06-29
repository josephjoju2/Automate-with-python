import requests
res=requests.get('http://inventwithpython.com/page_not_exist')
try:
    res.raise_for_status()
except Exception as err:
    print('error occured : %s'%(err))
