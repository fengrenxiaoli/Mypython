import urllib
import urllib.request
data={}
data['word']='one peace'
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
a = urllib.request.urlopen(full_url)
data=a.read()
data=data.decode('UTF-8')
print(data)
##打印出网址：
a.geturl()