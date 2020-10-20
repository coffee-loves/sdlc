from requests_html import HTMLSession
import  requests
from sys import  argv
from urllib.parse import urlparse,urljoin
#DEBUG = True

USAGE='''
USAGE:
python dead_link.py www.itest.info
'''
script_name,url = argv

# 判断命令行输入参数是否包含script_name和url
if len(argv)!=2:
    print(USAGE)
    exit(1) #退出命令行


if url[:4] != 'http':
     url = 'http://' + url #拼接

res = urlparse(url) #将url 解析为固定字段的内容

if res.netloc == '': #判断其中的netloc属性是否为空
    print('无法获取站点的domain信息')
    exit(1)

domain = res.netloc
# print(f"站点domain：{domain}")
print("站点domain:",domain)

session = HTMLSession()
r = session.get(url) #使用session抓取页面所有链接

links=r.html.find('img') #使用标签a定位链接



for link in links:
    if 'src' in link.attrs:#依次判断每个链接是内链还是外链
        src = link.attrs['src']
    else:
        continue
    result = urlparse(src)
    if result.netloc=='':
        src = urljoin(url,src)
        url_type = '内链'
    else:
        if domain in src:
            url_type = '内链'
        else:
            url_type = '外链'
    try:
        response = requests.get(src) #使用request判断链接状态码
        if response.status_code >= 400:
            print(f"{url_type}{src}失败")
        else:
            print(f"{url_type}{src}成功")
    except:
        print("出现异常")

