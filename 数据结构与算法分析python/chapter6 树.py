# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:05:36 2023

@author: 23665
"""

#6.3,术语

#层数：节点n的层数是从根节点到n的唯一路径长度（路径上边的个数）
#高度：树中所有节点层数的最大值

#定义一：树具有以下属性
#1）只有一个根节点
#2）根节点到节点的路径是唯一的
#3）除了根节点外，其他节点都只有唯一一个父节点
#4）每个节点至多只有两个（n个）子节点，这样的树称为二叉树（n叉树）

#定义二：一个树要么为空，要么由根节点和零个或多个子树构成，子树本身也是树


#6.4. 实现
#6.4.1. 列表之列表
#采用列表实现树，对于二叉树，列表的第一个元素是根节点，第二个元素是左子树，所以也是个列表，第三个元素是右子树（也是个列表）
#根据上面的树的实现，可以通过递归实现树
'''
myTree=['a' ,#根节点/
        ['b' ,#左子树/
         ['d',[],[]] ,#左子树的左子树
         ['e',[],[]], #左子树的右子树
         ],
        ['c', #右子树
         ['f',[],[]] ,#右子树的左子树
         []  #右子树的右子树
         ],
        ]
print(myTree)

#代码6_1 列表函数（船舰树，首先有个根节点）
def binarytree(r):
    return [r,[],[]]

#代码6-2 插入左子树
#注意：如果左子树已经存在，那么就将其作为插入节点的左子树

#root是原来的树，newbranch是新节点
def insertleft(root,newbranch):
    t=root.pop(1)
    #判断原来的树是否存在左子树
    if len(t)>1:
        root.insert(1,[newbranch,t,[]])  #存在左子树，那么将其作为新节点的左子树
    else:
        root.insert(1,[newbranch,[],[]])
        
    return root

#代码6-2 插入右子树
def insertright(root,newbranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newbranch,[],t])
    else:
        root.insert(2,[newbranch,[],[]])
    return root

#代码6-4树的访问函数
#访问根节点
def getrootval(root):
    return root[0]
#设置根节点的值
def setrootval(root,newval):
    root[0]=newval
#获取左子树
def getleftchild(root):
    return root[1]
#获取右子树
def getrightchild(root):
    return root[2]
r=binarytree(3)
insertleft(r, 4)
print(r)
insertleft(r, 5)
insertright(r, 6)
insertright(r, 7)
print(r)
l=getleftchild(r)
print(l)
setrootval(l, 9) #根据setrootval的构造可以知道此时也修改了r的值
insertleft(l, 11)
print(r)
print(getrightchild(getrightchild(r)))

#6.4.2.节点与引用
#引用两个链接，分别指向左右子树
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
r=binarytree('a')
print(r.getrootval())
print(r.getleftchild())
r.insertleft('b')
print(r.getleftchild())
print(r.getleftchild().getrootval())
r.insertright('c')
print(r.getrightchild().getrootval())

#6.5 二叉树的应用
#6.5.1. 解析树
#主要研究
#1）如何根据完全表达式构建解析树
#2）如何计算解析树中的表达式
#3）如何讲树还原成最初的数学表达式

#代码6-9 解析树构建器
#思路：
#1）如果标记是（,那么就为当前节点创建左子节点，并下沉到创建的左子节点
#2）如果是加减乘除中的，那么就将该节点设置为它，然后创建右子节点，并且下沉到新创建的右子节点
#3）如果是数字，那么就将该节点设置为它，跳到父节点
#4）如果是）,直接跳到父节点

#注意：可以通过栈记录其父节点，每当下沉到当前节点的子节点时，先将当前节点压入到栈中。当想要返回节点的父节点时，就将父节点从栈中弹出乱来
#栈
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
#函数结果是解析树
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
        elif i not in '+-*/)':
            currenttree.setrootval(eval(i))  # i改为eval(i)会出错。设置当前值。eval() 函数用来执行一个字符串表达式，并返回表达式的值。
            currenttree = pstack.pop()  # 调到父节点（pstack储存父节点）
        elif i in '+-*/':
            currenttree.setrootval(i)  # 设置当前节点值
            currenttree.insertright('')  # 创建右节点
            pstack.push(currenttree)  # 记录父节点
            currenttree = currenttree.getrightchild()  # 跳到右节点
        elif i == ')':
            currenttree = pstack.pop()
        else:
            raise ValueError('nuknownoperator:' + i)
    #虽然currenttree=etree进行了赋值后面是对currenttree修改，但是etree也已经被修改了，因为是个类
    #本质上是对创建的同一个对象进行的修改
    return eTree

#结果是个类,输入的表达式最外层必须要有括号，否则会报错
print(buildparsetree('( ( 2 * 3 + 1 ) + 2 )').getleftchild().getrootval())

'''
x = 7
print(eval( '3 * x' ))

print(eval('pow(2,2)'))
print(eval('2 + 2'))
n=81
print(eval("n + 4"))
'''
    
#代码6-10 计算二叉解析树的递归函数
#解析树特征：一定是满二叉树，也就是每个节点必有量子子节点，即左右子节点
#解析树的叶子节点必为操作数，其他的都是运算符。由于像整数和浮点数这样的数值对象不需要进一步翻译，因此evaluate函数
#可以直接返回叶子结点的值。为了像基本情况靠近，算法将执行递归步骤，即对当前的左右子节点调用evaluate函数

#operator提供了基本运算符的函数
import operator
#parsetree是解析树,是个类别
def evaluate(parsetree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    #获得左右子树
    leftc=parsetree.getleftchild()
    rightc=parsetree.getrightchild()
    #if None:停止循环，相当于True
    #如果左右子树都不是空的
    if leftc and rightc:
        fn=opers[parsetree.getrootval()]
        return fn(evaluate(leftc),evaluate(rightc))
    else:
        #基本结束条件
        return parsetree.getrootval()

#必须要有大括号
print(evaluate(buildparsetree('( ( 7 + 3 ) * ( 5 - 2 ) )')))
#6.5.2. 树的遍历：对数据集中的所有数据项进行访问的操作称为‘遍历’
#遍历的三种类型
#1)前序遍历：先访问根节点，然后递归访问左子树，最后递归访问右子树
#2）中序遍历：先中序递归访问左子树，然后访问根节点，最后递归地中序递归访问右子树
#3）后序遍历：递归访问左子树，然后递归访问右子树，然后访问根节点

#代码6-11 将前序遍历算法时限为外部函数(相比于代码6-12，这个较常用)
def preorder(tree):
    #如果tree不是None,如果是None那么停止递归
    if tree:
        #先访问根节点
        print(tree.getrootval())
        #在访问左子树
        preorder(tree.getleftchild())
        #在访问右子树
        preorder(tree.getrightchild())
    
#代码6-12 将前序遍历算法实现为binarytree类的方法
'''
def preorder(self):
    print(self.root)
    if self.getleftchild():
        self.getleftchild().preorder()
    if self.getrightchild():
        self.getrightchild().preorder()
'''

#代码6-13 后序遍历函数
def postorder(tree):
    if tree:
        postorder(tree.getleftchild)
        postorder(tree.getrightchild)
        print(tree.getrootval)

#后续求解析树的值（后续求值函数）
def posorderreval(tree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    if tree:
        res1=posorderreval(tree.getleftchild())
        res2=posorderreval(tree.getrightchild())
        if res1 and res2:
            return opers[tree.getrootval()](res1,res2)
        else:
            return tree.getrootval()
print(posorderreval(buildparsetree('( ( 7 + 3 ) * ( 5 + 2 ) )')))

#代码6-14 中序遍历函数
def inorder(tree):
    if tree:
        inorder(tree.getleftchild())
        print(tree.getrootval)
        inorder(tree.getrightchild())

#代码6-16 修改后的中序遍历函数，他能还原完全括号表达式
def printexp(tree):
    sval=''
    if tree:
        sval='('+printexp(tree.getleftchild())
        sval=sval+str(tree.getrootval())
        sval=sval+printexp(tree.getrightchild())+')'
    return sval
x=binarytree('*')
x.insertleft('+')
l=x.getleftchild()
l.insertleft(4)
l.insertright(5)

x.insertright(7)
print(printexp(x)) 
print(posorderreval(x))           

#6.6利用二叉堆实现队列的优先级

#优先级队列从头部移除元素，不过元素的逻辑顺序是由优先级决定的。优先级最高的在前面，优先级最低的元素在后面
#实现优先级队列的经典方法是二叉堆数据结构。二叉堆的入队和出队操作均可以达到O(logn)

#二叉堆的两个常见的变体：最小堆(最小的元素一直在队首)，最大堆(最大的元素一直在队首)

#平衡二叉树：根节点的左右子树含有数量大致相同的节点
#完全二叉树：除了最底层，其他节点都由左右子节点
#二叉堆的有序性：对任意的元素x,其父节点p,p小于等于x

#二叉堆的性质：
#1) 用完全二叉树表示(不是嵌套性质)
#2) 任何一个路径上都是有序序列，并且子节点比父节点大
 
#代码6-17 新建二叉堆
class binaryheap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0  #记录二叉堆中元素位置
    #实现元素的向上移动操作
    def percup(self,i):
        #如果到了根节点，就停止
        while i//2>0:
            #如果父节点大于子节点，那么就交换位置
            if self.heaplist[i]<self.heaplist[i//2]:
                temp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[i//2]
                self.heaplist[i//2]=temp
            i=i//2
    #向二叉堆中添加新元素
    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize=self.currentsize+1
        self.percup(self.currentsize)
    #delmin方法：删除最小值（根节点的值是最小值），并且返回（注意：删除之后可能会破坏堆的性质）
    #1）先将列表中的最后一个元素移动到根节点（这样会破坏堆的有序性）
    #2）将新的根节点，沿着树推到正确的位置，以获得堆的有序性
    def perdown(self,i):
        #如果存在子节点
        while (i*2)<=self.currentsize:
            mc=self.minchild(i)
            if self.heaplist[i]>self.heaplist[mc]:
                temp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[mc]
                self.heaplist[mc]=temp
            i=mc
    def minchild(self,i):
        #唯一的子节点
        if (i*2+1)>self.currentsize:
            return i*2 
        else:
            #如果左子节点小于右子节点，那么返回左子节点，否则返回右子节点，总体来说返回最小节点
            if self.heaplist[i*2]<self.heaplist[i*2+1]:
                return i*2 
            else:
                return i*2+1
    #从二叉堆中删除最小的元素,并且返回
    def delmin(self):
        retval=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize=self.currentsize-1
        self.heaplist.pop()
        self.perdown(1)
        return retval
    #构建堆的方法：
    #1)给定元素列表，每次插入一个元素，构建一个堆，这样时间复杂度是O(nlogn)
    #2)从完整列表开始，构建堆的时间复杂度是O(n)
    def buildheap(self,alist):
        i=len(alist)//2
        self.heaplist=[0]+alist[:]
        self.currentsize=len(alist)
        while i>0:
            self.perdown(i)
            i=i-1 
bh=binaryheap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
'''
#6.7 二叉树搜索：是映射的另外一种实现
#二叉树搜索依赖于这样的一个性质（二叉搜索性）：小于父节点的键都在左子树中，大于父节点的键都在右子树中
#正在完全平衡二叉树中，最坏的put得时间复杂度是O(logn)
#如过二叉搜索树的高度是n(节点个数)，那么put,get, in,del得时间复杂度是O(n)，也就是不平衡二叉树得最坏情况下时间复杂度是O(n)

class binarysearchtree():
    def __init__(self):
        self.root=None #根节点
        self.size=0    #节点个数
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    #删除指定的键值
    def delete(Self,key):
        if self.szie>1:
            nodetoremove=self._get(key,self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size=self.size-1
            else:
                raise KeyError('error,key not in tree')
        elif self.size==1 and self.root.key==key:
            self.size=self.size-1
            self.root=None
        else:
            raise KeyError('error,key not in tree')
    #特殊的实例方法：用del myziptree['pku]
    def __delitem__(self,key):
        self.delete(key)
    #删除指定节点方法,分三种情况
    #1）如果没有子节点
    #2）如果只有一个子节点
    #3）如果有两个子节点
    def remove(self,currentnode):
        #没有节点
        if currentnode.isleaf():
            if currentnode.parent.leftchild==currentnode:
                currentnode.parent.leftchild=None
            else:
                currentnode.parent.rightchild=None
        #只有一个节点
        #待删除的节点有两个子节点:
        #方法：搜索整棵树，找到可以替换删除节点的节点。成为候选节点，候选节点要
        #能为左右子树都保持二叉搜索树的关系，也就是书中具有次大键的节点，我们称之为后继节点
        elif currentnode.hasbothchild():
            #找到后继节点（nodetree类中的实例方法）
            succ=currentnode.findsuccessor() 
            succ.spliceout()  #将后继节点删除（nodetree中的实例方法）
            currentnode.key=succ.key
            currentnode.playload=succ.playload
            
            
            
        else:
            #当前节点只有一个左子节点
            if currentnode.hasleftchild():
                #当前节点是父节点的左子节点
                if currentnode.isleftchild():
                    currentnode.parent.leftchild=currentnode.leftchild
                    currentnode.leftchild.parent=currentnode.parent
                #当前节点是父节点的右子节点
                elif currentnode.hasrightchild():
                    currentnode.leftchild.parent=currentnode.parent
                    currentnode.parent.rightchild=currentnode.leftchild
                #当前节点没有父节点，也就是根节点：
                #调用replacenodedata方法，替换节点的key,playload,leftchild,rightchild方法
                else:
                    currentnode.replacenodedata(currentnode.leftchild.key,
                                                currentnode.leftplayload.playload,
                                                currentnode.leftchild.leftchild,
                                                currentnode.leftchild.rightchild)
            #当前节点只有一个右子节点
            else:
                #当前节点是右子节点
                if currentnode.isrightchild():
                    currentnode.rightchild.parent=currentnode.parent
                    currentnode.parent.rightchild=currentnode.rightchild
                #当前节点是左子节点
                elif currentnode.isleftchild():
                    currentnode.rightchild.parent=currentnode.parent
                    currentnode.parent.leftchild=currentnode.rightchild
                else:
                    currentnode.replacenodedata(currentnode.rightchild.key,
                                                currentnode.rightchild.playload,
                                                currentnode.rightchild.leftchild,
                                                currentnode.rightchild.rightchild)
    
    #向二叉搜索树中插入一个键值对
    def put(self,key,value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root=treenode(key,value)
        self.size=self.size+1
    #currentnode是当前节点
    def _put(self,key,value,currentnode):
        #插入到左子树
        if key<currentnode.key:
            #当存在左子节点时候
            if currentnode.hasleftchild():
                self._put(key,value,currentnode.leftchild)
            #如果不存在左节点，就将节点的左子节点设置为插入的节点
            else:
                currentnode.leftchild=treenode(key,value,parent=currentnode)
        if key>currentnode.key:
            if currentnode.hasrightchild():
                self._put(key, value, currentnode.rightchild)
            else:
                currentnode.rightchild=treenode(key,value,parent=currentnode)
                
    def __setitem__(self,key,val):
        self.put(key, val)
    
    #查找键对应的值
    def get(self,key):
        if self.root:
            currentnode=self._get(key,self.root)
            if currentnode:
                return currentnode.playload
            else:
                return None  
        else:
            return None
            
    def _get(self,key,currentnode):
        #递归结束条件,如果是空集，那么返回None
        if not currentnode:
            return None
        elif currentnode.key==key:
            return currentnode
        elif key<currentnode.key:
            self._get(key,currentnode.leftchild)
        else:
            self._get(key,currentnode.rightchild)
            
    #检查数中是否有某个键
    def __contains__(self,key):
        if self._get(key):
            return True
        else:
            return False
        

class treenode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key          #键
        self.playload=val     #值
        self.leftchild=left   #右子节点
        self.rightchild=right #记录左子节点
        self.parent=parent  #记录父节点
        self.balancefactor=0 #记录AVL中的平衡因子

    def hasleftchild(self):
        return self.leftchild
    
    def hasrightchild(self):
        return self.rightchild
    
    def isleftchild(self):
        #self.parent.leftchild==self:当前对象的父节点的左子节点等于当前对象本身。
        #这样的比较通常用于树或图等数据结构中，用于检查当前节点是否是其父节点的左子节点。
        return self.parent and self.parent.leftchild==self
    def isrightchild(self):
        return self.parent and self.parent.rightchild==self
    def isroot(self):
        return not self.parent
    #判断是否是叶节点
    def isleaf(self):
        #如果没有左右子节点时候为真
        return not (self.leftchild or self.rightchild)
    def hasbothchild(self):
        return self.leftchild and self.rightchild
    
    def hasanychild(self):
        return self.leftchild or self.rightchild
    
    def replacenodedata(self,key,value,lc,rc):
        self.key=key
        self.playload=value
        self.leftchild=lc
        self.rightchild=rc
        if self.hasleftchild():
            #如果当前节点由左子节点，就让新节点作为左子节点的父节点
            self.leftchild.parent=self
        if self.hasrightchild():
            self.rightchild.parent=self
            
    #寻找当前节点的后继节点：也就是找该节点的次大节点
    #1)如果当前节点的存在右子节点，那么后继节点是右子树中的最小节点（二叉搜索树的结构式右子节点大于父节点）
    #2）如果没有右子节点，并且是父节点的左子节点，那么后继节点是父节点
    #3）如果是父节点的右子节点，并且本身没有右子节点，那么后记节点就是出本身外父节点的后继节点
    def findsuccessor(self):
        succ=None
        #如果有右子节点，那么后记节点是右子树的最小键
        if self.hasrightchild():
            succ=self.rightchild.findmin()
        else:
            #如果没有右子节点，但是父节点的左子节点，后继节点是父节点
            if self.parent:
                if self.isleftchild():
                    succ=self.parent
                elif self.isrightchild():
                    self.parent.rightchild=None
                    succ=self.findsuccessor()
                    self.parent.rightchild=self
        return succ
    
    #计算子树中的最小键：在任意搜索二叉树中，最小键就是最左边的子节点
    def findmin(self):
        current=self
        #如果存在左子节点
        while current.leftchild():
            current=current.leftchild
        return current
    def spliceout(self):
        #是叶节点
        if self.isleaf():
            if self.isleftchild():
                self.parent.leftchild=None
            else:
                self.parent.rightchild=None
        #存在子节点
        elif self.hasanychild():
            #有左子节点
            if self.hasleftchild():
                if self.isleftchild():
                    self.parent.leftchild=self.leftchild
                    self.leftchild.parent=self.parent
                else:
                    self.parent.rightchild=self.leftchild
                    self.leftchild.parent=self.parent
            #有右子节点
            elif self.hasrightchild():
                if self.isrightchild():
                    self.parent.rightchild=self.rightchild
                    self.rightchild.parent=self.parent
                else:
                    self.parent.leftchild=self.rightchild
                    self.rightchild.parent=self.parent
    #python为创建迭代器提供了一个很强大的函数yield。与return类似，yield每次都向调用方返回一个值
    #除此之外，yield还会冻结函数状态，因此下次调用函数的时候，会从这次离开之处继续
    #创建迭代器对象的函数称为生成器
    
    #实现循环操作：for x in
    def __iter__(Self):
        if self:
            if self.hasleftchild():
                for elem in self.leftchild:  #相当于调用了__iter__(self.lefychild)函数,也就是进行了递归调用
                    yield elem
            yield self.key
            if self.hasrightchild():
                for elem in self.rightchild:
                    yield elem
'''
tree=binarysearchtree()
tree.put(2,'dog')
tree.put(3, 'cat')
tree.put(4,'banance')
print(tree.get(2))
'''
'''
#yield函数的介绍
def simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = simple_generator()
#next依次输出
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3
print(next(gen))  # 输出: 4
print(next(gen))  # 输出: 5

gen = simple_generator()
#也可以使用for循环输出结果
for value in gen:
    print(value)
# 输出:
# 1
# 2
# 3
# 4
# 5

'''
#6.8 平衡二叉搜索树
#自动维持二叉搜索树的平衡，这种称为AVL树
#二叉搜索树中的平衡因子定义为左右子树的高度之差
#balance factor=height(left sub tree)-height(right sub tree)
#平衡因子等于0，那么就说该节点是平衡的，如果大于0，那么称为左倾，小于0，称为右倾
#为了实现AVL树并利用平衡树得优势，我们将平衡因子为-1，0，1得树都定义为平衡树 
#对于平衡二叉搜索树的时间复杂度被限制在O(logN)

#6.8.2 AVL树得实现
#递归结束的基本情况：
#1）递归调用到达根节点
#2）父节点的平衡因子调整为0；可以确信，如果子树的平衡因子调整为0，那么祖先节点的平衡因子将不会再有变化
#因为如果树的平衡因子调整为零，那么左右子树的高度相同，说明肯定树的高度不变
class AVL(binarysearchtree):
    def __init__(self):
        super().__init__()
        
    def _put(self,key,val,currentnode):
        if key<currentnode.key:
            #如果有左子节点，那么递归
            if currentnode.hasleftchild():
                self._put(key, val, currentnode.leftchild)
            else:
                currentnode.leftchild=treenode(key, val,parent=currentnode)
                self.updatabalance(currentnode.leftchild)
        else:
            if currentnode.hasrightchild():
                self._put(key, val, currentnode.rightchild)
            else:
                currentnode.rightchild=treenode(key, val,parent=currentnode)
                self.updatabalance(currentnode.rightchild)
                
                
    #更新节点的平衡因子
    def updatabalance(self,node):
        #如果节点不平衡，那么让其重新平衡
        if node.balancefactor>1 or node.balancefactor<-1:
            self.rebalance(node)
            return  #为什么还要返回值
        #在上面平衡之后，node的平衡因子为-1，1，0这三个数
        if node.parent!=None:
            #如果存在父节点，并且是父节点的左子节点,那么新加入的节点的父节点平衡因子加1
            if node.isleftchild():
                node.parent.balancefactor=+1
            else:
            #新加入的节点是右子节点，那么父节点平衡因子-1
                node.parent.balancefactor=-1
            #如果某个节点平衡因子调整之后为0，那么停止循环，因为祖先节点的平衡因子不会改变
            if node.parent.balancefactor!=0:
                self.updatabalance(node.parent)
    
    #代码6-38 左旋
    #旧根节点rotroot
    def rotateleft(self,rotroot):
        #新的根节点
        newroot=rotroot.rightchild
        #如果新根节点存在左子节点，那么就让旧根节点的右子节点为新根节点的左子节点
        #此时新节点的左子节点可能是None
        rotroot.rightchild=newroot.leftchild
        if newroot.hasleftchild():
           newroot.leftchild.parent=rotroot
        newroot.parent=rotroot.parent
        if rotroot.isroot():
            self.root=newroot
        else:
            if rotroot.isleftchild():
                rotroot.parent.leftchild=newroot
            else:
                rotroot.parent.rightchild=newroot
        newroot.leftchild=rotroot
        rotroot.parent=newroot
        rotroot.balancefactor=rotroot.balancefactor+1-min(newroot.balancefactor,0)
        newroot.balancefactor=newroot.balancefactor+1+max(rotroot.balancefactor,0)
            
        
            
    #右旋
    def rotateright(self,rotroot):
        #新的根节点
        newroot=rotroot.rightchild
        #如果新根节点存在左子节点，那么就让旧根节点的右子节点为新根节点的左子节点
        #此时新节点的左子节点可能是None
        rotroot.leftchild=newroot.rightchild
        if newroot.hasrightchild():
           newroot.rightchild.parent=rotroot
        newroot.parent=rotroot.parent
        if rotroot.isroot():
            self.root=newroot
        else:
            if rotroot.isrightchild():
                rotroot.parent.rightchild=newroot
            else:
                rotroot.parent.leftchild=newroot
        newroot.rightchild=rotroot
        rotroot.parent=newroot
        rotroot.balancefactor=rotroot.balancefactor+1-min(newroot.balancefactor,0)
        newroot.balancefactor=newroot.balancefactor+1+max(rotroot.balancefactor,0)
    #如何实现树的再平衡
    #总的思路：左倾右旋，右倾左旋
    #1)如果子树需要左旋（即右倾），首先检查右子树的平衡因子。如果右子树左倾，就对右子树做一次右旋，在绕原节点做一次左旋
    #2）如果子树需要右旋（即左倾），首先检查左子树是否右倾，如果是，你就对左子树进行一次左旋，在绕原节点做一次右旋
    def rebalance(self,node):
        #右倾
        if node.balancefactor<0:
            #右子节点左倾
            if node.rightchild.balancefactor>0:
                self.rotateright(node.rightchild)
                self.rotateleft(node)
            else:
                self.rotateleft(node)
        #左倾
        elif node.balancefactor>0:
            #左子节点右倾
            if node.leftchild.balancefactor<0:
                self.rotateleft(node.leftchild)
                self.rotateright(node)
            else:
                self.rotateright(node)
                
tree=AVL()
tree.put(2,'dog')
tree.put(3, 'cat')
tree.put(4,'banance')
tree.put(5,'hello')
tree.put(1,'keke')
print(tree.get(2))       
                
                
            

                
            
        
        
    
    