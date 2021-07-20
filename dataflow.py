#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[51]:


import pyvis
import numpy as np
import matplotlib.pyplot as plt
import uuid
# TODO: use with arbitrary Python code/call graphs/abstract syntax trees?


# In[212]:


class DataChain:
    def placeholder(self):
        pass
    p = placeholder
    
#     def __getitem__
    
    def __init__(self, *values, **namedvalues):
        self.values = list(values)
        self.namedvalues = namedvalues
#         self.aux
        self.nodes = []
