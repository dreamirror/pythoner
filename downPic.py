import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(r'(<img src=)(.*?) alt=.*?')
    #pattern = re.compile(r'(<div class=\"content\">)(.*?<span>)(.*?)(</span>.*?</div>)',re.S)
    items = re.findall(pattern, content)
    for item in items:
        item = item[1][1:-1]
        url = 'http:'+ item
        name = item.split('/')[-1]
        print(url)
        u = urllib.urlopen(url)
        data = u.read()
        f = open(u'pic\\'+ name, 'wb')
        f.write(data)
        f.close()
        print '\n'

    #print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason