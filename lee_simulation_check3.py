def bomb(x,y,Arr):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        a, b = x, y
        for j in range(Arr[x][y]):
            if j == 0:
                Arr[a][b] = 0
            elif 0<=a+dx[i]<n and 0<=b+dy[i]<n:
                Arr[a+dx[i]][b+dy[i]] = 0
                a += dx[i]
                b += dy[i]
            else:
                continue
                
                
            
        
    

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            num = bomb(i,j,arr)

solution()