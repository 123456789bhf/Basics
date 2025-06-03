# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:06:03 2023

@author: 23665
"""

#5.2 搜索

#5.2.1 顺序搜索
#因为列表是有序集合，每一项数据只有唯一的前驱回和后继，也就是每个数据项的位置与其他的数据项相关。
#在python列表中数据项的位置就是其下标，所以能顺序访问

#代码5-1 无序列表的顺序搜索
def sequentialsearch(alist,item):
    pos=0
    found=False
    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pop=pos+1
    return found

#print(sequentialsearch([1,23,3],23))

#代码5-2 有序列表的顺序搜索
def orderedsequentialsearch(alist,item):
    pos=0
    found=False
    stop=False
    while (pos<len(alist)) and (not found) and (not stop):
        if alist[pos]==item:
            found=True
        elif alist[pos]>item:
            stop=True
        else:
            pos=pos+1
    return found

#print(orderedsequentialsearch([1,3,4,67], 2))
#5.2.2 二分搜索

#代码5-3 有序列表的二分搜索

#二分搜索的复杂度是O(logn)

#有序列表的二分搜索是分治策略的好例子
#分治策略：将大问题分解成小问题，通过一些方法解决小问题，然后整合结果，最终解决最初的问题

def binarysearch(alist,item):
    first=0
    last=len(alist)-1
    mid=(first+last)//2
    found=False
    while first<=last and not found:
        if alist[mid]==item:
            found=True
        elif alist[mid]>item:
            last=mid-1
        else:
            first=mid+1
        mid=(first+last)//2
        
    return found
#print(binarysearch([1,2,5], 5))

#代码5-4二分搜索的递归版本
#但是列表的切片的复杂度是O(K)，最终二分法的复杂度不是O(logn)
#可以在传入列表时候带上上头和下尾的坐标
def binarysearch1(alist,item):
    if len(alist)==0:
        return False
    else:
        mid=(len(alist)-1)//2
        if alist[mid]==item:
            return True
        elif alist[mid]<item:
            return binarysearch1(alist[mid+1:], item)
        else:
            return binarysearch1(alist[:mid-1], item)
    
    
print(binarysearch1([1,4,5,6,89,890], 891))


#5.2.3散列
#有序列表的二分法搜索的复杂度是对数阶，通过散列可以将时间复杂度降到O(1)

#解决冲突的方法
#1. 完美散列函数：给定一个元素的集合，能将元素映射到不同的槽，这样的函数成为完美散列函数
#散列函数的构造目标：冲突最少，计算方便，元素均匀分布在散列表中
#为实现上述散列函数的构造目标，有以下几种方法
#1） 折叠法：将元素切成等长的把部分，然后将这几部分相加得到散列值，之后求余数（散列表的长度）
#2）平方取中法：先将元素平方，然后取中间几位数
#3）基于字符元素（比如：字符串）创建散列函数


#作为一直校验的数据‘指纹函数’需要具有如下的性质；
#1)易压缩性：任意长度的数据得到的指纹的长度是固定的
#2）容易计算性：从原来数据计算指纹更容易，从指纹计算元数据基本不可能（加密）
#3）抗修改性：对原数据的微小变动会引起指纹的巨大改变
#4）抗冲突性：已经知道原数据和指纹，想要找到相同指纹的数据是非常困难的，最著名的是MD5和SHA函数

#区块链
#区块链是一种分布式的数据库
#1）通过网络连接的节点
#2）每个节点都保存着整个数据库的所有数据
#3）任何地点存入的数据都会完成同步

#散列函数的应用：区块链技术
#详细见PPT:区块链技术

#5-5 为字符串构造简单的散列函数
def hash(astring,tablesize):
    sum=0
    #ord()获得字符的ASCII码
    for pos in range(len(astring)):
        sum=sum+ord(astring[pos])
        
    return sum%tablesize

#print(hash('cat',11))

#上述方法的缺点是对于异序词，杉树散列函数计算的结果相同
#下面通过增加权重的方法来防止上述情况发生
def hash1(astring,tablesize):
    weight=[i for i in range(1,tablesize+1)]
    sum=0
    for i in range(len(astring)):
        sum=sum+weight[i]*ord(astring[i])
    
    return sum%tablesize
print(hash1('cat', 11))

#2 处理冲突的方法
#1）开放地址法：在散列表中找到另一个空槽用于防止引起冲突的元素，简单的做法是从初始位的散列值开始，顺序遍历散列表，知道找到一个空槽
#注意：为了遍历散列表，可能需要往回检查的第一个槽。这个过程称为开放地址方法，他尝试在散列表中寻找下一个空槽或者地址。由于是逐个访问槽，
#因此这个方法称为线性探索
#上述方法容易发生元素聚集，要避免上述过程，一种方法是扩展线性散列，不在一次顺序查找空槽，而是跳过一些槽，这样能使得引起冲突的 元素分布更加均匀
#再散列：值冲突发生后寻找另一个槽的过程
#再散列函数可以定义为rehash(pos)=(pos+skip)%sizetable
#注意：skip的大小要保证列表中所有槽最终都被访问到，否则就会浪费资源，所以散列表的大小常常为素数
#2）平方探测：是线性探测的一个变体，他不采用固定的跨步(skip)的大小，而是通过再散列函数递增散列值，也就是平方探测的跨步大小是一系列完全平方数
#3）链表发：每个槽都有一个指向元素集合（或链表）的引用
#链表法的平均算下来每个槽的元素不多，因此搜索更加高效

#3. 实现映射抽象数据类型
#映射抽象数据类型（ADT MAP）：将键和值关联起来的无序集合，其中键是不重复的，键和值之间是一一对应关系

#代码5-6 实现ADT MAP类（类似于字典）
#思路：
#创建两个列表，将键和值放在列表的同一位置，键是不同的，所以可以对键的放置使用散列表，这样时间复杂度是常数阶O(1)

class HashTable:
    def __init__(self):
        self.size=11  #散列表初始大小:是素数，并且与要存储的元素个数之间相符合
        self.slots=[None]*self.size  #储存键
        self.data=[None]*self.size   #储存值
        
    #put函数是将键值对加入到映射中，如果键已经存在，那么就用新的值代替旧的值
    def put(self,key,data):
        hashvalue=self.hashfunction(key, self.size)
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        elif self.slots[hashvalue]==key:
            self.data[hashvalue]=data
        else:
            nextvalue=self.rehash(hashvalue,self.size)
            while self.slots[nextvalue]!=None and self.slots[nextvalue]!=key:
                nextvalue=self.rehash(nextvalue,self.size)
            if self.slots[nextvalue]==None:
                self.slots[nextvalue]=key
                self.data[nextvalue]=data
            else:
                self.data[nextvalue]=data
                
    def hashfunction(self,key,size):
        return key%size
    def rehash(self,oldhash,size):
        #不能直接(oldhash+1)，这样无法便利散列表起点
        return (oldhash+1)%size #这里设置的步长是1，为什么要在求余数：因为如果散列表尾部仍未找到，那么需要返回到起点，求余数能返回到散列表起点
    

    #get函数返回key对应的值，如果key不存在，那么返回None
    def get(self,key):
        startslot=self.hashfunction(key, self.size)
        data=None  #因为key不存在的时候会犯或NOne,所以先设置为None
        found=False #用来控制while循环,也就是是否为空槽
        stop=False  #用来控制回到起点
        #循环结束条件：空槽或者回到起点
        #空槽没有找到
        while self.slots[startslot]!=None and not found and not stop:
            if self.slots[startslot]==key:
                found=True  #找到结束循环
                data=self.data[startslot]
            else:
                startslot=self.rehash(startslot,self.size) #没有找到，继续找下一个槽
                if startslot==self.hashfunction(key, self.size):
                    stop=True   #回到起点，结束循环，没找到
        return data
    #特殊的实例方法，可以使用a[]来得到返回结果
    def __getitem__(self,key):
        return self.get(key)
    #可以a[key]=data来调用实例函数
    def __setitem__(self,key,data):
        self.put(key, data)

H=HashTable()
H[32]='cat'
H[26]='dog'
H[93]='lion'
H[17]='tiger'
H[77]='bird'
H[31]='cow'
H[44]='goat'
H[55]='pig'
H[20]='chicken'
print(H.slots)
print(H.data)
print(H[32])
H[26]='duck'
print(H[26])
print(H[99])


#5.3.1 冒泡排序:O(n2)
#每轮便利都将下一个最大值放在正确位置上
def bubblesort(alist):
    #从列表中的最后一个元素开始
    for m in range(len(alist)-1,0,-1):
        for n in range(m):
            if alist[n]>alist[n+1]:
                #如果前一个元素小于后一个，交换位置
                a=alist[n]
                alist[n]=alist[n+1]
                alist[n+1]=a
                #python允许 同时赋值
                #下面语句与上述三条语句等价
                #alist[n],alist[n+1]=alist[n+1],alist[n]
        return alist

print(bubblesort([1,3,2,9,5,6,7]))

#5-10 修改后的冒泡排序函数
#如果在议论遍历中没有发生元素交换，就可以确定列表已经有序，可以修改冒泡排序，使得其遇见这种情况提前终止
def shortbubblesort(alist):
    exchange=True
    passnum=len(alist)-1
    while passnum>0 and exchange:
        exchange=False
        for m in range(passnum):
            if alist[m]>alist[m+1]:
                a=alist[m]
                alist[m]=alist[m+1]
                alist[m+1]=a
                exchange=True
        passnum=-1
            
    return alist
print(shortbubblesort([1,3,2,9,5,6,7]))

#python的局部变量与全局变量
#在函数里面定义的变量是局部变量
#在函数外面定义的变量的是全局变量
a=3  #全局变量
def function():
    a=2  #局部变量
    
function()
#这里输出a的值是全局变量的值，也就是3
print(a)
a=3
def function1():
    global a  #让a是全局变量
    a=2
function1()
print(a)
    
#全局变量在函数的内部不能直接修改
a=2
def temp():
    a=a+1 #出错
temp()
    


#5.3.2 选择排序：O(n2)(时间复杂度)
#每次遍历寻找最大值，并将其最正确的位置交换

def selectsort(alist):
    for m in range(len(alist)-1,0,-1):
        max=0
        for n in range(1,m+1):
            if alist[n]>alist[max]:
                max=n 
        temp=alist[m]
        alist[m]=alist[max]
        alist[max]=temp
    return alist
print(selectsort([1,2,32,43,23,13]))

#5.3.3 插入排序：
#时间复杂度：在最快的情况下，比较次数是前n-1个整数之和，对应的时间复杂度是O(n2)
#在最好的情况下，每一轮只需要比较一次，共n-1轮，对应的时间复杂度是O(n)(这种是列表有序的情况下，实际上列表越接近与有序，插入排序的对比次数就越少)
#思路：
#首先假设位置0处的元素是只含有单个元素的有序子列表，。从元素1到元素n-1,每一轮都将当前元素
#与有序子列表中的元素进行比较。在有序子列表中，将比它大的元素右移，当遇到比它小的元素
#或者抵达列表的终点时，就可以插入当前元素

def insertionsort(alist):
    #有序列表是从1开始的，一直增加到长度为len(alist)-1
    for m in range(1,len(alist)):
        currentvalue=alist[m]
        pos=m
        #当到达列表终点或者比它小的元素时候停止）
        while pos>0 and alist[pos-1]>currentvalue:
            #将比它的元素右移一个位置
            alist[pos]=alist[pos-1]
            pos=pos-1
            
        alist[pos]=currentvalue
    return alist

print(insertionsort([1,4,3,45,34,123,90]))

            
#5.3.4 希尔排序
#时间复杂度在O(n)到O(n2)之间。按照下面的代码时间复杂哦都是O(n2).通过改变增量，比如（1，3，7，15，31，。。。）可以使得时间复杂度将为O(n3/2)
#也成为‘递减增量排序’，对插入排序做了改进，将列表分成数个子列表，并对每个子列表应用插入排序
#如何对列表进行切分是希尔排序的关键--并不是连续的切分，而是使用增量（步长）i选取所有间隔为i的元素组成子列表（共有i个子列表）
#5-13 希尔排序函数
def shellsort(alist):
    sublistcount=len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapinsertiondort(alist, startposition, sublistcount)
        print('after increments of size',sublistcount,'the list is',alist)
        sublistcount=sublistcount//2
    
#对子序列采用的是插入排序，子序列是从start下标开始，步长为gap的子序列
def gapinsertiondort(alist,start,gap):
    for m in range(start+gap,len(alist),gap):
        currentvalue=alist[m]
        pos=m
        while pos>start and alist[pos-gap]>currentvalue:
            #将比其大的元素后移一个位置
            alist[pos]=alist[pos-gap]
            pos=pos-gap
        alist[pos]=currentvalue
        
shellsort([54,26,93,17,77,31,44,55,20])


#5.3.5. 归并排序
#时间复杂度是O(nlogn)
#注意：mergesort函数需要额外的储存空间来储存切片操作得到的两半部分。当列表较大时候，使用额外的储存空间可能会使得排序出现问题

#思想
#是分治策略，它是一种递归算法，每次将列表一分为二。如果列表是空或者只有一个元素，那么定义上来说他就是有序的（基本情况)
#如果列表不止一个元素，那么就将列表一份为二，并且对两部分都递归调用归并排序，当两部分都有序之后，就进行归并这一基本操作
#归并是将两个较小的有序序列归并为一个有序列表的过程
def mergesort(alist):
    print('splitting',alist)  #输出分解过程
    #基本结束条件：如果只有一个元素或者没有，那么就认为其是有序的
    if len(alist)>1:
        mid=len(alist)//2 
        #递归调用左右列表
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        
        i=0
        j=0
        k=0 
        #归并过程：将两个有序子列合并为一个有序序列
        #因为前面已经递归调用自身了，所以这里的都是有序的（从小到大排序）
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1 
        #如果有剩余就将其加入（因为两个子列表是有序的，所以在前面while循环之后可能有个子列表会剩余）
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j <len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print('merging',alist)

#5..3.6. 快速排序
#如果划分操作总是发生在列表中部，就会切分logn次，为了找到分割点，n个元素都要与基准值进行比较
#所以时间复杂度是O(nlogn)。另外递归操作不需要额外的储存空间(归并排序需要额外的储存空间储存列表，但是快速排序不需要)
#在最坏的情况下，分割点不在列表中不，而是偏向某一段，这会导致且分布均匀。在这种情况下，含有n个元素的
#列表可能被分为不含元的列表与含有一个n-1元素的列表。然后，含有n-1个元素的列表可能被分为不含元素的列
#表与含有n-2个元素的列表，以此类推，导致时间复杂度是O(n2)

#注意：1)可以采取三数取中发避免分割不均匀，即在选择的时候考虑中间元素‘头部元素，尾部元素，取中间的那个值作为分割点
#2）也可以根据先验分布，比如均匀分布，但会产生额外的开销，仍不能排除极端情况
alist=[54,26,93,17,77,31,44,55,20]
def quicksort():
    global alist
    #设置列表中第一个元素为基准点
    quicksorthelper(alist,0, len(alist)-1)
    
def quicksorthelper(alist,first,last):
    if first<last:
        splitpoint=partition(alist, first, last)
        quicksorthelper(alist, splitpoint+1, last)
        quicksorthelper(alist, first, splitpoint-1)
    
#展示了课本P57的移动过程
def partition(alist,first,last):
    leftmark=first+1  
    rightmark=last
    pivotvalue=alist[first]  #自己设置的基准值
    done=False  #用来控制循环体，一直让其交换

    #如果
    while not done:
        while pivotvalue>=alist[leftmark] and leftmark<=rightmark:
            leftmark=leftmark+1
            
        while pivotvalue<=alist[rightmark] and rightmark>=leftmark:
            rightmark=rightmark-1
        #如果左边的大于右边的，那么交换
        if leftmark<rightmark:
            a=alist[leftmark]
            alist[leftmark]=alist[rightmark]
            alist[rightmark]=a
        else:
            done=True
    #将基准值与rightmark的值进行交换
    
    a=alist[first]
    alist[first]=alist[rightmark]
    alist[rightmark]=a
    return rightmark

quicksort()
print(alist)
        
    
    
        
    

