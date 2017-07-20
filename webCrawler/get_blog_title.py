#!/usr/bin/python2
#coding:utf-8

import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from basic.initial import Base
'''获取博客推荐博客的标题'''


class IndexPage(object):
    def __init__(self,driver):
        #初始化浏览器，默认为chrome,
        # super(IndexPage,self).__init__(url)
        self.driver = driver
        #self.drier.find_element(By.XPATH,"//div[@id='nav_menu']//a[text()='新闻']").click()

    def get_recommend_blog_title(self,page):

        url = 'https://www.cnblogs.com/'
        if page > 1:
            url = url +'#p'+str(page)
        #这个url加页码数，好像不可以
        r = requests.get(url)
        # print r.text
        index_blog = BeautifulSoup(r.text, 'lxml')
        title_list = index_blog.find_all(name='a',attrs='titlelnk')

        with open('page_1.txt','w+') as f:
            for title in title_list:
                print title.string
                f.write(title.string.encode('utf-8')+'\n')

    def get_all_title(self, page=5):
        '''page:需要获取标题的页面的总页数'''
        total_page_xpath = (By.XPATH,"//a[text()='Next >']/preceding-sibling::a[1]")

        total_page = self.driver.find_element(*total_page_xpath).text
        # print total_page
        for p in range(1, page+1):

            self.get_title_by_post(page=p)
            if p > 1:
                #页面跳转
                self.driver.find_element_by_xpath("//div[@id='paging_block']//a[text()='"+str(p)+"']").click()
            time.sleep(3)

    def get_title_by_post(self, page):
        url = 'https://www.cnblogs.com/'
        data = {"CategoryType":"SiteHome","ParentCategoryId":0,"CategoryId":808,
                "PageIndex":page,
                "TotalPostCount":4000,"ItemListActionName":"PostList"}
        r = requests.post(url,data)

        index_blog = BeautifulSoup(r.text, 'lxml')
        title_list = index_blog.find_all(name='a',attrs='titlelnk')

        with open('page_1.txt','a+') as f:
            for title in title_list:
                print title.string
                f.write(title.string.encode('utf-8')+'\n')

if __name__ == '__main__':
    # get_recommend_blog_title()
    url = 'https://www.cnblogs.com/'
    base = Base(url=url)
    index = IndexPage(base.browser)
    index.get_all_title()