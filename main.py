# -*- coding: utf-8 -*-
"""
Twitch Follower Count API
"""

print("hello world")
import requests as r
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time as t
import statsmodels.formula.api as sm

#required for Twitch API
header = {"Client-ID": "[REDACTED]"} #UPDATE HERE
#api url

#Follower info
user ="[twitch user name here]"  #UPDATE HERE
limit =100 #1-100
offset =0 #0-1600 (secret limit)
chan_f = "https://api.twitch.tv/kraken/channels/"+user+"/follows?"+"limit="+str(limit)+"&offset="+str(offset)

#Channel info
chan= "https://api.twitch.tv/kraken/channels/"+user
store=r.get(chan,headers=header)
print(store)
channel = store.json()
maxfollow=channel['followers']
print(user,"has",str(maxfollow),"followers")


#loop through all followers
#Intialize
tdate=[]
tname=[]
cursor=''
limit=100
offset=0

#using cursor pagination
while True:        
    chan_f = "https://api.twitch.tv/kraken/channels/"+user+"/follows?"+"limit="+str(limit)+"&cursor="+str(cursor)
    store=r.get(chan_f,headers=header)
    print(store)    
    dat=store.json()
    cursor=dat['_cursor']
    for i in range(len(dat['follows'])):
        fdat=dat["follows"][i]['created_at']
        tdate.append(fdat)
        dat['follows'][1]
        fdat=dat["follows"][i]['user']['name']
        tname.append(fdat)
        
    offset=offset+100
    if offset > maxfollow:
        break
    t.sleep(1)
len(tdate)

pre = {'date':tdate, 'name' : tname}
x=pd.DataFrame(pre)

x['cnt']=1
x['day']= pd.to_datetime(x['date'], format='%Y-%m-%d', errors='coerce')
x['day']=pd.DatetimeIndex(x['day']).normalize()

x.to_csv(user+"_out.csv")
