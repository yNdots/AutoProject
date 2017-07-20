#coding:utf-8
import re

import requests
from bs4 import BeautifulSoup


def func():
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>and they lived at the bottom of a well.
    </p>
    <m><!--Hey, buddy. Want to buy a used parser?--></m>"
    <p class="story">...</p>
    """
    soup = BeautifulSoup(html_doc, 'lxml')
    # find = soup.find('p')#tag
    # print type(find)
    # print find
    # print find['class']
    # print find.string#navigable string

    # c = soup.find('m').string
    # print type(c)
    h = soup.b
    link = soup.find('a')

    # for s in link.next_siblings:#兄弟节点
    #     print repr(s)
    #
    # # print link
    # for parent in link.parents:
    #     if parent is None:
    #         print parent
    #     else:
    #         print parent.name

    # print soup.find_all(name='a')
    # print soup.find_all(string=re.compile('sisters'))
    url = 'https://www.cnblogs.com/'
    r = requests.get(url)
    # print r.text
    index_blog = BeautifulSoup(r.text, 'lxml')
    title_list = index_blog.find_all(name='a',attrs='titlelnk')

    with open('page_1.txt','w') as f:
        for title in title_list:
            print title.string,type(title.string)
            f.write(title.string.encode('utf-8')+'\n')


if __name__ == '__main__':
    func()

