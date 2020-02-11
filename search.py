from bs4 import BeautifulSoup
import requests
import  os
import warnings
import configparser
import boring

warnings.filterwarnings("ignore")

def search(filmname):
    filmlist=[]
    urllist=[]
    filmname1=filmname.encode('gb2312')
    data={'typeid':'1','keyword':filmname1}
    response = requests.get('http://s.ygdy8.com/plus/s0.php',params=data)
    response.encoding = "GBK"
    soup=BeautifulSoup(response.text)
    taglist=soup.find_all("div",class_="co_content8")
    for a in taglist:
        ultag=a.find_all("ul")
        for b in ultag:
            btag=b.find_all("b")
            for c in btag:
                realtag=c.find_all("a")
                for each in realtag:
                    name=each.get_text()
                    filmlist.append(name)
                    url=each["href"]
                    urllist.append(url)
    return filmlist,urllist

def select():
    skr = {}
    n=1
    while n<=len(selectlist[0]):
        skr[n]=selectlist[1][n-1]
        print(n,":",selectlist[0][n-1])
        n=n+1
    while True:
        switch=int(input("请输入影片编号："))
        if switch in skr.keys():
            halfurl=skr[switch]
            return halfurl
            break
        else:
            print("数值不存在")
            continue

def getrealurl():
    realurllist=[]
    response2=requests.get('http://www.ygdy8.com'+filmurl)
    response2.encoding = "GBK"
    soup2=BeautifulSoup(response2.text)
    atag=soup2.find_all("td",style="WORD-WRAP: break-word")
    for a in atag:
            hreftag=a.find_all("a")
            for each in hreftag:
                realurl=each['href']
                realurllist.append(realurl)
    return realurllist

def download():
    thunderurl='\" \"'.join(list)
    os.system("start {mypath} \"{myurl}\"".format(mypath=thunderpath,myurl=thunderurl))

def getthunderpath():
    conf = configparser.ConfigParser()
    conf.read("example.ini",encoding="utf-8-sig")
    str_val = conf.get("THUNDERPATH", "path")
    return str_val


while True:
    try:
        thunderpath=getthunderpath()
        filmname = input("请输入名称:")
        if filmname == "boring":
            selectlist = boring.getlist()
            filmurl = select()
            list = []
            list.append(filmurl)
            download()
            continue
        else:
            selectlist = search(filmname)
            if len(selectlist[0])>0:
                filmurl = select()
                list = getrealurl()
                print(list)
                download()
                continue

            else:
                print("影片不存在")
                continue
    except:
        continue

