#!/usr/bin/env python
# coding: utf-8

# # Analysis 

# In[1]:


import numpy as np


# In[2]:


arr = np.random.rand(5)


# In[3]:


arr.mean()


# In[4]:



import time
from tqdm.notebook import trange


# In[5]:


for i in trange(10):
    x= i**2 + i 
    time.sleep(0.1)
    


# In[ ]:




