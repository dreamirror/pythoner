#!usr/bin/python
import re  
import urllib  
import urllib2
def getHtml(url):  
    #page = urllib.urlopen(url)  
    #html = page.read()
    #print html
    #return html

        myUrl = url  
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        #headers = { 'User-Agent' : user_agent }   
        headers = {  
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        }  
  
        req = urllib2.Request(myUrl, headers = headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()
        return myPage

def getImg(html):  
    reg = r'src="(.+?\.jpg)"'  
    imgre = re.compile(reg)  
    imglist = imgre.findall(html)
    print imglist
    x = 0  
    for imgurl in imglist:
        print imgurl
        urllib2.urlretrieve(imgurl,'%s.jpg' % x)  
        x = x + 1          
     
html = getHtml("https://www.135cd.com/htm/pic2/55341.htm")  
getImg(html) 
