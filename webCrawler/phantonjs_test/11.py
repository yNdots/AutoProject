#coding=utf-8
from selenium import webdriver
import time
import os
br=webdriver.PhantomJS('phantomjs')
baseurl="http://quote.eastmoney.com/"
indexurl="stocklist.html"
gourl="%s%s"%(baseurl,indexurl)
br.get(gourl)
print br.title
time.sleep(5)
br.quit()
