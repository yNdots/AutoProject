#coding:utf-8
from selenium import webdriver


class Base(object):
    """
    @version 13.3.2016
    @author voilet
    浏览器对象webdriver初始化
    """
    def __init__(self,browser_name='chrome', url=None):

        self.browser = self._browser_init(browser_name)
        if url == None:
            self._page_site_init('https://www.cnblogs.com/')
        else:
            self._page_site_init(url)

    def _browser_init(self,browser_name):
        """
        :param browser_name:
        :param url:
        :return:
        """
        # browser=""
        if browser_name=="firefox":
             browser = webdriver.Firefox()

        elif browser_name=="chrome":
            browser = webdriver.Chrome()
        elif browser_name == 'phantomjs':
            browser = webdriver.PhantomJS()
        else:
            browser_name=="ie" or browser_name=="internetexplorer"
            browser = webdriver.Ie()
        return browser

    def _page_site_init(self, url):
        self.browser.get(url)
        self.browser.maximize_window()


if __name__ == '__main__':
    b = Base('chrome')
    b._page_site_init('https://www.cnblogs.com/')