def MEX(alist):
    n=len(alist)
    pre=[False]*(n+1) 
    for num in alist:
        if num<=n:
            pre[num]=True
    for i in range(n+1):
        if not pre[i]:
            return i 
    return n+1
alist=[]
print(MEX(alist))
# def help(n,k,x,alist):
#     res=k*MEX(alist)
#     for i in range(n):
#         cur_alsit=alist[i+1:]
#         cur_cost=(i+1)*x+k*MEX(cur_alsit)
#         res=min(res,cur_cost)
#     return res

# T=int(input())
# for _ in range(T):
#     n,k,x=map(int,input().split())
#     alist=list(map(int,input().split()))
#     print(help(n,k,x,alist))