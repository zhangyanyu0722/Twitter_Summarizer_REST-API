from requests import put, get, post, delete
import sys
keywords = sys.argv[1:]
URL = 'http://127.0.0.1:5000/twitter/'
for keyword in keywords:
    print('***************** Starting to download' + keyword + ' *****************')
    put(URL + keyword)
    get(URL + keyword)
print("***************** Succeed Download *****************")