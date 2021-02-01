def count(x,y,ggrid):
    gold = 0
    for i in range(x,x+3):
        for j in range(y,y+3):
            if ggrid[i][j] == 1:
                gold += 1
    return gold
            

def solution():
    n = int(input())
    grid = []
    answer = 0
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    for i in range(n-2):
        for j in range(n-2):
            num = count(i,j,grid)
            answer = max(num,answer)
    return answer

print(solution())
            
            
