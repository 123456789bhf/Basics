# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:39:08 2023

@author: 23665
"""

#chapter2 算法分析

#什么是算法分析
#计算前n个数之和
import time
def sumofn(n):
    thesum=0
    for i in range(1,n+1):
        thesum=thesum+i
        
    return thesum

#计算执行时间
def sumofn1(n):
    starttime=time.time()
    thesum=0
    for i in range(1,n+1):
        thesum=thesum+i
    endtime=time.time()
    return thesum,endtime-starttime

for i in range(5):
    print('sum is %d required %10.7f seconds'%sumofn1(1000000))


#2.2.2检查两个长度相同，并均由小写字母组成的字符中的组成单词是否相同
#法一：'清'点法：一次从第一个字符串中取一个字母''，在依次与第二个字符串中的字母比较
'''
def anagramsolution1(string1,string2):
    alist=list(string2)
    pos1=0
    stillok=True
    while pos1<len(string1) and stillok:
        pos2=0
        found=True
        while pos2<len(alist) and found:
            if string1[pos1]==alist[pos2]:
                found=False
            else:
                pos2=+1 
        if not found:
            pos1=pos1+1
        else:
            stillok=False
    return stillok

print(anagramsolution1('heh','eeh'))

#方法二：排序法
def anagramsolution2(string1,string2):
    alist1=list(string1)
    alist2=list(string2)
    alist1.sort()
    alist2.sort()
    matchs=True
    pos=0
    while pos<len(alist1) and matchs:
        if alist1[pos]==alist2[pos]:
            pos=pos+1
        else:
            matchs=False
    return matchs
print(anagramsolution2('heh','eeh'))
#法三：暴力破解法
#法泗：计数法
def anagramsolution3(string1,string2):
    c1=[0]*26
    c2=[0]*26
    for i in string1:
        #将字母变成Unicode编码的函数，实现字母到数字的转换，进而与列表进行连接
        pos=ord(i)-ord('a')
        c1[pos]=c1[pos]+1 
    for i in string2:
        pos=ord(i)-ord('a')
        c2[pos]=c2[pos]+1 
    match=True
    pos=0
    while pos<26 and match:
        if c1[pos]==c2[pos]:
            pos=pos+1
        else:
            match =False
    return match
print(anagramsolution3('heh','ehh'))
        
#2。3python数据结构的性能
#生成列表的四种方式
def test1():
    l=[]
    for i in range(1000):
        l=l+[i]#将两个列表链接
def test2():
    l=[]
    for i in range(1000):
        l.append(i)
def test3():
    l=[i for i in range(1000)]
    
def test4():
    l=list(range(1000))
    
#使用timeit模块计算时间
#import timeit
t1=Timer('test1','from__main__ import test1')
print('concat',t1.timeit(number=1000),'milliseconds')

t2=Timer('test2','from__main__ import test2')
print('concat',t2.timeit(number=1000),'milliseconds')

t3=Timer('test3','from__main__ import test3')
print('concat',t3.timeit(number=1000),'milliseconds')

t4=Timer('test4','from__main__ import test1')
print('concat',t4.timeit(number=1000),'milliseconds')'''
#P56 2.5第5题给定一个数字列表，其中的数字随机排序，编写一个线性阶算法，找出第k小的元素
import random
alist=[i for i in range(1,20)]
#随机打乱列表顺序
random.shuffle(alist)
print(alist)
print(alist[2])
#生成一个1,20上均匀分布的随机列表
alist1=[random.randint(1,20) for i in range(20)]

print(alist1)

def kmin(list):
    list.sort()
    return list[2]
    #不能这样哦，会报错
    '''
    list=list.sort()
    reyurn list[2]
    '''
print(kmin(alist))
