def solve(s):
    n=len(s)
    initial_head=s.count('1')
    gain=[-1 if c=='1' else 1 for c in s]
    max_gain=float('-inf')
    current_gain=0
    start=0
    end=0
    temp_start=0
    for i in range(n):
        if current_gain+gain[i]>gain[i]:
            current_gain+=gain[i]
        else:
            current_gain=gain[i]
            temp_start=i 
        if current_gain>max_gain:
            max_gain=current_gain
            start=temp_start
            end=i 
    max_heads=initial_head+max_gain
    if max_gain<=0:
        print(initial_head)
        print(1,1)
    else:
        print(max_heads)
        print(start+1,end+1)
s=input().strip()
solve(s)