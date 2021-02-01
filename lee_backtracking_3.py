n,m = map(int,input().split())
answer = []


def Print():
    for i in answer:
        print(i, end=' ')
    print()
        

def Choose(start, curr_num):
    if(curr_num == m+1):
        Print()
        return

    for i in range(start, n+1):
        if len(answer)>0 and answer[-1] >= i:
            continue
        else:
            answer.append(i)
            Choose(start+1, curr_num+1)
            answer.pop()
    return
        
Choose(0,1)
    
