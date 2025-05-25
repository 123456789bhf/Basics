def cal_expression(expression):
    def calc(nums,ops):
        op=ops.pop()
        b=nums.pop()
        a=nums.pop()
        if op=='+':
            nums.append(a+b)
        elif op=='*':
            nums.append(a*b)
    nums=[]
    ops=[]
    i=0
    while i<len(expression):
        if expression[i].isdigit():
            num=0
            while i<len(expression) and pression[i].isdigit():
                num=num*10+int(expression[i])
                i+=1
            nums.append(num)
        elif expression[i] in '*+':
            while (ops and ops[-1]=='*') or (ops and expression[i]=='+'):
                calc(nums,ops)
            ops.append(expression[i])
            i+=1
        else:
            i+=1
    while ops:
        calc(nums,ops)
    return nums[0] if nums else None

def help(equation):
    left_side,right_side=equation.split('=')
    if cal_expression(left_side)==cal_expression(right_side):
        return True
    for i in range(len(equation)+1):
        for digit in range(10):
            new_eq=equation[:i]+str(digit)+equation[i:]
            new_left_side,new_right_side=new_eq.split('=')
            if cal_expression(new_left_side)==cal_expression(new_right_side):
                return True
    return False
def main():
    import sys
    input=sys.stdin.read
    data=input().strip().split('\n')
    T=int(data[0])
    res=[]
    for i in range(1,T+1):
        equation=data[i]
        if help(equation):
            res.append('Yes')
        else:
            res.append('No')
    for result in res:
        print(result)
if __name__=='__main__':
    main()


    