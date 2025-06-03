# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 15:20:06 2023

@author: 23665
"""
#进制转换
def tostr(n,base):
    converstring='0123456789ABCDEF'
    if n<base:
        return converstring[n]
    else:
        return tostr(n//base,base)+converstring[n%base]


#4.10 讨论题
#1 汉诺塔问题的调用栈
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
    
def moveTower(height,fromtower,totower,withtower):
    fromslack=Slack()
    withslack=Slack()
    toslack=Slack()
    for i in range(height):
        fromslack.push(i+1)
    if height>=1:
        moveTower(height-1, fromtower, withtower, totower)
        movedisk(fromtower,totower)
        moveTower(height-1, withtower, totower, fromtower)
    
    
def movedisk(fp,tp):
    print('moving disk from',fp,'to',tp)
    
#print(moveTower(4,'#1','#2','#3'))

#4.11 编程练习
#1 计算数的阶乘
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    elif n==1:
        return 1
#print(factorial(4))

#2 写出递归函数来反转列表
#lr是个列表，其长度newlist长度相同用来存储反转结果

#在递归的时候常用到全局变量，小技巧
lr=[]
def reverselist(newlist):
    #lr是个全局变量，会一直变化，如果直接在函数里面写lr=[]，那么lr在每次循环的时候会变为[],无法实现要求
    global lr
    if len(newlist)>=2:
        lr.insert(0,newlist[0])
        return reverselist(newlist[1:])
    else:
        lr.insert(0,newlist[0])
        return newlist[0]
        
reverselist([1,2,3,4,5,6,True])
#print(lr)

# 5写一个递归函数来计算斐波那契数列，并且对比递归函数与循环函数的性能
import time
def Fibonaccisequence(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonaccisequence(n-1)+Fibonaccisequence(n-2)
print(Fibonaccisequence(3))

#循环函数实现
import timeit
def cycleFibonaccisequence(n):
    result=[0]*(n+1)
    result[0]=0
    result[1]=1
    for i in range(2,n+1):
        result[i]=result[i-1]+result[i-2]
    return result[n]
print(cycleFibonaccisequence(3))

def performantFibonacci():
    for i in range(40, 60):
        t = timeit.Timer("Fibonaccisequence(%d)" % i, 
            "from __main__ import Fibonaccisequence")
        recursion_time = t.timeit(number = 1000)
        t = timeit.Timer("cycleFibonaccisequence(%d)" % i, "from __main__ import cycleFibonaccisequence")
        itea_time = t.timeit(number = 1000)
        print("%d, %10.3f, %10.3f" % (i, recursion_time, itea_time))
        
performantFibonacci()

#6 实现汉诺塔问题的一个解决方案，用三个栈记录盘子的位置
from turtle import *
from chapter3基本数据结构 import Slack
def moveTower(plates, poles, height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(plates, poles, height - 1, fromPole, withPole, toPole)
        moveDisk(plates, poles, fromPole, toPole)
        moveTower(plates, poles, height - 1, withPole, toPole, fromPole)


def moveDisk(plates, poles, fp, tp):
    mov = poles[fp].peek()
    plates[mov].goto((fp - 1) * 400, 300)
    plates[mov].goto((tp - 1) * 400, 300)
    l = poles[tp].size()
    plates[mov].goto((tp - 1) * 400, -90 + 20 * l)
    poles[tp].push(poles[fp].pop())
    print("moveing disk from %d to %d\n" % (fp, tp))


def drawpoles():
    myTurtle = Turtle()
    myTurtle.hideturtle()

    def drawpole(i):
        myTurtle.up()
        myTurtle.pensize(10)
        myTurtle.speed(100)
        myTurtle.goto(400 * (i - 1), 300)
        myTurtle.down()
        myTurtle.goto(400 * (i - 1), -100)
        myTurtle.goto(400 * (i - 1) - 20, -100)
        myTurtle.goto(400 * (i - 1) + 20, -100)

    drawpole(0)
    drawpole(1)
    drawpole(2)


def create_plates(n):
    plates = [Turtle() for _ in range(n)]
    for i in range(n):
        plates[i].up()
        plates[i].hideturtle()
        plates[i].shape('square')
        plates[i].shapesize(1, 20 - i)
        plates[i].goto(-400, -90 + 20 * i)
        plates[i].showturtle()
    return plates


def polestack():
    return [Slack() for _ in range(3)]


def moveTowertest():
    turtle=Turtle
    #myWin = turtle.getscreen()
    drawpoles()

    n = int(input("请输入汉诺塔的层数并回车确定:\n"))
    plates = create_plates(n)
    poles = polestack()
    for i in range(n):
        poles[0].push(i)
    moveTower(plates, poles, n, 0, 2, 1)
    #myWin.exitonclick()


moveTowertest()

#7 希尔伯特曲线
from turtle import *

def turn_direction(myTurtle, d):
    if d == 1:
        myTurtle.right(90)
    elif d == -1:
        myTurtle.left(90)


# 每第三次前进的前后需要转向
# 使用类是为了不共享direction值
class Direct():
    direction = 1
    count = 1
    length = 12

    def direct3(self, myTurtle):
        turn_direction(myTurtle, self.direction)
        myTurtle.forward(self.length)
        turn_direction(myTurtle, self.direction)
        if self.count % 2 == 1:
            self.direction *= -1
        self.count += 1


direct_list = []


def helbert(myTurtle, depth):
    length = 12
    for i in range(1, 10):
        if depth > 1:
            helbert(myTurtle, depth - 1)
        if i % 3 == 0 and i != 9:
            direct_list[depth - 1].direct3(myTurtle)
        elif i == 9:
            break
        else:
            myTurtle.forward(length)


def drawhelbert():

    myTurtle = Turtle()
    myTurtle.left(90)
    myWin = myTurtle.getscreen()
    depth = 3
    for _ in range(depth):
        direct_list.append(Direct())
    helbert(myTurtle, depth)
    myWin.exitonclick()

#drawhelbert()

#8 科赫雪花
from turtle import *
def koch(myTurtle, len, n):
    if n == 0:
        myTurtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            myTurtle.left(i)
            koch(myTurtle, len / 3, n - 1)


def drwakoch():
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()
    length = 500
    level = 3
    koch(myTurtle, length, level)
    myTurtle.right(120)
    koch(myTurtle, length, level)
    myTurtle.right(120)
    koch(myTurtle, length, level)
    myTurtle.right(120)
    myWin.exitonclick()

drwakoch()


#9 有2个坛子，其中一个容量是4加仑，另一个3加仑。坛子上都没有刻度线。可以用水泵将他们装满水。如何使4加仑的坛子最后装有2加仑的水
def gettarget(bottle1, bottle2, a, b, target):
    for _ in range(b):
        bottle2.push('water')
    print(f'bottle1:{bottle1.size()}')
    print(f'bottle2:{bottle2.size()}')
    for _ in range(a):
        bottle1.push(bottle2.pop())
    print(f'bottle1:{bottle1.size()}')
    print(f'bottle2:{bottle2.size()}')   
    if bottle2.size() != target:
        for _ in range(a):
            bottle1.pop()  
        print(f'bottle1:{bottle1.size()}')
        print(f'bottle2:{bottle2.size()}')
        bottle1.push(bottle2.pop())
        return gettarget(bottle1, bottle2, 2 * a - b, b, target)
    else:
        return 'complete'
 
def getwater():
    bottle1 = Stack()
    bottle2 = Stack()
    gettarget(bottle1, bottle2, 3, 4, 2)
    
    
#14 背包问题
def bag(maximumcapacity):
    # 使用列表表示艺术品相关的价值，列表中元素是字典，因为艺术品有重量和价值两个参数，所为了方便以可以用字典分别艺术品的两个参数,
    # w是重量，v是价值
    art = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]
    # 用字典表示书中的表格，是个二维表,字典得键是元组
    m = {(i, w): 0 for i in range(len(art)) for w in range(maximumcapacity + 1)}
    for i in range(1, len(art)):
        for w in range(1, maximumcapacity + 1):
            if art[i]['w'] > w:  # 装不下第i个宝物
                m[(i, w)] = m[(i - 1, w)]
            else:
                # 不装第i个宝物装第i个宝物，两种情况下最大价值
                m[(i, w)] = max(m[(i - 1, w)], m[(i - 1, w - art[i]['w'])]+ art[i]['v'])

    return m[(len(art) - 1, maximumcapacity)]


print(bag(20))

           
        