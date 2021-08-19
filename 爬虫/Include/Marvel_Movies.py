# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
import requests
import time
import xlwt

web = 'https://movie.douban.com/tag/#/?sort=T&tags=%E6%BC%AB%E5%A8%81'

driver = webdriver.Chrome('G:/Anaconda3/Scripts/chromedriver_win32/chromedriver.exe')
driver.get(web)

while True:
    time.sleep(2)
    try:
        driver.find_element_by_link_text(u"加载更多").click()
    except:
        break

time.sleep(2)
content = driver.page_source

data = etree.HTML(content).xpath('//*[@id="app"]/div/div[1]/div[3]/a/@href')
title = etree.HTML(content).xpath('//*[@id="app"]/div/div[1]/div[3]/a/p/span[1]')
# end = etree.HTML(content).xpath('//*[@id="app"]/div/div[1]/div[4]/a[contains(text(),"当前筛选没有找到结果")]')

datalist = []
for element in range(len(title)):
    # print(type(data[element].attrib))
    # print(end[element].attrib)
    datalist.append(title[element].text)
    datalist.append(data[element])
    print(title[element].text + '\t' + str(data[element]))


savepath = "漫威电影.xls"
print("save.......")
book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet('漫威电影', cell_overwrite_ok=True)  # 创建工作表
col = ("影片中文名", "电影详情链接")

for i in range(0, 2):
    sheet.write(0, i, col[i])  # 列名
    for j in range(1, 600):
            datas = datalist[:j]
            if j % 2 == 1 and i == 0:
                sheet.write(j, i, datas[j-1:j])  # 数据
            if j % 2 == 0 and i == 1:
                sheet.write(j-1, i, datas[j-1:j])  # 数据
book.save(savepath)  # 保存
