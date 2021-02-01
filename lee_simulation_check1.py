def solution():
    n, m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    max_sum = 0

    for i in range(n):
        for j in range(m):
            for x in range(n):
                for y in range(m):
                    
                    arrsum = 0
                    if x+i>=n or y+j >= m:
                        break
                    
                    for a in range(x,x+i+1):
                        for b in range(y,y+j+1):
                            if arr[a][b] < 0:
                                arrsum = 0
                                break
                            else:
                                arrsum += 1
                    max_sum = max(max_sum, arrsum)
                                
    return max_sum                  

print(solution())                            