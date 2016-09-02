from urllib2 import Request, urlopen, URLError, HTTPError 
import urllib   
import re    
import thread    
import time    

class Spider_Model:    
        
    def __init__(self):    
        self.page = 1    
        self.pages = []    
        self.enable = False    
    
 
    def GetPage(self,page):    
        myUrl = "http://www.qiushibaike.com/hot/page/" + page 
        print myUrl   
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        #headers = { 'User-Agent' : user_agent }   
        headers = {  
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        }  
        print '11111111111'
        req = urllib2.Request(myUrl, headers = headers)   
        
        print '2222222222222'
        myResponse = urllib2.urlopen(req)  
        print '33333333333'
        myPage = myResponse.read()    
        print '4444444444'
        unicodePage = myPage.decode("utf-8")    
        myItems = re.findall('<div.*class="content".*>(.*)</div>',unicodePage,re.S)    
        items = []    
        for item in myItems:    
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])    
        return items    
    
 
    def LoadPage(self):    
        while self.enable:      
            if len(self.pages) < 2:    
                try:    
                    myPage = self.GetPage(str(self.page))    
                    self.page += 1    
                    self.pages.append(myPage)    
                except:    
                    print 'cont connect qiushibaike !!!!!'

            else:    
                time.sleep(1)    
            
    def ShowPage(self,nowPage,page):    
        for items in nowPage:    
            print u'page%d' % page , items[0]  , items[1]    
            myInput = raw_input()    
            if myInput == "quit":    
                self.enable = False    
                break    
            
    def Start(self):    
        self.enable = True    
        page = self.page    
    
        print u'laoding!!!!!!'    
            
        thread.start_new_thread(self.LoadPage,())    
            
        while self.enable:    
            if self.pages:    
                nowPage = self.pages[0]    
                del self.pages[0]    
                self.ShowPage(nowPage,page)    
                page += 1    
    
    

    
print u'press enter'    
raw_input(' ')    
myModel = Spider_Model()    
myModel.Start()