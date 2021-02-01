from collections import deque
import sys
n,m = map(int,input().split())  #n 격자 크기, m 병원 수
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [['F' for _ in range(n)] for _ in range(n)]
q = deque()
answer = []
hospitalstate = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            hospitalstate.append((i,j))
hospital = len(hospitalstate)
maxpeople = sys.maxsize

def InRange(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False
    
def CanGo(x,y):
    if not InRange(x,y):
        return False
    if (visited[x][y] == 'T') or (arr[x][y]==0) or (arr[x][y]==2):
        return False
    return True


def Push(x,y,h):
    visited[x][y] = 'T'
    q.append([x,y,h])
    
def BFS():
    global visited
    global maxpeople
    people = 0

    while q:
        x,y,h = q.popleft()
        if h == 2:
            hospital_x = x
            hospital_y = y
        for i in range(n):
            for j in range(n):
                if CanGo(i,j):
                    people += abs(hospital_x-i)+abs(hospital_y-j)
                    Push(i,j,1)
    maxpeople = min(maxpeople, people)
    visited = [['F' for _ in range(n)] for _ in range(n)]
    
def Print():
    for i in answer:
        q,w = hospitalstate[i]
        visited[q][w] = 'T'
        Push(q,w,2)
    BFS()
    

def Choose(start, curr_num):
    if(curr_num == m+1):
        Print()
        return
    
    for i in range(start, hospital):
        if len(answer)>0 and answer[-1] >= i:
            continue
        else:
            answer.append(i)
            Choose(start+1, curr_num+1)
            answer.pop()
    return




        
Choose(0,1)
print(maxpeople)



    



