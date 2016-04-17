
# coding: utf-8

# In[22]:

import requests
import hashlib
import datetime
import string
import csv


# In[23]:

public_key = "bbca2c9c88fb26b6186f7adc5dafbc3e"
private_key = "f850ae27c606bc96740132921ab101c0e69d6511"


# In[24]:

def get_TS_HASH( pub_key, priv_key):
    ts = str(datetime.datetime.now()).replace(" ", "").replace(".", "").replace("-", "").replace(":", "")
    m = hashlib.md5()
    h = ts + priv_key + pub_key
    m.update( h.encode('utf-8'))
    h = m.hexdigest()
    return ts, h
    


# In[25]:

def make_url(base_url,limit,offset, pub_key, priv_key):
    ts, h = get_TS_HASH( pub_key, priv_key)
    get_url = base_url + '?ts=' + ts + '&limit=' + str(limit) + '&offset=' + str(offset) + "&apikey=" + pub_key + '&hash=' + h
    return get_url


# In[26]:

filepath = 'Authored_comic.csv'
out_put = open(filepath, "w+", newline='')
datafile = csv.writer(out_put) 
header = ['comic_id','creator_id']
datafile.writerow(header)


# In[27]:

creator_comic_url = "http://gateway.marvel.com:80/v1/public/comics/%s/creators"


# In[28]:

comic_file = open('./comics.csv', "r")
comic_file.readline()
comic_id = []
for line in  comic_file:
    comic_id.append( line.split(',')[0])
comic_file.close()


# In[29]:

for i in range(len(comic_id)):
    url = (creator_comic_url % comic_id[i])
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
            creator = data['results'][j]
            row.append(comic_id[i])
            row.append(creator['id'])
            
            datafile.writerow(row)
    
    r = requests.get(make_url(url, 100, count, public_key, private_key))
        
    if(r.status_code != 200):
        print("something wrong!!! error code of %d"% r.status_code)
        break;
        
    data = r.json()['data']
        
        
out_put.close()   
    


# In[177]:



