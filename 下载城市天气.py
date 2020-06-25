# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:46:59 2020

@author: z
"""

import re
import urllib.request as r  


city=['beijing','nanjing','chengdu','wuhan','zhengzhou','tianjin','anshan','anshun'
      ,'dalian','shenzhen','baoji','bole','qingdao','changde','jinan','binzhou'
      ,'hefei','xianyang','chongqing','dazhou','anshan','anshun','wenzhou','bazhong'
      ,'zhengzhou','baotou','hanzhong','xiamen','shanghai','guizhou']

k=" "
for i in range(len(city)):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    name=str(url.format(city[i]))
    data=r.urlopen(name).read().decode('utf-8','ignore')
    
    temp=re.compile('"temp":"(.*?)",').findall(data)
    description=re.compile('"description":"(.*?)",').findall(data)

    k=k+city[i]+'温度为:'+str(temp)+'天气为:'+str(description)+'\n'
tq=open('城市天气.txt','w',encoding='utf-8')
tq.write(k)
tq.close()