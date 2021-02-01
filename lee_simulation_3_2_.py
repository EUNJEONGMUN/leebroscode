def solution():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    
    
    x,y = map(int,input().split())
    point = arr[x-1][y-1]
    arr[x-1][y-1] = 0

    arr = bomb(x,y,n,point, arr)
    newarr = bombafter(n,arr)

    for elem in newarr:
        for i in range(len(elem)):
            print(elem[i], end=' ')
        print() 

def bomb(x,y,n,Point, Arr):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(4):
        a,b = x-1,y-1
        for _ in range(1, Point):
            Arr[a+dx[i]][b+dy[i]] = 0
    return Arr

def bombafter(n,Arr):
    Newarr = [[0 for i in range(n)] for i in range(n)]
    
    for i in range(n):
        put = n-1
        for j in range(n-1,-1,-1):
            if Arr[j][i] != 0:
                Newarr[put][i] = Arr[j][i]
                put-=1
    return Newarr

solution()
    
