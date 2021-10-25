import requests
import re
res = requests.get('https://free-proxy-list.net/')
# print(res.text)
# #
m = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)
# m = ["193.149.225.128:80","209.141.56.127:80"]

validips = []
for ip in m:
    try:
        res = requests.get('https://api.ipify.org?format=json',proxies = {'http':ip, 'https':ip}, timeout = 5)
        validips.append({'ip':ip})
        print(res.json())
    except:
        print('FAIL', ip )


print(len(validips))