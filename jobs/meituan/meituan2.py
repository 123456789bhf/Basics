def help(n,s,passwords):
    correct_len=len(s)
    len_dic={}
    for password in passwords:
        length=len(password)
        if length in len_dic:
            len_dic[length]+=1
        else:
            len_dic[length]=1
    min_res=0
    max_res=0
    pre=0
    for length in sorted(len_dic.keys()):
        if length<correct_len:
            min_res+=len_dic[length]
            max_res+=len_dic[length]
            pre+=len_dic[length]
        elif length==correct_len:
            min_res=pre+1
            max_res=pre+len_dic[length]
            break 
    return min_res,max_res

def main():
    n=int(input())
    s=input()
    passwords=[input().strip() for _ in range(n)]
    min_res,max_res=help(n,s,passwords)
    print(min_res,max_res)

if __name__=='__main__':
    main()
