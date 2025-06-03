# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:08:52 2023

@author: 23665
"""

#chapter3 基本数据结构
#基本数据结构：
#3.3.3勇python实现栈，假设列表是一个栈，列表的右边是栈顶
class Slack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    #查找栈中顶部的第一个元素
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
s=Slack()
print(s.isEmpty())
s.push(2)
s.push('dog')
print(s.peek())
print(s.isEmpty())
print(s.size())

#栈的另一种实现：列表的左边是栈顶
#虽然栈的两种实现方式不同，但是他们的运行时间不一样，push,pop的时间复杂度不同
class Slack1:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        return self.items.insert(0,item)
    
    def pop(self):
        return self.items.pop(0)
    
    #查找栈中顶部的第一个元素
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

#3.3.4栈的应用一：匹配括号
def parChecker(symbolstring):
    s=Slack()
    index=0
    balanced=True#用来判断右括号多的情况
    while index<len(symbolstring) and balanced:
        if symbolstring[index]=='(':
            s.push('(')
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1
    
    if s.isEmpty() and balanced:
        return True
    else:
        return False
print(parChecker('(()())'))

#3.3.5栈的应用二：普通情况：匹配符号

#定义一个括号是否对应的函数，当然也可以直接在类中定义两个字典，键为括号类型，值可以设置为1，2，3
def matches(open,close):
    opens='{[('
    closers='}])'
    #字符串也可以通过index访问指定字符的索引
    return opens.index(open)==closers.index(close)
print(matches('{',']'))

def parChecker1(symbolstring):
    s=Slack()
    index=0
    balanced=True#用来判断右括号多的情况
    while index<len(symbolstring) and balanced:
        if symbolstring[index] in '({[':
            s.push(symbolstring[index])
        else:
            if s.isEmpty():
                balanced=False
            else:
                if matches(s.peek(),symbolstring[index]):
                  s.pop()  
                else:
                    balanced=False
        index=index+1
    
    if s.isEmpty() and balanced:
        return True
    else:
        return False
print(parChecker1('({}[)'))

#3.3.6 栈的应用四：将十进制数转变为二进制数

def divideBy2(decNumber):
    #空栈
    s=Slack()
    
    while decNumber>0:
        rem=decNumber%2
        decNumber=decNumber//2
        s.push(rem)
        
    binstring=''
    while  not s.isEmpty():
        #将两个字符相连接，str()转变为字符
        binstring=binstring+str(s.pop())
        
    return binstring

print(divideBy2(233))

#栈的应用四：将十进制数转变为2-16进制数，A：10，B:11,,,,F:15
#base:2-16任意取一个数字
def divideBy21(decNumber,base):
    #空栈
    s=Slack()
    digits='0123456789ABCDEF'
    while decNumber>0:
        rem=decNumber%base
        decNumber=decNumber//base
        s.push(rem)
        
    binstring=''
    while  not s.isEmpty():
        #将两个字符相连接，str()转变为字符
        binstring=binstring+digits[s.pop()]
        
    return binstring


print(divideBy21(233,7))


#3.3.7 栈的应用五：前序、后序、中序表达式
#中序表达式向后序表达式的'转换'
a='s d'
list=a.split()
print(list)
import string 
def infixToPostfix(infixexpr):
   
    #用字典定义运算符的优先级,左括号的优先级最小，这样任何与左括号比较的运算符都会被放入栈中
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    #存放运算符以及括号
    opstack=Slack()
    #存放结果
    PostfixList=[]
    
    #按空格将字符串分开，将分开后的结果放在列表中，结果是列表
    tokenList=infixexpr.split()
    
    for token in tokenList:
        if token in string.ascii_uppercase:
            PostfixList.append(token)
           #包含所有大写字母字符串，也可以勇'ABCDEFGHIJKLMNOPQISTUVWXYZ'
        elif token=='(':
            opstack.push(token)
        elif token==")":
            toptoken=opstack.pop()
            while toptoken!='(':
                PostfixList.append(toptoken)
                toptoken=opstack.pop()
        else:
            #下面别忘记加括号，当判别式比较复杂的时候需要加上括号
            while (not opstack.isEmpty()) and (prec[opstack.peek()]>=prec[token]):
                 PostfixList.append(opstack.pop())
            opstack.push(token)
        
        #最后可能还剩一些运算符按照优先级从低到高排序的运算符，那么需要将其放入结果中
    while not opstack.isEmpty():
        PostfixList.append(opstack.pop())    
            
        #是个字符串，将列表表中的元素用空格相连接，用个空格分开 str.split(),用空格链接列表中的元素' '.join(list),结果是字符串
    return " ".join(PostfixList)   


#别忘记加空格哦
print(infixToPostfix("( A + B ) * ( C + D )"))
    
print(infixToPostfix("( A + B ) * C"))     
print(infixToPostfix('A + B * C'))        

#  实现后续表达式的计算
def domath(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op1+op2
    else:
        return op1-op2
    
#定义函数
def postfixEva1(postfixexpr):
    operandstack=Slack()
    tokenlist=postfixexpr.split()
    for token in tokenlist:
        if token in '0123456789':
            #一开始是字符型，需要用int()将其转换为整型
            operandstack.push(int(token))
        else:
            operandop2=operandstack.pop()
            operandop1=operandstack.pop()
            #这里前后顺序不能搞反了
            operandstack.push(domath(token,operandop1,operandop2))
    return operandstack.pop()

print(postfixEva1('7 8 + 3 2 + /'))

#3.4队列：只能在首端删除，末端添加，也就是先进先出的原则，FIFO

#列表表示队列，列表的首端表示队列的尾端，列表尾端表示队列首端
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
q=Queue()
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.items)

#3.4.4 队列的应用一：传土豆
def hotpotato(namelist,num):
    simqueue=Queue()
    #将名字放在队列中
    for name in namelist:
        #从列表首段也就是队列尾端插入元素
        simqueue.enqueue(name) 
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    
    return simqueue.dequeue()

namelist='zxcv'
print(hotpotato(namelist, 7))

#3.4.5 队列的应用二：打印任务

#打印机状态类
class printer:
    #ppm也就是每分钟打印多少页数
    def __init__(self,ppm):
        self.pagerate=ppm
        #目前是否有任务，一开始默认没有任务
        self.currenttask=None
        #一个任务还差几秒打印完
        self.timeRemaining=0
        
        #打印状态
    def trick(self):
        if self.currenttask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currenttask=None
                
    def busy(self):
        if self.currenttask!=None:
            return True
        else:
            return False
        
        #开始打印新任务
    def starnext(self,newtask):
        self.currenttask=newtask
        #记录总的打印时间
        self.timeRemaining=newtask.getPages()*60/self.pagerate

#创建一个任务
import random  
class Task:
    def __init__(self,time):
        #生成任务的时间
        self.timestamp=time
        #1-20中随机抽取一个数
        self.pages=random.randrange(1,21)
        
    def getstamep(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self,currenttime):
        #总的等待时间
        return currenttime-self.timestamp
    
#打印任务模拟程序
#numSeconds:总的打印时间，pagesPerMinute：每分钟打印页数

#是否生成新的打印作业，因打印任务也是随机的，所以需要随机生成
def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False
    
    
def simulation(numSeconds,pagesPerMinute):
    labprinter =printer(pagesPerMinute)
    printqueue=Queue()
    #记录每个任务的等待时间，最后计算平均等待时间
    waitingtimes=[]
    
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printqueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printqueue.isEmpty()):
            nexttask=printqueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.starnext(nexttask)
            
        labprinter.trick()
        
    averageWait=sum(waitingtimes)/len(waitingtimes)
    print('average wait %6.2f secs %3d tasks remaining.'%(averageWait,printqueue.size()))
        
    
for i in range(10):
    simulation(3600, 5)
    
for i in range(10):
    simulation(3600, 10)
    
#3.5双端队列：两端（即首端以及尾端）都可以添加、删除元素
#列表表示双端队列，列表首端为双端队列尾端，列表尾端为双端队列首端，此时，双边列表首端增删元素复杂度为O(1),在双边列表尾端增删元素复杂度为O(n)
#也可以列表首端作为双边队列的首端，但是这样复杂度就会变化，
class Deque:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def addFront(self,item):
        self.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)


#3.5.4 双端列表的应用：回文检测器：盘那段一串字符是否左右对称

def palchecker(astring):
    chardeque=Deque()
    stillequal=True
    #将字符中的元素从双端队列尾端加入双端队列中,，因为没有空格所以没办法勇.split()将其直接转变为列表，可以用一个循环来进行
    for string in astring:
        chardeque.addRear(string)
        
    #chardeque.size()>1包括了两种情况：字符个数为奇数或者偶数两种情况
    while chardeque.size()>1 and stillequal:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillequal=False
            
    return stillequal
            
print(palchecker('sdfds'))

#3。6 列表：列表是一个线性数据结构（对于一个数据项，其有唯一一个前端和后继），是无序列表（无序针对的是列表的元素没有孙顺序）。
#列表有第一个元素、第二个元素等等，第一个元素成为列表的起点，最后一个元素称为列表的终点

#3.6.2实现无序列表：链表

#1node类：节点：(1) 数据变量，即列表元素 （2） 下一个节点的引用

class node:
    def __init__(self,initdata):
        self.data=initdata
        self.next =None
     
    #获取当前节点数据变量
    def getdata(self):
        return self.data
    
    #获取当前该节点对下一个结点的引用
    def getnext(self):
        return self.next
    
    #建立一个新的节点的数据变量
    def setdata(self,newdata):
        self.data=newdata
        
    #建立的新节点newnext到下一个节点的引用
    def setnext(self,newnext):
        self.next=newnext
      
temp=node(93)
print(temp.getdata())

class n:
    def __init__(self):
        self.d=3
    def f(self,k):
        self.d=k



#节点类的理解

# 链表实现
class Node():
    def __init__(self, item): # 初始化
        self.item = item
        self.next = None  # 最初不存在
 
# 传入节点数据
a = Node(1) #类实例化为对象
b = Node(2)
c = Node(3)
 
# 创建链接
a.next = b # a的下一个是b
b.next = c # b的下一个是c
 
print(a.item) #输出为1
print(a.next.item)  # 输出为b点，2
print(a.next.next.item) # 输出为c点，3
print(b.item)
print(b.next.item) #输出为c点，3

#2 无序列表类

class unorderedlist:
    
    def __init__(self):
        #表示链表中没有节点,self.next表示一个指向，一开始为空表示没有指向
        self.head=None
        
    def isEmpty(self):
        #self.head=none表示列表中没有节点,也就是整个列表是空的
        return self.head==None
    
    #像链表中添加新元素
    def add(self,item):
        temp=node(item)
        temp.setnext(self.head)
        self.head=temp
        
    #计算列表的长度
    def length(self):
        count=0
        current=self.head
        while current!=None:
            count=count+1
            current=current.getnext()
            
        return count
    
    #查找元素是否在列表中
    def search(self,item):
        found=False
        #此时的current是一个node类的实例方法
        current=self.head
        #current!=None表示最后一个元素的指向是none
        #循环里的current是下一个结点的指向
        while current!=None and not found:
            if current.getdata()==item:
                found=True
            else:
                current=current.getnext()
        
        return found
    
    #remove(item)删除指定元素item
    def remove(self,item):
        found =False
        #记录之前的指向
        previous=None
        #根据add实例方法的定义可知这是个节点node类
        current=self.head
        
        while current!=None and not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getnext()
            
        #考虑想要删除的元素在第一个位置,直接让self.head指向第二个节点即可
        if previous==None:
            self.head=current.getnext()
        else:
            previous.setnext(current.getnext())
        
    
   
        
        
        
        
List=unorderedlist()

#list.remove(3)
List.add(5)
List.add(44)
List.add(21)
List.remove(5)
print(List.head.getnext()==None)
#print(List.append(90))
print(List.length())
print(List.search(44))
        
                
#3.6.3 有序列表的抽象数据类型:也就是列表元素是有顺序的（前提：排序具有意义）
#有序列表与无序列表的构造方式相同，通过链表实现。但有些实例方法需要做些修改
#一下都是考虑的升序排列的有序 列表
class orderedlist:
     
    def __init__(self):
         #表示链表中没有节点,self.next表示一个指向，一开始为空表示没有指向
        self.head=None
         
    def isEmpty(self):
        #self.head=none表示列表中没有节点,也就是整个列表是空的
        return self.head==None
     
     #像链表中添加新元素，但因为是有序的那么需要判断
    def add(self,item):
        current=self.head
        previous=None
        temp=node(item)  
        stop = False
        while current!=None and not stop:
            if current.getdata()>item:
                stop =True
            else:
                previous=current
                current=current.getnext()
        
        if previous==None:
            
             #理解成self.head也是个指针，其指向第一个元素，。setnext就是让temp指向第一个元素
            temp.setnext(self.head)
            self.head=temp
        else:
            temp.setnext(current)
            previous.setnext(temp)
        
       
                    
         
         
     #计算列表的长度
    def length(self):
        count=0
        current=self.head
        while current!=None:
            count=count+1
            current=current.getnext()
             
        return count
     
     #查找元素是否在列表中，因为是有序的，所以不用全部查找
    def search(self,item):
        found=False
          #此时的current是一个node类的实例方法
        current=self.head
        stop=False
         #current!=None表示最后一个元素的指向是none
         #循环里的current是下一个结点的指向
        while current!=None and not found and not stop:
            if current.getdata()==item:
                found=True
            else:
                if current.getdata>item:
                    stop=True
                else:
                    current=current.getnext()
        return found
     
     #remove(item)删除指定元素item
    def remove(self,item):
        found =False
         #记录之前的指向
        previous=None
         #根据add实例方法的定义可知这是个节点node类
        current=self.head
         
        while current!=None and not found:
            if current.getdata()==item:
                found=True
            else:
                previous=current
                current=current.getnext()
        if previous==None:
            
            self.head=current.getnext()
        else:
            
            previous.setnext(current.getnext())
             
     #考虑想要删除的元素在第一个位置,直接让self.head指向第二个节点即可
     
             
mylist=orderedlist()
mylist.add(45)
mylist.add(36)
mylist.add(12)
print(mylist.length())
mylist.add(89)
print(mylist)

#3。7总结：线性数据结构：栈，队列，双端队列，无序列表，有序列表
#链表保证逻辑顺序，对实际的储存顺序没有要求，修改链表头部是一种特殊情况

                    
    
    