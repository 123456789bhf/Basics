from collections import deque

def help(n,a):
    dp=[float('-inf')]*(n+1)
    dp[0]=0
    deq=deque([0])
    for i in range(1,n+1):
        if deq[0]<i-4:
            deq.popleft()
        dp[i]=dp[deq[0]]+a[i-1]
        while deq and dp[deq[-1]]<=dp[i]:
            deq.pop()
        dep.append(i)
    return dp[n] if dp[n]>=0 else -1
n=int(input())
a=list(map(int,input().split()))
print(help(n,a))