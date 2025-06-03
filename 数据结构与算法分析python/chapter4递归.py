# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 19:31:36 2023

@author: 23665
"""


#4.2。1什么是递归

#4.2.1计算列表中所有数之和
#方法一：采用循环实现
def listsum(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum
#方法二：采用递归实现
#递归三要素：
#1)基本结束条件
#2）每一次都要想着基本结束条件减少问题规模
#3）要递归调用自身
def listsum1(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0]+listsum(list[1:])
    
print(listsum([1,23,3]))
print(listsum1([1,23,3]))

#4.2.3 将整数转变为任意进制的字符串

#采用递归的形式将字符串转变为2~16进制的字符串
def tostr(n,base):
    converstring='0123456789ABCDEF'

    if n<base:
        return converstring[n]
    else:
        return tostr(n//base,base)+converstring[n%base]
    
#print(tostr(123,2))

#4.3 栈帧：实现递归
#将字符串压入栈中，并且采用递归形式,通过栈来保存结果
import chapter3基本数据结构
rstack=chapter3基本数据结构.Slack()
def tostr1(n,base):
    converstring='0123456789ABCDEF'
    if n<base:
        rstack.push(n)
    else:
        rstack.push(n%base)
        tostr1(n//base,base)
tostr1(123,2) 
while not rstack.isEmpty():       
    print(rstack.pop(),end='')


from turtle import *
myTurtle =Turtle()
myWin=myTurtle.getscreen()

def drawSpiral(myTurtle,linlen):
    if linlen>0:
        myTurtle.forward(linlen)
        myTurtle.right(90)
        drawSpiral(myTurtle,linlen-5)
        
#drawSpiral(myTurtle, 100)
myWin.exitonclick()

    
def tree(branchlen,t):
    if branchlen>5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        tree(banchlen-10,t)
        t.right(20)
        t.backward(branchlen)
from turtle import *      
t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()
    
#4.4 递归可视化
#绘制树


def tree(branchlen,t):
    if branchlen>5:
        t.forward(branchlen)
        t.right(20)
        tree(branchlen-15,t)
        t.left(40)
        tree(branchlen-10,t)
        t.right(20)
        t.backward(branchlen)
from turtle import *
t=Turtle()
myWin=t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.color('green')
tree(110,t)
myWin.exitonclick()

# 谢尔平斯基三角形
from turtle import *
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()
def getMid(p1,p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1,myTurtle)
        sierpinski([points[1],getMid(points[0],points[1]),getMid(points[1],points[2])],degree-1,myTurtle)
        sierpinski([points[2],getMid(points[2],points[1]),getMid(points[0],points[2])],degree-1,myTurtle)
myTurtle =Turtle()
myWin=myTurtle.getscreen()
mypoints=[(-500,-250),(0,500),(500,-250)]
sierpinski(mypoints,5,myTurtle)
myWin.exitonclick()


#4.5 复杂的递归问题

#三个汉诺塔问题
#1）先将高度height-1的一叠盘子从起始位置经过终点位置转移到中间位置
#2）再将最后一个盘子移到终点位置
#3）将高度为height-1的一叠盘子从中间位置经过起始位置移动到终点位置

def moveTower(height,frompole,topole,withpole):
    if height>=1:
        moveTower(height-1,frompole,withpole,topole)
        moveDisk(frompole,topole)
        moveTower(height-1, withpole, topole, frompole)
def moveDisk(fp,tp):
    print("moving disk from",fp,'to',tp)
    
moveTower(5,'#1','#2','#3')
'''
'''
#4.6 探索迷宫
from turtle import *
#maze类用于读入数据文件
class maze:
    def __init__(self,mazeFileName):
        self.mazelist=[]#记录地图
        rowsInMaze=0
        columnsInMaze=0
        mazeFile=open(mazeFileName , 'r')
        for line in mazeFile:
            rowlist=[]
            col=0
            #这样会丢失最后一列
            #for ch in line[:-1]:
            for ch in line:
                rowlist.append(ch)
                if ch=='S':
                    self.startRow=rowsInMaze
                    # 记录起始位置
                    self.startCol=col
                    # 因为每一行都会会让col=0，那么就会记录列
                col=col+1
            rowsInMaze=rowsInMaze+1
            self.mazelist.append(rowlist)
            columnsInMaze=len(rowlist)
        
        self.rowsInMaze=rowsInMaze
        self.columnsInMaze=columnsInMaze
        #迷宫中间位置的（0，0）的坐标
        self.xTranslate=-columnsInMaze/2#设置迷宫左上角的初始x的坐标
        self.yTranslate=rowsInMaze/2 #设置迷宫左上角的初始y的坐标
        self.t=Turtle(shape='turtle')#设置形状为乌龟，默认的是箭头
        setup(width=600,height=600)
        setworldcoordinates(-(columnsInMaze-1)/2-0.5,-(rowsInMaze-1)/2-0.5,(columnsInMaze-1)/2+0.5,(rowsInMaze-1)/2+0.5)
    #在屏幕上绘制迷宫
    def drawmaze(self):
        self.t.speed(20) #绘制速度
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x]==OBSTACLE:#如果迷宫列表的位置为障碍物，那么画方块
                    self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'tan')
    
    #画方块
    def drawCenteredBox(self,x,y,color):
        tracer(0)
        self.t.up() #画笔抬起
        self.t.goto(x-0.5,y-0.5) #前往参数位置，，因为方块的四个角是值，此处0.5偏移量的作用是使乌龟的探索路线在单元格的正中心位置
        self.t.color('black',color)#方块填充的颜色
        self.t.setheading(90) #设置海归的朝向，标准模式：0 - 东，90 - 北，180 - 西，270 - 南。logo模式：0 - 北，90 - 东，180 - 南，270 - 西。
        self.t.down()#画笔落下
        self.t.begin_fill()#开始填充
        for i in range(4): #画方块边框
            self.t.forward(1)   #向前1各单位
            self.t.right(90)    #右转90度
        self.t.end_fill()       #结束填充
        tracer(1)
    #移动海龟
    def moveTurtle(self,x,y):
        self.t.up()   #画笔抬起
        # setheading()设置海龟朝向，towards()从海龟位置到由(x, y)，矢量或另一海龟位置连线的夹角。此数值依赖于海龟初始朝向，由"standard"、"world"或"logo" 模式设置所决定。
        self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
        self.t.goto(x+self.xTranslate,-y+self.yTranslate)
        
    def dropBreadcRumb(self,color):
        # dot(size=None, color)画路径圆点
        self.t.dot(color)
        
     # 用以更新迷宫内的状态及在窗口中改变海龟位置，行列参数为乌龟的初始坐标。
    def updatePosition(self,row,col,val=None):
        self.mazelist[row][col] = val  # 设置该标记状态为当前单元格的值
        self.moveTurtle(col, row)
        if val == PART_OF_PATH:  # 其中一条成功路径的圆点的颜色
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:  # 尝试用的圆点的颜色
            color = 'black'
        elif val == DEAD_END:  # 死胡同用的圆点的颜色
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)  # 画路径圆点并上色


    #判断是否为出口
    def isExit(self,row,col):
        return(row==0 or row==self.rowsInMaze-1 or col==0 or col==sel.columnsInMaze-1)
        
    #特殊的实例方法，可以直接 实例对象[key]来调用
    def __getitem__(self,key):
        return self.mazelist[key]

#搜索迷宫的函数
def searchFrom(maze,startRow,startColumn):
#从初始位置开始尝试四个方向，直到找到出路
    maze.updatePosition(startRow,startColumn)
    #1.检查基本情况
    #1. 遇到墙
    if maze[startRow][startColumn]==OBSTACLE:
        return False
    #2. 遇到已经走过的格子
    
    if maze[startRow][startColumn]==TRIED or maze[startRow][startColumn]==DEAD_END:
        return False
    
    #3. 找到出口
    if maze.isEmpty(startRow,startColumn):
        maze.updatePosition(startRow,startColumn,PART_OF_PATH)
        return True
    
    #否则，一次尝试四个方向移动
    #A orB 中or酷游短路特征，如果A是正确的，就不再执行B,返回True
    found=searchFrom(maze, startRow-1, startColumn) or\
        searchFrom(maze, startRow+1, startColumn) or\
            searchFrom(maze, startRow, startColumn+1) or\
                searchFrom(maze, startRow, startColumn-1)
    if found:
        maze.updatePosition(startRow,startColumn,PART_OF_PATH)
    else:
        maze.updatePosition(startRow,startColumn,DEAD_END)
    return found
                

if __name__=='__main__':
    PART_OF_PATH = 'O'          # 部分路径
    TRIED = '.'                 # 尝试
    OBSTACLE = '+'              # 障碍
    DEAD_END = '-'              # 死胡同
    myMaze=maze('mazeFileName.txt')
    myMaze.drawmaze()#在屏幕上绘制迷宫
    searchFrom(maze,myMaze.startRow,myMaze.startCol)

import turtle

# 迷宫类
class Maze(object):
    # 读取迷宫数据，初始化迷宫内部，并找到海龟初始位置。
    def __init__(self, mazeFileName):
        rowsInMaze = 0                          # 初始化迷宫行数
        columnsInMaze = 0                       # 初始化迷宫列数
        self.mazelist = []                      # 初始化迷宫列表
        mazeFile = open(mazeFileName, 'r')      # 读取迷宫文件
        for line in mazeFile:                   # 按行读取
            rowList = []                        # 初始化行列表
            col = 0                             # 初始化列
            # for ch in line[:-1]:              # 这样会丢失最后一列
            for ch in line:                     # 按列读取
                rowList.append(ch)              # 添加到行列表
                if ch == 'S':                   # S为乌龟初始位置，即迷宫起点
                    self.startRow = rowsInMaze  # 乌龟初始行
                    self.startCol = col         # 乌龟初始列
                col = col + 1                   # 下一列
            rowsInMaze = rowsInMaze + 1         # 下一行
            self.mazelist.append(rowList)       # 行列表添加到迷宫列表
            columnsInMaze = len(rowList)        # 获取迷宫总列数
        self.rowsInMaze = rowsInMaze            # 设置迷宫总行数
        self.columnsInMaze = columnsInMaze      # 设置迷宫总列数
        self.xTranslate = -columnsInMaze/2      # 设置迷宫左上角的初始x坐标
        self.yTranslate = rowsInMaze/2          # 设置迷宫左上角的初始y坐标
        self.t = turtle.Turtle()                # 创建一个海龟对象
        self.t.shape('turtle')                  # 给当前指示点设置样式(类似鼠标箭头)，海龟形状为参数指定的形状名，指定的形状名应存在于TurtleScreen的shape字典中。多边形的形状初始时有以下几种："arrow", "turtle", "circle", "square", "triangle", "classic"。
        self.wn = turtle.Screen()               # 创建一个能在里面作图的窗口
        self.wn.setworldcoordinates(-columnsInMaze/2, -rowsInMaze/2, columnsInMaze/2, rowsInMaze/2)         # 设置世界坐标系，原点在迷宫正中心。参数依次为画布左下角x轴坐标、左下角y轴坐标、右上角x轴坐标、右上角y轴坐标

    # 在屏幕上绘制迷宫
    def drawMaze(self):
        self.t.speed(20)                        # 绘图速度
        for y in range(self.rowsInMaze):        # 按单元格依次循环迷宫
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE: # 如果迷宫列表的该位置为障碍物，则画方块
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')

    # 画方块
    def drawCenteredBox(self, x, y, color):
        self.t.up()                             # 画笔抬起
        self.t.goto(x - 0.5, y - 0.5)           # 前往参数位置，此处0.5偏移量的作用是使乌龟的探索路线在单元格的正中心位置
        self.t.color(color)                     # 方块边框为橙色
        self.t.fillcolor('green')               # 方块内填充绿色
        self.t.setheading(90)                   # 设置海龟的朝向，标准模式：0 - 东，90 - 北，180 - 西，270 - 南。logo模式：0 - 北，90 - 东，180 - 南，270 - 西。
        self.t.down()                           # 画笔落下
        self.t.begin_fill()                     # 开始填充
        for i in range(4):                      # 画方块边框
            self.t.forward(1)                   # 前进1个单位
            self.t.right(90)                    # 右转90度
        self.t.end_fill()                       # 结束填充

    # 移动海龟
    def moveTurtle(self, x, y):
        self.t.up()                             # 画笔抬起
        self.t.setheading(self.t.towards(x + self.xTranslate, -y + self.yTranslate))    # setheading()设置海龟朝向，towards()从海龟位置到由(x, y)，矢量或另一海龟位置连线的夹角。此数值依赖于海龟初始朝向，由"standard"、"world"或"logo" 模式设置所决定。
        self.t.goto(x + self.xTranslate, -y + self.yTranslate)  # 前往目标位置

    # 画路径圆点
    def dropBreadcrumb(self, color):
        self.t.dot(color)                       # dot(size=None, color)画路径圆点

    # 用以更新迷宫内的状态及在窗口中改变海龟位置，行列参数为乌龟的初始坐标。
    def updatePosition(self, row, col, val):
        self.mazelist[row][col] = val           # 设置该标记状态为当前单元格的值
        self.moveTurtle(col, row)               # 移动海龟
        if val == PART_OF_PATH:                 # 其中一条成功路径的圆点的颜色
            color = 'green'
        elif val == TRIED:                      # 尝试用的圆点的颜色
            color = 'black'
        elif val == DEAD_END:                   # 死胡同用的圆点的颜色
            color = 'red'
        self.dropBreadcrumb(color)              # 画路径圆点并上色

    # 用以判断当前位置是否为出口。
    def isExit(self, row, col):
        return (row == 0 or row == self.rowsInMaze - 1 or col == 0 or col == self.columnsInMaze - 1)                                # 根据海龟位置是否在迷宫的4个边线位置判断

    # 返回键对应的值，影响searchFrom()中maze[startRow][startColumn]值的获取
    def __getitem__(self, key):
        return self.mazelist[key]

# 探索迷宫，注意此函数包括三个参数：一个迷宫对象、起始行、起始列。
def searchFrom(maze, startRow, startColumn):
    # 从初始位置开始尝试四个方向，直到找到出路。
    # 1. 遇到障碍
    if maze[startRow][startColumn] == OBSTACLE:
        return False
    # 2. 发现已经探索过的路径或死胡同
    if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn]== DEAD_END:
        return False
    # 3. 发现出口
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)# 显示出口位置，注释则不显示此点
        return True
    maze.updatePosition(startRow, startColumn, TRIED)# 更新迷宫状态、设置海龟初始位置并开始尝试
    # 4. 依次尝试每个方向
    # A orB 中or酷游短路特征，如果A是正确的，就不再执行B,返回True,也就是如果先设置向下，向下可以走，就不会再判断其他的
    found = searchFrom(maze, startRow +1, startColumn) or \
            searchFrom(maze, startRow -1, startColumn) or \
            searchFrom(maze, startRow, startColumn - 1) or \
            searchFrom(maze, startRow, startColumn + 1)
    if found:                                                   # 找到出口
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)# 返回其中一条正确路径
    else:                                                       # 4个方向均是死胡同
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found

if __name__ == '__main__':
    PART_OF_PATH = 'O'          # 部分路径
    TRIED = '.'                 # 尝试
    OBSTACLE = '+'              # 障碍
    DEAD_END = '-'              # 死胡同
    myMaze = Maze('mazeFileName.txt')   # 实例化迷宫类，maze文件是使用“+”字符作为墙壁围出空心正方形空间，并用字母“S”来表示起始位置的迷宫文本文件。
    myMaze.drawMaze()           # 在屏幕上绘制迷宫。
    searchFrom(myMaze, myMaze.startRow, myMaze.startCol)    # 探索迷宫
    

#4.7 动态规划
#贪婪算法：最大程度的解决问题
#4.7.1贪婪算法解决找零问题
def recMC1(coinValueList,change):
    mincoin=0 
    i=len(coinValueList)-1 
    a=change
    while a!=0:
        if a>=coinValueList[i]:
            a=a-coinValueList[i]
            mincoin=mincoin+1
        else:
            i=i-1
        
    return mincoin
print(recMC1([1,10,25], 100-37))
#4.7.1 找零问题的递归解决方案
def recMC2(coinValueList,change):
    mincoins=change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if change>=c]:
            numcoins=1+recMC2(coinValueList, change-i)
            if numcoins<mincoins:
                mincoins=numcoins
    return mincoins
print(recMC2([1,5,10,21,25], 63))

#4.7.3找零问题的优化的递归实现
#4.7.2中的递归实现会出现很多重复计算，为防止重复计算，引入了一个列表来储存之前计算的结果
#这是通过牺牲内存来提高计算性能
#knownesultss值个全零的列表，列表的长度要比change大1
def recMC3(coinValueList,change,knownesults):
    mincoins=change
    if change in coinValueList:
        knownesults[change]=1
        return 1
    elif knownesults[change]>0:
        return knownesults[change]
    else:
        for i in [c for c in coinValueList if c<=change]:
            numcoin=1+recMC3(coinValueList, change-i, knownesults)
            if mincoins>numcoin:
                mincoins=numcoin
                knownesults[change]=mincoins
        
    
    return mincoins
print(recMC3([1,5,10,25],63,[0]*64))

#4.7.4 采用动态规划解决找零问题
#动态规划：将从1分找零开始直至所需的找零金额。这样可以保证计算出任何小于当前值的找零金额所需的最小硬币数
#1)1分的最小硬币数为1个，2，3，4分的分别为1，2，3，4个1分的
#2)5分的找零有两种情况，因为找零必须有1，5，10其中的数，如果有1分的，那么最小硬币数是5，如果有5，那么需要找零的硬币数为1
#3）11分的找零分为三种情况，
#如果有1分的那么加上10分的零钱找零所需最小硬币数
#如果有5分的那么加上6分的找零所需的最小硬币数
#如果有10分的那么加上1分找零所需的最小硬币数
#以上三种情况取最小

#mincoins记录了1分找零开始直至所需的找零金额所有的最小硬币数
def recMC4(coinValueList,change,mincoin):
    #生成1，2，3，。。。，change
    for cent in range(1,change+1):
        coincount=cent  #为了后面找所有可能出现的情况中最小的哪个
        for i in [c for c in coinValueList if c<=cent]:
            #if循环是为了找到最小值
            if mincoin[cent-i]+1<coincount:
                coincount=mincoin[cent-i]+1
           
        mincoin[cent]=coincount     #1分找零的必为1，因为前面if语句不成立，直接让列表第一个位置的元素为1
            
    return mincoin[change]

print(recMC4([1,5,10,25],63,[0]*64))

#4.7.5 修改后的动态规划问题（找零问题），可以记录所用的硬币

#coinuse用于保存1到所所求的找零金额所选择的哪个找零的硬币数
def recMC5(coinValueList,change,mincoin,coinused):
    for cent in range(1,change+1):
        coincount=cent
        newcoin=1
        for i in [c for c in coinValueList if c<=cent]:
            if mincoin[cent-i]+1<coincount:
                coincount=mincoin[cent-i]+1
                newcoin=i#记录最小那个的'下标
        mincoin[cent]=coincount
        coinused[cent]=newcoin
  
        
    return mincoin[change]
coinused=[0]*64
print(recMC5([1,5,10,21,25],63,[0]*64,coinused))

def printcoin(coinused,change):
    coin=change
    while coin>0:
        thiscoin=coinused[coin]
        print(thiscoin)
        coin=coin-thiscoin
        
printcoin(coinused, 63)
print(coinused)