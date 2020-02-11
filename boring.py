import requests
import re

def pagelink(url):
    base_url = 'https://www.dygod.net/html/gndy/dyzz/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req = requests.get(url , headers = headers)
    req.encoding = 'gbk'#指定编码，否则会乱码
    pat = re.compile('<b>(.*?)<a href="/html/gndy/dyzz/(\d+.*?)" class="ulink" title=(.*?)/a>',re.S)#获取电影列表网址
    reslist = re.findall(pat,req.text)
    finalurl = []
    for i in range(0,25):
        xurl = reslist[i][1]
        finalurl.append(base_url + xurl)
    print(finalurl)
    return finalurl #返回该页面内所有的视频网页地址

#getdownurl获取页面的视频地址
def getdownurl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    req = requests.get(url , headers = headers)
    req.encoding = 'gbk'#指定编码，否则会乱码
    pat = re.compile('<a href="magnet(.*?)"',re.S)#获取下载地址
    reslist = re.findall(pat, req.text)
    furl = 'magnet'+reslist[0]
    print(furl)
    return furl


def getlist():
    filmlist = []
    downloadurllist = []
    html = "https://www.dygod.net/html/gndy/dyzz/index.html"
    print('你即将爬取的网站是：https://www.dygod.net/html/gndy/dyzz/index.html')
    p1 = pagelink(html)
    for p1i in p1[0:10] :
        p2 = getdownurl(p1i)
        if len(p2) == 0 :
            pass
        else :
            finalurl = p2
            pat = re.compile('\[电影天堂www.dytt89.com\](.*?)$', re.S)  # 获取下载地址
            reslist = re.findall(pat,finalurl)
            downloadurllist.append(finalurl)
            filmlist.append(reslist[0])
    return filmlist,downloadurllist

getlist()