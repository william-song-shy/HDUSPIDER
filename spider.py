from urllib import request
import re
num=input("题目编号：")
response = request.urlopen("http://acm.hdu.edu.cn/showproblem.php?pid={}".format(num))
html = response.read()
html = html.decode("gb2312")
title=re.findall(r"<h1 style='color:#1A5CC8'>(.*?)</h1>",html)
ltitle=re.findall(r"<div class=panel_title align=left>(.*?)</div>",html)
test=re.findall(r"<div class=panel_content>([\d\D]*?)</div>",html)
d={}
for i,d[ltitle[i]] in enumerate(test):
	pass
print (title,d)
