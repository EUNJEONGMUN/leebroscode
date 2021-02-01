import sys
user = list(input())
k = len(user)//2+1
answer = []
maxsum = -sys.maxsize


       

def Choose(curr_num):
    global maxsum
    if(curr_num == k+1):
        Sum = Operate(answer)
        maxsum = max(maxsum, Sum)
        #A = answer
        #Sum = Operate(A)
        #maxsum.append(Sum)
        return

    for i in range(1, 5):
        answer.append(i)
        Choose(curr_num+1)
        answer.pop()
    return

def Operate(temp):
    Sum = temp[0]
    for i,j in zip(temp[1:], range(1,len(user),2)):
        if user[j] == '+':
            Sum += i
        elif user[j] == '-':
            Sum -= i
        else:
            Sum *= i
    
    return Sum
            
        
        
Choose(1)
print(maxsum)


