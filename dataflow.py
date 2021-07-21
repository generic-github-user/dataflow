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

class Node:
    def __init__(self, i=None, data=None):
        self.i = i
        self.inputs = []
        self.id = uuid.uuid4().hex
        self.op = None
        self.data = data
    
    def set_graph(self, g):
        self.graph = g
        if self not in g.nodes:
            g.nodes.append(self)
        for i in self.inputs:
            i.set_graph(g)
        return self
    
    def add_input(self, n):
        if type(n) in [list, tuple]:
            for ni in n:
                self.add_input(ni)
        else:
            if type(n) not in [N, Node]:
                n = N(data=n)
            self.inputs.append(n)
        return self
    
#     def __pow__(self, n):
#         self.op = np.power
#         self.add_input(n)
#         return self

opnames = {
    'pow': lambda q: np.power(*q),
    'mul': lambda q: np.prod(q, axis=0),
    'add': lambda q: np.sum(q, axis=0),
}
def magic_method(func):
        def M(self, *args):
            self.op = func
            print(args)
            self.add_input(args)
            return self
        return M
