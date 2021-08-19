# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml

findLink = re.compile(r'<a href="(.*?)">')
findtitle = re.compile(r'<span class="title">(.*?)</span>')

head = {
    # 'Cookie': 'll="118287"; bid=DL9P4md1nf4; __utmc=30149280; ap_v=0,6.0; dbcl2="244231295:JxHymP+Krk0"; '
    # 'ck=zthK; push_doumail_num=0; __utmv=30149280.24423; '
    # '_pk_ref.100001.2939=%5B%22%22%2C%22%22%2C1628749775%2C%22https%3A%2F%2Fmovie.douban.com%2Ftag%2F%22%5D;'
    # ' _pk_ses.100001.2939=*; __gads=ID=8fddfd55ccd1cc1d:T=1628744537:S=ALNI_Mbssiu7VSMINHsaDUfPR1mxFV8yOw; '
    # '__utma=30149280.276926313.1628744501.1628749775.1628749967.4; '
    # '__utmz=30149280.1628749967.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; '
    # '_pk_id.100001.2939=026746b57ccf7464.1628745124.2.1628751432.1628745124.; '
    # '__utmt=1; __utmb=30149280.10.10.1628749967',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'}
web = 'https://movie.douban.com/top250?start='

text = ''
for i in range(0, 10):
    website = web+str(i*15)
    # resp = webdriver.Chrome('G:/Anaconda3/Scripts/chromedriver_win32/chromedriver.exe')
    # resp.get(website)
    # print(resp.page_source)
    resp = requests.get(website, headers=head)
    # print(resp)  # 打印请求结果的状态码
    # print(resp.content.decode())  # 打印请求到的网页源码
    bsobj = BeautifulSoup(resp.content, 'lxml')
    for a_list in bsobj.find_all('div', class_="item"):
        a_list = str(a_list)
        Link = re.findall(findLink, a_list)
        Title = re.findall(findtitle, a_list)
        if Link:
            print(Title[0] + '\t' + Link[0])
            # text += Title[0] + '\t' + Link[0]+'\n'
        # print(a_list.get('href'))

# with open('DoubanTop250.txt', 'w') as f:
#     f.write(text)
