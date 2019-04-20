from urllib import request
import re
def work (num):
	headers={'User_Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
	response = request.Request("http://acm.hdu.edu.cn/showproblem.php?pid={}".format(num),headers=headers)
	response = request.urlopen(response)
	html = response.read()
	html = html.decode("gb2312")
	title=re.findall(r"<h1 style='color:#1A5CC8'>(.*?)</h1>",html)
	ltitle=re.findall(r"<div class=panel_title align=left>(.*?)</div>",html)
	test=re.findall(r"<div class=panel_content>([\d\D]*?)</div>",html)
	d={}
	for i,d[ltitle[i]] in enumerate(test):
		pass
	return (title[0],d)
if __name__=='__main__':
	print (work(input()))
