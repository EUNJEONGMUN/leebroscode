n, m = map(int, input().split())

answer = [[0 for _ in range(m)] for _ in range(n)]
num = 1
x, y = 0, 0
while True:

    answer[x][y] = num

    if x==n-1 and y == m-1:
        break
    
    if y == 0:
        if x>=m-1:
            y = m-1
            x = x+1-y
        else:
            x, y = y, x+1          
    elif x == n-1:
        temp = x+y
        y = m-1
        x = temp+1-y
    else:
        x, y = x+1, y-1

    num += 1


for elem in answer:
    for i in range(len(elem)):
        print(elem[i], end=' ')
    print()
