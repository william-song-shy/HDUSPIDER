from urllib import request
import re
import html
class HDUError (Exception):
	pass
class Content ():
        def __init__(self,data):
                self.title=data[0]
                self.content=data[1]
                self.subtitle=list (self.content.keys())
        def __str__ (self):
                return str((self.title,self.content))
        def get (self,method=None):
                if method==None:
                        return str((self.title,self.content))
                if not callable (method):
                        raise HDUError ("Method is not callable")
                else:
                        return method(self.title,self.content)
        def markup (self):
                return html.unescape(str((self.title,self.content)))
class HDU:
        def __init__ (self,num=1001):
                self.num=num
        def work (self,headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}):
                response = request.Request("http://acm.hdu.edu.cn/showproblem.php?pid={}".format(self.num),headers=headers)
                response = request.urlopen(response)
                if response.status==404:
                        raise HDUError ('Not found error of {}'.format(self.num))
                html = response.read()
                html = html.decode("gb18030")
                if  not re.findall('No such problem - ',html)==[]:
                        raise HDUError ('Not found error of {}'.format(self.num))
                title=re.findall(r"<h1 style='color:#1A5CC8'>(.*?)</h1>",html)
                ltitle=re.findall(r"<div class=panel_title align=left>(.*?)</div>",html)
                test=re.findall(r"<div class=panel_content>([\d\D]*?)</div>",html)
                d={}
                for i,d[ltitle[i]] in enumerate(test):
                        pass
                return Content ((title[0],d))
if __name__=='__main__':
	problem=HDU(input())
	print (problem.work())
