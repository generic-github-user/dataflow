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


# In[422]:


class Overloader:
    def __init__(self, obj, **methods):
        self.obj = obj
#         for i, j in methods.items():
#             setattr(self, f'__{i}__', j)

    def __mul__(self, n):
        return [self.obj.gen() for l in range(n)]


# In[486]:


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
for a, b in opnames.items():
    if callable(b):
        opfunc = b
    else:
        opfunc = getattr(np, b)
    setattr(Node, f'__{a}__', magic_method(opfunc))

N = Node

flow = [
    D(R.n(0, 1, [20]*2), N(1)**3, N(1)**3)
]

vis = pyvis.network.Network(width=1000, height=1000, notebook=True, directed=True)
for f in flow:
    prev = None
    for v in f.values:
        meta = {
            'label': v.data
        }
        if type(v) in [list, tuple]:
            print(True)
            if prev is not None:
                args = list(v[2:])
                if type(args) not in [list, tuple]:
                    args = [args]
                v = N(data=v[0](prev,*args))
        
        print([type(v_.data) for v_ in v.inputs])
        if v.op and len(v.inputs)>0:
#             print([I.data if type(I) is Node else I for I in v.inputs])
            v.data = v.op([I.data if type(I) in [Node, N] else I for I in v.inputs])
        
#         print(type(v), type(prev), v.data)
        if type(v.data) is np.ndarray:
            p = savefig(v.data)
            meta = {
                'size': 50
            }
#             meta['image'] = 'file:///'+p[:].replace('/','\\')
            meta['image'] = p#[:].replace('/','\\')
            meta['shape'] = 'image'
            meta['label'] = 'I'
        
#         print(type(v.id))
#         print(meta)
    
        if type(v.data) in [int, float, str, bool]:
            meta = {
                'label': v.data
            }
        vis.add_node(n_id=v.id, **meta)
        node_id += 1
    for v in f.values:
        for i in v.inputs:
            if type(i.data) in [int, float, str, bool]:
                meta = {
                    'label': i.data
                }
            if not i.id in vis.node_ids:
                vis.add_node(n_id=i.id, **meta)
            vis.add_edge(i.id, v.id, smooth=True)
    
        
        prev = v

# vis.show('./graphvis.html')
vis.save_graph('./graphvis.html')


# In[180]:


([s.data for s in flow[0].values[1].inputs])


# In[154]:


[list(map(type,v.inputs)) for v in flow[0].values]


# In[108]:


# ...
# _a


# In[ ]:




