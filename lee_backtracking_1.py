k,n = map(int,input().split())
answer = []


def Print():
    for i in answer:
        print(i, end=' ')
    print()
        

def Choose(curr_num):
    if(curr_num == n+1):
        Print()
        return

    for i in range(1, k+1):
        answer.append(i)
        Choose(curr_num+1)
        answer.pop()
    return
        
Choose(1)
    
