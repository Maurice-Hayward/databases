
# coding: utf-8

# In[32]:

import requests
import hashlib
import datetime
import string
import csv


# In[33]:

public_key = "bbca2c9c88fb26b6186f7adc5dafbc3e"
private_key = "f850ae27c606bc96740132921ab101c0e69d6511"
filepath = "comics_characters_appeared_in.csv"


# In[34]:

def get_TS_HASH( pub_key, priv_key):
    ts = str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace("-", "").replace(":", "")
    m = hashlib.md5()
    h = ts + priv_key + pub_key
    m.update( h.encode('utf-8'))
    h = m.hexdigest()
    return ts, h
    


# In[35]:

def make_url(base_url,limit,offset, pub_key, priv_key):
    ts, h = get_TS_HASH( pub_key, priv_key)
    get_url = base_url + '?ts=' + ts + '&limit=' + str(limit) + '&offset=' + str(offset) + "&apikey=" + pub_key + '&hash=' + h
    return get_url


# In[36]:

filepath = 'comics_by_event_happen_in.csv'
out_put = open(filepath, "w+", newline='')
datafile = csv.writer(out_put) 
header = ['event_id','comic_id']
datafile.writerow(header)


# In[37]:

event_comic_url = "http://gateway.marvel.com:80/v1/public/events/%s/comics"


# In[38]:

event_file = open('./event.csv', "r")
event_file.readline()
event_id = []
for line in  event_file:
    event_id.append( line.split(',')[0])
event_file.close()


# In[39]:

for i in range(len(event_id)):
    url = (event_comic_url % event_id[i])
    count = 0
    r = requests.get(make_url(url, 100, count, public_key, private_key))
    if(r.status_code != 200):
        print("something wrong!!! error code of %d"% r.status_code)
    data = r.json()['data']
    total = data['total']
    while(count < total):
        count = count + data['count']
        for j in range(len(data['results'])):
            row = []
            comic = data['results'][j]
            row.append(event_id[i])
            row.append(comic['id'])
            
            datafile.writerow(row)
    
    r = requests.get(make_url(url, 100, count, public_key, private_key))
        
    if(r.status_code != 200):
        print("something wrong!!! error code of %d"% r.status_code)
        break;
        
    data = r.json()['data']
        
        
out_put.close()   
    


# In[177]:



