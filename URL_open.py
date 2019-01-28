
# coding: utf-8

# In[18]:


import urllib


# In[19]:


from bs4 import BeautifulSoup


# In[20]:


page = "https://aisel.aisnet.org/cais/vol37/iss1/1/"


# In[21]:


open_page = urllib.request.urlopen(page)


# In[22]:


Soup = BeautifulSoup(open_page,'html.parser')


# In[23]:


for div in Soup.findAll('div', {'id':'title','class': 'element'}):
    a = div.findAll('a')[0]
    print (a.text.strip())


# In[25]:


for div in Soup.findAll('div', {'id':'abstract','class': 'element'}):
    a = div.findAll('p')[0]
    print (a.text.strip())


# In[27]:


for div in Soup.findAll('div', {'id':'authors','class': 'element'}):
    a = div.findAll('p')[0]
    print (a.text.strip())


# In[28]:


for div in Soup.findAll('div', {'id':'recommended_citation','class': 'element'}):
    a = div.findAll('p')[0]
    print (a.text.strip())

    
#In[29]


for div in Soup.findAll('div', {'id':'doi','class': 'element'}):
    a = div.findAll('p')[0]
    print (a.text.strip())
