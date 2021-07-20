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
        
#         for v in range(len(self.values)):
        for iv, v in enumerate(self.values):
            if type(v) not in [N, Node]:
                self.values[iv] = N(data=v)
            self.values[iv].set_graph(self)
            
#         for iv, v in enumerate(self.nodes):
#             if type(v) not in [N, Node]:
#                 self.nodes[iv] = N(data=v)
        
#         for i in range(len(self.values)):
#             for r in self.values[i].inputs:
#                 self.values.insert(i, r)
#                 i -= 1
        
        for iv, v in enumerate(self.nodes):
#             if type(v) in [N, Node]:
            if v.i is not None:
                v.inputs.insert(0, self.values[self.values.index(v)-v.i])
        
D = DataChain

node_id = 0
def savefig(x):
    plt.close('all')
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.imshow(x)
    path = f'cache/node_img_{node_id}.svg'
    plt.axis('off')
    plt.savefig(path)
    return path

class R:
    pass
for r in ['normal']:
    setattr(R, r[0], getattr(np.random, r))

flow = [
#     D(R.n(0, 1, [20]*2), (np.power, , 2))
#     D(N(np.random.normal(0, 1, [50, 50])) * )
#     D(a=R.n(0,1,[20]*2))
]
