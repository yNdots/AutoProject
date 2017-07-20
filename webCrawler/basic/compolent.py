#coding:utf-8

class ExtTree(object):
    """
    @version 13.2.2016
    """
    def tree_traverse(self,browsr,path_arr):
        """
        根据tuple数组遍历ext树
        :param path_arr:
        :return:
        """
        #path_arr=['My Documents','Photos','Friend','violet']
        # browser=webdriver.Chrome()
        # browser.get("file:///C:/Users/violet/Desktop/easyUI/demo/tree/basic.html")
        for index,node in enumerate(path_arr):
            node_xpath="//span[text()='"+node+"']"
            print "current_path:[%d,%s]"%(index,node)#遍历路径元组
            expand_xpath=node_xpath+"/parent::div//span["+str(index+1)+"]"
            print "expadn_node:",expand_xpath
            browsr.find_element_by_xpath(expand_xpath).click()

