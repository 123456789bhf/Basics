# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:54:12 2023

@author: 23665
"""
'''
#总结
#1）不管列表是否有序，顺序搜索算法的时间复杂度是O(n)
#2)对于有序列表来说，二分法搜索在嘴滑的情况下是O(logn)
#3)散列表的搜索排序算法可以达到常数阶
#4）冒泡排序’插入排序，选择排序的算法的时间复杂度是O(n2)
#5）希尔排序最坏的时间复杂度介于O(n)与O(n2)之间
#6）归并排序的时间复杂度是O(nlogn),但是需要额外的储存空间
#7)快速排序的时间复杂度是O(nlogn),但是当分割点不靠近列表中部时候会讲到O(n2),不需要额外的储存空间

#5.7 编程练习

#3. 不用切片运算，实现递归版本的二分搜索算法(记录初始位置，first,last将其作为函数参数)
def binarysearch(alist,item,first,last):
    if len(alist[first:last])==0:
        return False
    else:
        mid=(first+last)//2 
        if alist[mid]==item:
            return True
        elif alist[mid]<item:
            first=mid+1
            return binarysearch(alist,item,first,last)
        else:
            last=mid-1
            return binarysearch(alist, item,first,last)
lis=[1,3,4,5,7,12,45]
print(binarysearch(lis, 13, 0, len(lis)-1))

#4，5. 为散列表实现len方法，以及in方法
class HashTable:
    def __init__(self):
        self.size=11  #散列表初始大小:是素数，并且与要存储的元素个数之间相符合
        self.slots=[None]*self.size  #储存键
        self.data=[None]*self.size   #储存值
        self.height=0 #计算存储键值对个数
        
    #put函数是将键值对加入到映射中，如果键已经存在，那么就用新的值代替旧的值
    def put(self,key,data):
        hashvalue=self.hashfunction(key, self.size)
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
            self.height=self.height+1
        elif self.slots[hashvalue]==key:
            self.data[hashvalue]=data
        else:
            nextvalue=self.rehash(hashvalue,self.size)
            while self.slots[nextvalue]!=None and self.slots[nextvalue]!=key:
                nextvalue=self.rehash(nextvalue,self.size)
            if self.slots[nextvalue]==None:
                self.slots[nextvalue]=key
                self.data[nextvalue]=data
                self.height=self.height+1
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
    #获取键值对个数
    def __len__(self):
        return self.height
    #为散列表实现in方法
    def __contains__(self,key):
        if self.get(key)!=None:
            return True
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
print(H.slots)
print(len(H))
print(32 in H)
'''
#8. 实现平方探测的散列技巧
#14.. 不用切片运算符，实现mergesort函数
def mergesort(alist,first,last):
    print('splitting',alist)  #输出分解过程
    #基本结束条件：如果只有一个元素或者没有，那么就认为其是有序的
    if len(alist)>1:
        mid=(first+last)//2 
        #递归调用左右列表
    
        mergesort(alist,first,mid-1)
        mergesort(righthalf,mid,last)
        
        i=0
        j=mid
        k=0 
        #归并过程：将两个有序子列合并为一个有序序列
        #因为前面已经递归调用自身了，所以这里的都是有序的（从小到大排序）
        while i<mid and j<last+1:
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1 
        #如果有剩余就将其加入（因为两个子列表是有序的，所以在前面while循环之后可能有个子列表会剩余）
        while i<mid:
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j <last+1:
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print('merging',alist)
b=[54,26,93,17,77,31,44,55,20]
mergesort(b, 0, len(b)-1)