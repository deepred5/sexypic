from bs4 import BeautifulSoup
import requests
import threading
import re
import os
import time

# http://www.ninihen.com/

# 偷拍自拍
# http://www.ninihen.com/art/9.html
# http://www.ninihen.com/art/9-131.html


url_all = []
url_all_1 = []
img_src = []
name_begin = time.strftime("%Y-%m-%d-", time.localtime())





dif_url = ['http://www.ninihen.com/art/9-', 'http://www.ninihen.com/art/10-',
           'http://www.ninihen.com/art/11-', 'http://www.ninihen.com/art/12-',
           'http://www.ninihen.com/art/13-', 'http://www.ninihen.com/art/14-',
           'http://www.ninihen.com/art/15-', 'http://www.ninihen.com/art/16-']

pattern1 = 'div.k_list-1a > div.k_list-txt > ul > li > a'
pattern2 = 'div.content-img > p > img[src]'

# url1 = 'http://www.27270.com/ent/meinvtupian/list_11_1.html'
# url2 = 'http://www.27270.com/ent/meinvtupian/list_11_83.html'
# div#imgList > ul > li > a > img
# body > div.w960.yh > div.NewPages > ul > li:nth-child(13) > a
# body > div.warp > div.imgPage > ul > li:nth-child(13) > a
# body > div.warp > div.imgPage > ul > li:nth-child(13) > a
# div.k_list-1a > div.k_list-txt > ul > li > a
# div.content-img > p > img



def saveImage( imgUrl,imgName ="default.jpg" ):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    DstDir= path
    print("保存文件"+DstDir+imgName+"\n")
    try:
        with open(DstDir+imgName ,"wb") as jpg:
            jpg.write(image)
            return
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close




def collect_url(page, url, num):
    url_all.append('http://www.ninihen.com/art/' + str(num+9) + '.html')
    for i in range(2, page+1):
        url_all.append(url + str(i) + '.html')


def collect_url_1(pattern):
    for url in url_all:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        url_1 = soup.select(pattern)
        # time.sleep(1)

        for src in url_1:
            href = src.get('href')
            url_all_1.append(href[href.rfind('/')+1:href.find('.html')])

def collect_img(pattern):
    for url in url_all_1:
        wb_data = requests.get('http://www.ninihen.com/arthtml/' + url + '.html')
        soup = BeautifulSoup(wb_data.text, 'lxml')
        images = soup.select(pattern)
        # time.sleep(1)

        for src in images:
            img_src.append(src.get('src'))



def download_img(name):
    index = 1
    for src in img_src:
        saveImage(src, str(name) + str(index) + '.jpg')
        index += 1


def begin(num):
    collect_url(page, dif_url[num], num)
    collect_url_1(pattern1)
    collect_img(pattern2)
    download_img(name_begin)


choice = input('请选择要下载图片的编号\n 偷拍自拍-0\n 亚洲色图-1\n 欧美色图-2\n 清纯唯美-3\n 动漫图片-4\n 熟女少妇-5\n '
               '美腿丝袜-6\n 成人套图-7\n')
name_begin = name_begin + str(choice) + '-'
page = int(input('请输入要爬取的页数(比如：2)\n'))
disk = input('请输入要保存到的磁盘名(比如: d ) :')
file = input('请输入文件夹名(比如: mm ) :')
path = disk + ':/' + file + '/'


if os.path.isdir(path):
    print('已经存在该文件夹')
else:
    os.makedirs(path)

print('请耐心等待...')

begin(int(choice))

print('下载完成!')

decide = input('输入0结束程序: ')

if (int(decide) == 0):
    exit()


























