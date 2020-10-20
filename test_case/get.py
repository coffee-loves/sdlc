import requests
from sys import argv

script,url = argv

USAGE='''
USAGE:
python dead_link.py www.itest.info
'''
if len(argv)!=2:
    print(USAGE)
    exit()

r = requests.get(url)

print("接口地址",url,'\n')
print("状态码",r.status_code,'\n')
print(f"Headers:")
for key, value in r.headers.items():
  print(f"{key} : {value}")


print(r.text)

