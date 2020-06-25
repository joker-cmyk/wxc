# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:51:42 2020

@author: z
"""

"""import request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for i  in range(1,2):
    url = 'http://www.qiushibaike.com/8hr/page'+str(i)
    pagedata = urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat = '<div class="concent">.*?<span>(.*?)</span>.*?</div>'
    datalist = re.compile(pat,re.S).findall(pagedata)
    for j in range(0,len(datalist)):
        print("第"+str(i)+"页第"+str(j)+"个")
        print(datalist[j])"""
import re
import urllib.request
import urllib.error
import threading
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,36,2):
              url = 'http://www.qiushibaike.com/hot/page/'+str(i)+"/"
              urllib.request.urlopen(url).read().decode("utf-8","ignore")
              pagedata = urllib.request.urlopen(url).read().decode("utf-8","ignore")
              pat = '<div.*?class=\"content\">(.*?)</div>'
              datalist = re.compile(pat,re.S).findall(pagedata)
              for j in range(0,len(datalist)):
                  print("第"+str(i)+"页第"+str(j)+"个")
                  print(datalist[j])
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,36,2):
              url = 'http://www.qiushibaike.com/hot/page/'+str(i)+"/"
              urllib.request.urlopen(url).read().decode("utf-8","ignore")
              pagedata = urllib.request.urlopen(url).read().decode("utf-8","ignore")
              pat = '<div.*?class=\"content\">(.*?)</div>'
              datalist = re.compile(pat,re.S).findall(pagedata)
              for j in range(0,len(datalist)):
                  print("第"+str(i)+"页第"+str(j)+"个")
                  print(datalist[j])
t1 = A()
t1.start()
t2 = B()
t2.start()
            
        