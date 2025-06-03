'''from turtle import *
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


moveTowertest()'''

'''from turtle import *

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
#二叉树
class binarytree:
    def __init__(self,rootobj):
        self.root=rootobj
        self.leftchild=None
        self.rightchild=None
    #插入左子节点
    def insertleft(self,newnode):
        #树原来不存在左子树，那么就插入
        if self.leftchild==None:
            self.leftchild=binarytree(newnode)
        else:
            #存在左子树
            t=binarytree(newnode)
            #将新节点的左子树设置为原来节点的左子树
            t.leftchild=self.leftchild
            #将树的左子树设置为当前节点
            self.leftchild=t
    #插入右子节点
    def insertright(self,newnode):
        if self.rightchild==None:
            self.rightchild=binarytree(newnode)
        else:
            t=binarytree(newnode)
            t.rightchild=self.rightchild
            self.rightchild=t
    #二叉树的访问函数
    def getleftchild(self):
        return self.leftchild
    def getrightchild(self):
        return self.rightchild
    #修改根节点
    def setrootval(self,obj):
        self.root=obj
    #获取根节点
    def getrootval(self):
        return self.root
    
#解析树
def buildparsetree(fexp):
    pstack=Slack()  #用栈来记录父节点
    eTree=binarytree('') #创建空树
    fplist=fexp.split() #空格分割
    currenttree=eTree 
    pstack.push(eTree) 
    for i in fplist:
        if i =='(':
            currenttree.insertleft('') #创建左子节点
            pstack.push(currenttree) #记录父节点(这里记录的是一整棵树)
            currenttree=currenttree.getleftchild() #下沉至左子节点
        #如果是操作符
        elif i not in '+-*/':
            currenttree.setrootval(eval(i)) #设置当前值。eval() 函数用来执行一个字符串表达式，并返回表达式的值。
            currenttree=pstack.pop()  #调到父节点（pstack储存父节点）
        elif i in '+-*/':
            currenttree.setrootval(i)   #设置当前节点值
            currenttree.insertright('')  #创建右节点
            pstack.push(currenttree)  #记录父节点
            currenttree=currenttree.getrightchild() #跳到右节点
        elif i ==')':
            currenttree=currenttree.pop()
        else:
            raise ValueError('nuknownoperator:'+i)
    return eTree

print(buildparsetree('( 2 * 3 + 1 ) + 2')))'''


class Slack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    # 查找栈中顶部的第一个元素
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 二叉树
class binarytree:
    def __init__(self, rootobj):
        self.root = rootobj
        self.leftchild = None
        self.rightchild = None

    # 插入左子节点
    def insertleft(self, newnode):
        # 树原来不存在左子树，那么就插入
        if self.leftchild == None:
            self.leftchild = binarytree(newnode)
        else:
            # 存在左子树
            t = binarytree(newnode)
            # 将新节点的左子树设置为原来节点的左子树
            t.leftchild = self.leftchild
            # 将树的左子树设置为当前节点
            self.leftchild = t

    # 插入右子节点
    def insertright(self, newnode):
        if self.rightchild == None:
            self.rightchild = binarytree(newnode)
        else:
            t = binarytree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t

    # 二叉树的访问函数
    def getleftchild(self):
        return self.leftchild

    def getrightchild(self):
        return self.rightchild

    # 修改根节点
    def setrootval(self, obj):
        self.root = obj

    # 获取根节点
    def getrootval(self):
        return self.root


# 解析树
def buildparsetree(fexp):
    pstack = Slack()  # 用栈来记录父节点
    eTree = binarytree('')  # 创建空树
    fplist = fexp.split()  # 空格分割
    currenttree = eTree
    pstack.push(eTree)
    for i in fplist:
        if i == '(':
            currenttree.insertleft('')  # 创建左子节点
            pstack.push(currenttree)  # 记录父节点(这里记录的是一整棵树)
            currenttree = currenttree.getleftchild()  # 下沉至左子节点
        # 如果是操作符
        elif i not in '+-*/':
            currenttree.setrootval(i)  # 设置当前值。eval() 函数用来执行一个字符串表达式，并返回表达式的值。
            currenttree = pstack.pop()  # 调到父节点（pstack储存父节点）
        elif i in '+-*/':
            currenttree.setrootval(i)  # 设置当前节点值
            currenttree.insertright('')  # 创建右节点
            pstack.push(currenttree)  # 记录父节点
            currenttree = currenttree.getrightchild()  # 跳到右节点
        elif i == ')':
            currenttree = currenttree.pop()
        else:
            raise ValueError('nuknownoperator:' + i)
    return eTree


print(buildparsetree('( 2 * 3 + 1 ) + 2'))