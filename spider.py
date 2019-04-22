from urllib import request
import re
class HDU:
        def __init__ (self,num=1001,headers={'User_Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}):
                self.num=num
                self.headers=headers
if __name__=='__main__':
	problem=HDU(input())
	print (problem.html())
