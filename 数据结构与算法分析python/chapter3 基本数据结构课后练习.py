# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:47:46 2023

@author: 23665
"""
#慕课课后练习

#1. 慕课第三周作业：有效的括号
#先定义栈
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

def matches(open,close):
    opens='{[('
    closers='}])'
    #字符串也可以通过index访问指定字符的索引
    return opens.index(open)==closers.index(close)
print(matches('{','}'))





    
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
print(parChecker1('([])'))
          
#2,慕课第三周作业一维开心消消乐 (耗时2小时呵呵)
#开心消消乐我们都熟悉，我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，这个游戏输入一串字符，逐个消去相邻的相同字符对。
#如果字符全部被消完，则输出不带引号的“None”
#思路：与有效括号的思路是一致的

def Entertainment(astring):
    s=Slack()
    index=0
    while index<len(astring)-1:
        s.push(astring[index])
        k=1
        while (s.peek()==astring[index+k]) and (k<len(astring)-index):
            s.pop()
            k=k+1
        index=index+k
    if s.peek()==astring[len(astring)-1]:
        s.pop()
    else:
        s.push(astring[len(astring)-1])
            
    if s.isEmpty():
        return None
    else:
        str1=''
        while not s.isEmpty():
            str1=str1+str(s.pop())
            
        list1=list(str1)
        list1.reverse()
        
        
        return ''.join(list1)
    
print(Entertainment('beepooxxxyz'))
       
#3 第三周慕课作业：洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。

#小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。

#老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。

#你也能像老王一样作出准确的判断吗？

'''
思路：输入序列1043257689 和 4321078965 都将输出为Yes
使用栈来存取、比较
拿走的盘子号码数number：
	1、大于上一个拿走的盘子号(即栈顶号码peak)，则将其压入栈中。
	2、小于peak，number应为比peak小且离peak最近的没拿走过的盘子号。比如序列”4321078965“中的96。


class Stack:
	def init(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self)
		return self.items.pop()
	def peak(self):
		return self.items[-1]
		
def wash(string):
	sequence=[0,1,2,3,4,5,6,7,8,9]   #记录盘子是否被拿走，拿走几号则将几号置为None
	found=True   #记录是否按顺序洗碗
	s=Stack()
	index=0
	while index<len(string) and found:
		number=int(string[index])#取盘子的顺序
		if s.isEmpty():    #栈为空，将第一个拿走的盘子压入栈中
			s.push(number)
			sequence[number]=None     #将拿走number号设置为None
		else:       #栈不为空
			peak=int(s.peak())   #得到栈顶号，在取栈顶号之前需要判断是否为空
			if number<peak:     #拿走的盘子号码数number小于peak
				while number!=peak-1 and found:   #判断number是否为比peak小且离peak最近的没拿走过的盘子号
					if sequence[peak-1]==None:
						peak=peak-1
					else:
						found=False
				s.push(number)     # 是，则压入栈，并将其设置为None
				sequence[int(number)]=None
			else:        # 拿走的盘子号码数number大于peak
				s.push(number)
				sequence[int(number)]=None
		index=index+1
	if found==True:
		return "Yes"
	else:
		return "No"
			
string=input()
print(wash(string))
'''
#3.10 编程练习
#1
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
    
    try:
        for token in tokenList:
            if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
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
    
    except:
        return '中序表达式错误'
       


#别忘记加空格哦

print(infixToPostfix("( A + B ) * ( C + D )"))

print(infixToPostfix("( A + B) * ( C + D )"))

#2修改后续表达式的算法使得其能处理异常情况
#只能计算0-9个位数的计算，对于二位，三位等都不可以哦
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
    try:
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
    except:
        return '中序表达式错误'

print(postfixEva1('7 8 + 3 2 + /'))

#3. 实现中序表达式的计算
#使用两个栈，一个用于保存运算符，另一个用于保存操作数

#方法一：
def infixEva2(infixexpr):
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
    PostfixList=Slack()
    
    #按空格将字符串分开，将分开后的结果放在列表中，结果是列表
    tokenList=infixexpr.split()
    
    for token in tokenList:
        if token in '0123456789':
            PostfixList.push(int(token))
           #包含所有大写字母字符串，也可以勇'ABCDEFGHIJKLMNOPQISTUVWXYZ'
        elif token=='(':
            opstack.push(token)
        elif token==")":
            toptoken=opstack.pop()
            while toptoken!='(':
                #修改这里即可
                first2=PostfixList.pop()
                first1=PostfixList.pop()
                PostfixList.push(domath(toptoken, first1, first2))
                toptoken=opstack.pop()
                
        else:
            #下面别忘记加括号，当判别式比较复杂的时候需要加上括号
            while (not opstack.isEmpty()) and (prec[opstack.peek()]>=prec[token]):
                #修改这里即可
                first2=PostfixList.pop()
                first1=PostfixList.pop()
                do=opstack.pop()
                PostfixList.push(domath(do, first1, first2))
                
                 
            opstack.push(token)
        
        #最后可能还剩一些运算符按照优先级从低到高排序的运算符，那么需要将其放入结果中
    while not opstack.isEmpty():
        #修改这里即可
        first2=PostfixList.pop()
        first1=PostfixList.pop()
        do=opstack.pop()
        PostfixList.push(domath(do, first1, first2))
         
#
            
        #是个字符串，将列表表中的元素用空格相连接，用个空格分开 str.split(),用空格链接列表中的元素' '.join(list),结果是字符串
    return PostfixList.pop()
    
print(infixEva2("( ( ( 1 + 2 ) * 3 ) - ( 4 + 5 + 6 - 7 ) ) * 8"))
print(infixEva2('( 1 + 2 ) + 3 * 4'))

#方法二：
def infixEval(infixExpr):
    opStack = Stack()
    signStack = Stack()
    tokenList = infixExpr.split()
    
    for token in tokenList:
        if token in ['+', '-', '*', '/', '(', ')']:
            if token == ')':
                while signStack.peek() != '(':
                    operatenum2 = opStack.pop()
                    signlabel = signStack.pop()
                    operatenum1 = opStack.pop()
                    res = domath(signlabel, operatenum1, operatenum2)
                    opStack.push(res)
                signStack.pop()
            else:
                signStack.push(token)
        else:
            opStack.push(int(token))
 
    while not signStack.isEmpty():
        operatenum2 = opStack.pop()
        signlabel = signStack.pop()
        operatenum1 = opStack.pop()
        res = domath(signlabel, operatenum1, operatenum2)
        opStack.push(res)
 
    return opStack.pop()          

#5. 使用列表实现队列抽象数据类型，将列表的后端作为尾部
class Queue1:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        return self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    
#6 两种实验增加，删除元素的时间复杂度正好相反
#9. 修改模拟传土豆的程序，润许随机计数，从而使得每一轮的结果都不可预测

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
import random
def hotpotato(namelist):
    num=random.randrange(0,10000)
    queue=Queue()
    for token in namelist:
        queue.enqueue(token)
        
    while queue.size()>1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()
print(hotpotato('zcxs'))

#10. 实现基数排序器：也就是比较整数的大小

#总体的思想：
#1）将所有比较的数值（正整数）统一为相同的数位长度，数位较短的前面补零
#2）从最低位开始，依次进行一次排序
#3）这样从最低位排序一直到最高位，完成以后，数列就变成了有序数列

#输入：一个包含想要比较的整数的列表，比如：[23,12,311]
#输出：比较的排序

def radix_sort(string)->list:
    main=Queue()
    for n in string:
        #将s中的元素放在队列里面
        main.enqueue(n)
    #寻找最大的数以及它的位数
    
    #先将列表中的元素转变为字符\
    '''
    for i in range(len(s)):
        s[i]=str(s[i])
    #用零填充至长度相同
    for i in range(len(s)):
        while len(s[i])!=d:
            s[i]='0'+s[i]  

    #将列表中的内容放入队列  
    '''
    
    #准备10个队列,_表示占位符
    nums=[Queue() for _ in range(10)]
    #前面补充0的模板，比如%%输出为一个百分号%，如果d是5，那么为%05d,这里d是最大数的位数
    d=len(str(max(string)))
    dstr='%%0%dd' % d
    for i in range(-1,-d-1,-1):
        while not main.isEmpty():
            a=main.dequeue()
            #int对象不可以作为下标
            dn=(dstr % a)[i]#转换成类似"00345"[-2],这是倒数第二位
            #dn=int(a[i])
            nums[int(dn)].enqueue(a)
        
        for k in range(10):
            while not nums[k].isEmpty():
                main.enqueue(nums[k].dequeue())
        
    result=[]
    while not main.isEmpty():
        result.append(main.dequeue())
        
    return result
            
print(radix_sort([666, 1, 24, 3, 67, 9, 45]))    
            

#11. 实现HTML中的括号匹配问题

def HTMLMatch(s)->bool:
    #判断是否开标记，即判断是否为</head>
    def isOpenTag(tag):
        return tag[1]!='/'
    #判断两个是否配对，replace(old,new),用新的取代原来的符号，也就是说判断是否为<head> </head>
    def matches(open,close):
        return open==close.replace('/','')
    
    #从i位置“<”开始找到一个标记，实例方法输出是<tag>或者</tag>
    #输入的s是<,返回的是<head>，</head>这样的结果
    def getTag(s,i):
        t=''
        while s[i]!='>':
           t+=s[i]
           i+=1
        t+='>'
        #返回标记和结束的位置
        return t,i
    st=Slack()
    balanced=True
    index=0
    while index<len(s) and balanced:
        symbol=s[index]
        if symbol=='<':
            tag,index=getTag((s), index)
        if isOpenTag(tag):
            st.push(tag)
        else:
            if st.isEmpty():
                balanced=False
            else:
                top=st.pop()
                if not matches(top,tag):
                    balanced=False
        #忽略所有非标记内容
        while index<len(s) and s[index]!='<':
            index+=1
    if balanced and st.isEmpty():
        return True
    else:
        return False
                        
print(HTMLMatch('<html><head>dhgs</head></html>'))

#12. 扩展回文检测器，使得其可以处理包含空格的回文

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

        
def palchecker(astring):
    s=''
    for n in astring:
        if n !=' ':
            s=s+n
    astring=s
    chardeqeue=Deque()
    for ch in astring:
        chardeqeue.addRear(ch)
    stillEqual=True
    while chardeqeue.size()>1 and stillEqual:
        first=chardeqeue.removeFront()
        last=chardeqeue.removeRear()
        if first!=last:
            stillEqual=False
    
    return stillEqual

print(palchecker('sdf d s'))

#14 实现列表中的renmove方法，使得其能正确处理要移除的元素不在列表中的情况
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
        
class unorderedlist:
    
    def __init__(self):
        #表示链表中没有节点,self.next表示一个指向，一开始为空表示没有指向
        self.head=None
    def __str__(self):
        current=self.head
        a='['
        a=a+str(current.getdata())
        current=current.getnext()
        while current!=None:
            a=a+' '+str(current.getdata())
            current=current.getnext()
        a=a+']'
        return a
    
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
        if not found:
            print('要移除的元素不在列表中')
        else:
            #考虑想要删除的元素在第一个位置,直接让self.head指向第二个节点即可
            if previous==None:
                self.head=current.getnext()
            else:
                previous.setnext(current.getnext())
        
        
    def append(self,item):
        current=self.head
        previous=None
        while current!=None:
        
            previous=current
            current=current.getnext()
    #在循环结束后，current=None，也就是最后一个节点指向的None,
    #previous才是最后一个节点
            
        temp=node(item)
        previous.setnext(temp)
        
    def index(self,item):
        count=0
        current=self.head
        find=False
        while current!=None and not find:
            if current.getdata()!=item:
                count=count+1
                current=current.getnext()
            else:
                find=True
        return count
    #删除指定位置的元素
    def pop(self,index):
        current=self.head
        previous=None
        if index==0:
            self.head=current.getnext()
        else:
            for _ in range(index):
                previous=current
                current=current.getnext()
            previous.setnext(current.getnext())
    #在指定位置插入元素item
    def insert(self,index,item):
        current=self.head
        previous=None
        if index==0:
            temp=node(item)
            temp.setnext(self.head)
            self.head=temp
        else:
            temp=node(item)
            for _ in range(index):
                previous=current
                current=current.getnext()
                
            previous.setnext(temp)
            temp.setnext(current)
    #19. 实现列表的切片功能，返回从start 开始到stop位置结束的新列表（不包括stop位置）
    def slice(self,start,stop):
        current=self.head
        previous=None
        if start==0:
            for _ in range(stop):
                previous=current
                current=current.getnext()
            previous.setnext(None)
        else:
            #有错误哦
            #需要从第一开始一个的删除
            for _ in range(start):
                current=current.getnext()
            self.head=current
                
                
            
            current =self.head
            for _ in range(stop-start):
                previous=current
                current=current.getnext()
            previous.setnext(None)
        
        
        
            
        
        
            
    
List=unorderedlist()
List.add(5)
List.add(44)
List.add(21)

List.append(7)
print(List.index(7))
print(List)
List.pop(0)
print(List)
List.insert(2,89)
print(List)
List.slice(1,3)
print(List)
print(List.length())

#16. 实现列表的链表类中的__str__方法。列表适合用什么养的字符串表示
#17. 修改__str__方法，使得按照python的方式来表示
#18
#19
#以上答案都在14题的答案中
#首先介绍__str__方法
#当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
#__str__方法需要返回一个字符串，当做这个对象的描写
class a:
    def __init__(self,m):
        self.data=m
    def __str__(self):
        #想要在return中输出字符串，并且带有变量，那么需要加上f'{}'
        return f'这个数据是{self.data}'
s=a(2)
print(s)


#18. 实现无序列表剩余方法：append,index,pop ,insert

    #def index(self,item):
        
#21. 有序列表与无序列表的关系。能否利用继承关系来构造更高的实现？试着写一下继承结构
#因为无序列表的append,pop,insert,remove,length ,empty与有序列表的实现是一样的
#所以直接继承即可，只需要自己写add，search方法即可
class orderedList(unorderedlist):
    def __init__(self):
        #表示继承父类的实例方法__init__
        super().__init__()
    def add(self,item):
        current=self.head
        
        previous=None
        stop=False
        
        while current!=None and not stop:
            if current.getdata()>item:
                stop=True
            else:
                previous=current
                current=current.getnext()
        temp=node(item)
        if previous==None:
            temp.setnext(self.head)
            self.head=temp
        else:
            previous.setnext(temp)
            temp.setnext(current)
    def search(self,item):
        #该方法包括列表中没有item的情况
        current=self.head
        found=False
        stop=False
        while current!=None and not found and not stop:
            if current.getdata()==item:
                found=True
            else:
                if current.getdata()>item:
                    stop=true
                else:
                    current=current.getnext()
        
        return found
    

def OrderedFromUnorederedlisttest():
    ol = orderedList()
    ol.add(67)
    ol.add(35)
    ol.add(97)
    ol.add(22)
    print(ol)
    print(ol.index(97))
    print

print(OrderedFromUnorederedlisttest())
#22，23 用链表实现栈和队列
#链表实现栈
class LinkStack():
    def __init__(self):
        self.head=None
        self.length=0 
        
    def isEmpty(self):
        return self.length
    def size(self):
        return self.length
    def peek(self):
        return self.head.getdata()
    def push(self,item):
        top=node(item)
        top.setnext(self.head)
        self.head=top
        self.length+=1
        
    def pop(self):
        top_item=self.head.getdata()
        self.head=self.head.getnext()
        self.length-=1
        return top_item

#链表实现队列
class LinkQueue():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def isEmpty(self):
        return self.head==None
    
    def size(self):
        return self.length
    
    def enqueue(self,item):
        tail=node(item)
        if self.head==None:
            self.head=self.tail=tail
        else:
            self.tail.setnext(tail)
            self.tail=self.tail.getnext()
        self.length+=1
    
    def deqeue(self):
        top_item=self.head.getdata()
        if self.head==self.tail:
            self.head=self.tail=None
        else:
            self.head=self.head.getnext()
        self.length-=1
        return top_item
        
    
    


#27. 实现双向链表:双向链表的节点有：列表元素（数据变量），指向下一个结点的引用，指向前一个结点的引用



class node1:
    def __init__(self,item):
        self.data=item
        self.pre=None
        self.next=None
    def getdata(self):
        return self.data
    def getpre(self):
        return self.pre
    def getnext(self):
        return self.next
    def setdata(self,data1):
        self.data=data1
        
    def setpre(self,pre1):
        self.pre=pre1
    def setnext(self,next1):
        self.next=next1

#双向链表的实现，比单向链表多了一self.tail
class DoublyLinkedlist:
    def __init__(self,it=None):
        self.head=None
        self.tail=None
        self.length=0
        if it !=None:
            for d in it:
                #后面append已经定义
                self.append(d)
        
    def isEmpty(self):
        return self.head==None
    
    def size(self):
        return self.length
    __len__=size
    
    def getTail(self):
        return self.tail
    #从第一个位置上面添加元素
    def add(self,item):
        idx0=node1(item)
        #如果是第一个添加的元素
        if self.head==None:
            self.head=self.tail=idx0
        else:
            self.head.setpre(idx0)
            idx0.setnext(self.head)
            self.head=idx0
        self.length+1 
    
    #在最后一个位置添加元素
    def append(self,item):
        temp=node1(item)
        if self.head==None:
            self.head=self.tail=temp
        else:
            self.tail.setnext(temp)
            temp.setpre(sel.tail)
            self.tail=temp
        self.length+=1
     #在指定位置插入元素
     def insert(self,index,item):
         current=self.head
         n=0
         #最后的列表的下标从1开始
         while n<index
             current=current.getnext()
             n=n+1
        #因为在当链表是空和在链表的尾部添加元素与在中间添加元素的不一样的，所以要分开讨论
        #而current==None正好包括了上面两种情况
        #current==None只有两种情况，1）链表为空，也就是self.head=None 
        #2）在链表的尾部，也就是self.tail==None
        if current==None:
            if self.head==None:
                #调用类本身的实例方法，在列表的头部添加元素
                self.add(item)
            else:
                #在列表的尾部添加元素
                self.append(item)
        else:
            temp=node1(item)
            temp.setnext(current)
            temp.setpre(current.getpre())
            #需要判断temp是否在第一个位置添加，其需要单独讨论
            if temp.getpre()!=None:
                temp.getpre().setnext(temp)
            current.setpre(temp)
        sel.length+=1 
        
    def index(self,item):
        current=self.head
        count=0
        found=False
        while current!=None and not found:
            if current.getdata()!=item:
               current=current.getnext()
               count+=1 
            else:
                found=True
        return n
    def search(self,index):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getdata()!=item:
               current=current.getnext()
            else:
                found=True
        return found
    
    #删除current所引用的所有节点
    def delete(self,current):
        #删除本节点
        if self.head==current:
            #删除了第一个节点
            self.head=current.getnext()
        if self.tail==current:
            #删除了最后一个节点
            self.tail=current.getpre()
        if current.getpre() !=None:
            current.getpre().setnext(current.getnext())
        if current.getnext()!=None:
            current.getnext().setpre()
        self.length-=1
    def remove(sself,item):
        current=self.head 
        while current !=None:
            if current.getdata()==item:
                self.delete(currrent)
                break
            current=current.getnext()
    
    def remove(self,item):
        current=self.head
        while current.getdata()==item:
            self.delete(current)
            break
        current=current.getnext()
    def pop(self,n=None):
        if n ==None:
            n=self.length-1
        current=self.head
        i=0
        while i<n:
            current=current.getnext()
            i+=1
        dat=current.getdata()
        self.delete(current)
        return dat
    def __str__(self):
        tlist=[]
        current=self.head
        while current !=None:
            tlist.append(current.getdata())
            current=current.getnext()
        return str(tlist)
    __repr__=__str__            
    
    

#寻找最大的数以及它的位数

#先将列表中的元素转变为字符\

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
string=[21,234,1]
main=Queue()
for n in string:
    #将s中的元素放在队列里面
    main.enqueue(n)
#前面补充0的模板，比如%%输出为一个百分号%，如果d是5，那么为%05d,这里d是最大数的位数

d=len(str(max(string)))
dstr='%%0%dd' % d
n=string[0]
print((dstr % n)[-3])
print(d)
#准备10个队列,_表示占位符
nums=[Queue() for _ in range(10)]


for i in range(-1,-d-1,-1):
    while not main.isEmpty():
        a=main.dequeue()
        #int对象不可以作为下标
        dn=(dstr % a)[i]#转换成类似"00345"[-2],这是倒数第二位
        #dn=int(a[i])
        nums[int(dn)].enqueue(a)
    
    for k in range(10):
        while not nums[k].isEmpty():
            main.enqueue(nums[k].dequeue())
    
result=[]
while not main.isEmpty():
    result.append(main.dequeue())
    
print(result)
    
        