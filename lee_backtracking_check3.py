import sys
n,m = map(int,input().split())
arr = []
answer=[]
my_answer = []

for _ in range(m):
    arr.append(tuple(map(int,input().split())))

        

def Choose(start, curr_num):
    if(curr_num == 3):
        solution(answer)
        return

    for i in range(start, n):
        if len(answer)>0 and answer[-1] >= i:
            continue
        else:
            answer.append(i)
            Choose(start+1, curr_num+1)
            answer.pop()
    return

def solution(temp):
    print(temp)
    print(arr[temp[0]][0])
    print(arr[temp[1]][0])
    print(arr[temp[0]][1])
    print(arr[temp[1]][1])
    #a = ((arr[temp[0]][0]-arr[temp[1]][0])**2) + ((arr[temp[0]][1]-arr[temp[1]][1])**2)
    #my_answer.append(a)

Choose(0,1)
#print(min(my_answer))

    
