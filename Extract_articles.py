
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

page = requests.get('https://www.thequint.com/hot-news')
contents = page.content


# In[3]:


soup = BeautifulSoup(contents, 'lxml')


# In[8]:


for link in soup.find_all('a'):
    print(link.get('href'))


# In[5]:


len(soup.find_all('a'))


# In[6]:


len(soup.find_all('h3'))


# In[13]:


soup.find_all('h3')


# In[20]:


urls = []
for h in soup.find_all(class_='card-elements__link'):
    urls.append(h.get('href'))


# In[21]:


urls


# In[60]:


full_data = []


# In[61]:


for link in tqdm(urls):
    text = ""
    page = requests.get('https://www.thequint.com/hot-news'+link)
    contents = page.content
    soup_tmp = BeautifulSoup(contents, 'lxml')
    headline = soup_tmp.find(itemprop='headline').text
    author = soup_tmp.find(itemprop='author').a.text
    date = soup_tmp.find(itemprop='dateModified').get('content')
    passages = soup_tmp.find_all(class_='story-article__content__element--text')
    
    try:
        for passage in passages:
            text += passage.p.text
    except AttributeError:
        pass

    obj= {
        "headline": headline,
        "author": author,
        "date": date,
        "passage": text
    }
    full_data.append(obj)

# In[58]:


import csv


# In[80]:


with open("PATH HERE", 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(["headline", "author", "date", "passage"])
    for i in full_data:
#         print(i.headline)
        writer.writerow([i['headline'], i['author'], i['date'], i['passage']])


# In[ ]:




