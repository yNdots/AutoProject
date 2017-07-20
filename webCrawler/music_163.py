#coding:utf-8
import os

import requests
from bs4 import BeautifulSoup

from basic.initial import Base


class AlbumCover():
    '''抓取云音乐中beatles所有专辑的封面照片'''
    def __init__(self,driver=None,url=None):
        self.url = url
        self.pic_folder = 'music/beatles/'
        self.driver = driver

    def request(self):
        r = requests.get(self.url)
        return r

    def save_img(self,url,file_name):
        '''文件名中不能包含\/:*?''<>|等非法字符'''
        inlegal_ch = ['\\','/',':','*','?',''',''','<','>','|']
        for c in inlegal_ch:
            # print c
            file_name = file_name.replace(c,'')

        img = requests.get(url)
        with open(file_name,'ab') as f:
            f.write(img.content)
            # print 'save img'

    def mkdir_rec(self,path):
        '''创建文件夹，创建之前判断文件夹是否存在'''
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            return

    def spider(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame("g_iframe")
        html = self.driver.page_source
        # print html

        #重复创建文件夹会出错
        # os.makedirs(self.pic_folder)#递归创建文件夹
        self.mkdir_rec(self.pic_folder)
        os.chdir(self.pic_folder)

        all_pic = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        # print all_pic,type(all_pic)#<class 'bs4.element.ResultSet'>
        for p in all_pic:
            # print p,type(p)#<class 'bs4.element.Tag'>
            album_img = p.find('img')['src']

            album_name = p.find('p',class_='dec')['title']
            album_date = p.find('span',class_='s-fc3').get_text()

            photo_name = album_date+'-'+album_name+'.jpg'
            album_img_url = album_img[:album_img.index('?')]

            # print (album_img_url,photo_name)
            ##遍历图片信息列表，并保存到本地
            self.save_img(album_img_url,photo_name)



if __name__ == '__main__':
    url = "http://music.163.com/#/artist/album?id=101988&limit=120&offset=0"
    b = Base(browser_name='phantomjs')
    a = AlbumCover(driver=b.browser,url=url)
    a.spider()
    # a.save_img('http://p4.music.126.net/eBtwfEuCMV-b_CwNDEKjrw==/5504155208736808.jpg?param=120y120 ','1.jpg')