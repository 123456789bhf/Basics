# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 15:17:16 2023

@author: 23665
"""

#chapter 7 图及其算法

#7.2 术语以及定义
#顶点：顶点又称节点，使徒的基础部分。它可以有自己的名字，我们称为“键”。定点也可带有附加信息，我们成为“有效载荷”
#边：两个定点通过一条边项链，表示它们之间存在关系。边既可以是单向的，也可以是双向的。如果图中所有边都是单向的，称为“有向图”
#权重：表示从一个顶点到另一个顶点的成本


#图:可以用G=(V,E)表示，V是图的点的集合，E是图边的集合。每条边是一个二元数组(v,e),其中v,e在V中。可以向边的二元组中添加一个元素，用于表示权重
#E={(v1,v3,5)，(V1,V4,90)},如果是有向图，那么(v1,v3,5)表示v1指向节点v3得便，并且权重是5

#路径：是由边连接的顶点组成的序列。路径的正式定义为：w1,w2,...,wn,其中，对于所有的1<=i<=n-1,有(wi,wi+1)在边集合E里面
#环：有向图中的一条起点与终点为同一顶点的路径，没有环的图称为无环图，没有换有向图称为有向无环图，简称DAG

#7.3.1 邻接矩阵
#实现图，最直接的方式是二维矩阵。在矩阵实现中，每一行和每一列都表示图中的一个顶点，第v行和第w列交叉的格子中的值表示从顶点v到顶点w的边的权重/
#如果两个顶点被一条边连接起来，就称他们是相邻的。
#如果边是有权重的，那么设定行列值。如果是无权边，将矩阵分量标注为1 或者为0
#问题：现实生活中图对应的矩阵都是稀疏的，这样储存数据并不高效，因此邻接矩阵适用于有很多边的图。

#7.3.2  邻接表
#在邻接表的实现中，我们位图对象的所有顶点保存一个主列表，同时为每一个定点对象都维护一个列表，其中记录了与他相连接的顶点。

#7.3.3实现
#代码7-1 vertex类：
#vertex是用字典connectdeto来记录与其相连的顶点，以及每一条边的权重
class vertex:
    def __init__(self,key):
        self.id=key  #通常是一个字符串,是当前的节点，即新创建的节点
        self.connectdeto={}
    #与该顶节点相连接的顶点以及之间的权重,nbr是顶点对象的键key,也就是顶点的值
    def addneighbor(self,nbr,weight=0):
        self.connectdeto[nbr]=weight
    #特殊的实例方法，调用print()
    def __str__(self):
        return str(self.id)+' connectedto'+str([x.id for x in self.connectdeto])
    #返回字典的所有的键，也就是所有邻接边
    def getconnections(self):
        #返回字典所有的键
        return self.connectdeto.keys()
    #返回当前节点值
    def getid(self):
        return self.id
    #获得指定邻接边的权重
    def getweight(self,nbr):
        return self.connectdeto[nbr]
#代码7-2 graph类
#包含一个将顶点名映射到定点对象的字典。graph类也提供了像图中添加顶点和连接不同顶点的方法。
class graph:
    def __init__(self):
        self.verlist={}  #顶点
        self.numgvertices=0 #顶点数量
    #向图中添加顶点
    def addvertex(self,key):
        self.numgvertices=self.numgvertices+1
        newvertex=vertex(key)
        self.verlist[key]=newvertex
        return newvertex
    #通过key查找顶点
    def getvertecx(self,n):
        #n是否为self.verlist中的键
        if n in self.verlist:
            return self.verlist[n]
        else:
            return None
    #直接调用x in a等价于a.__contains__(x)
    def __contains__(self,n):
        return n in self.verlist
    #在两节点f,t之间添加边，并且权重为cost
    def addedge(self,f,t,cost=0):
        #如果节点f不在里面，就加入该节点
        if f not in self.verlist:
            self.addvertex(f)
        #如果节点t不在图中，就加入该节点
        if t not in self.verlist:
            self.addvertex(t)
        #添加邻接边以及权重
        self.verlist[f].addneighbor(self.verlist[t],weight=cost)
    #获得所有的键（顶点）
    def getvertices(self):
        return self.verlist.keys()
    def __iter__(self):
        return iter(self.verlist.values())
    
g=graph()
for i in range(6):
    g.addvertex(i)
print(g.verlist)
g.addedge(0,1,5)
g.addedge(0,5,2)
g.addedge(1,2,4)
g.addedge(2,3,9)
g.addedge(3,4,7)
g.addedge(3,5,3)
g.addedge(4,0,1)
g.addedge(5,4,8)
g.addedge(5,2,1)
for v in g:
    for w in v.getconnections():
        print('(%s,%s)'%(v.getid(),w.getid()))

#7.4 广义优先搜索
#7.4，1 词梯问题
#代码7-3 为词梯问题构建单词关系图
def buildgraph(wordfile):
    d={}  #用于储存桶。，字典的键就是桶上的标签，值是对应的单词列表
    g=graph()
    wfile=withopen(wordfile,'r')
    #将文件中四个字的单词添加到d中，字典上的键是同上的标签，值是对应的单词列表
    for line in wfile:
        for i in range(len(line)):
            bucket=line[:i]+'_'+line[i+1:] #字符串相连接，line[:i]是字符串
            #如果d中已经有桶了，那么就添加新的单词
            if bucket in d:
                d[bucket].append(line)
            #如果d中没有桶，那么就设置键值对
            else:
                d[bucket]=[line]
    #为同一个桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in bucket:
            for word2 in bucket:
                if word1!=word2:
                    #addedge实例方法如果没有新的节点，那么就将新的节点添加到图中，然后再向起加入边
                    #默认两个顶点之间新添加边的权重是0
                    g.addedge(word1, word2)
    return g

#7.4.3 实现广度优先搜索
from chapter3基本数据结构 import Queue
def bfs(g,start):
                
        
        
        
        
