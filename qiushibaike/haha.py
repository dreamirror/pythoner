# -*- coding: utf-8 -*-  
import urllib    
import urllib2  
import cookielib  
  
cookie = cookielib.CookieJar()    
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))  
  
#需要POST的数据#  
postdata=urllib.urlencode({    
    'UserName':'212015081200003',    
    'UserPass':'cgc11191636'    
})  
  
#自定义一个请求#  
req = urllib2.Request(    
    url = 'http://xhu.aiyy.org/Action/verificationcode.ashx?action=publiclogin',    
    data = postdata  
)  
  
#访问该链接#  
result = opener.open(req)  
  
#打印返回的内容#

result2 = opener.open('http://xhu.aiyy.org/Manage/PStudent/payment.html?ver=399')  
  
#打印返回的内容#  
print result2.read() 
  
