import sys
n = int(input())
arr = []
dp = [[-1 for _ in range(n)] for _ in range(n)]
INT_MIN = -sys.maxsize
for _ in range(n):
    arr.append(list(map(int,input().split())))

def Initialize():
    dp[0][0] = arr[0][0]
    for i in range(1,n):
        dp[0][i] = dp[0][i-1]+arr[0][i]
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + arr[i][0]

def solution():
    global INT_MIN
    Initialize()

    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]
    for j in range(n):
        INT_MIN = max(INT_MIN, dp[n-1][j])
    print(INT_MIN)

    
solution()

