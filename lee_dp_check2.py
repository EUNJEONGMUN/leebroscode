n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]


def Initialize():
    dp[0][0] = arr[0][0]
    for i in range(1,n):
        dp[0][i] = min(dp[0][i-1], arr[0][i])
    for i in range(1,n):
        dp[i][0] = min(dp[i-1][0], arr[i][0])

def solution():
    Initialize()

    for i in range(1,n):
        for j in range(1,n):
            if (i==n-1 and j==n-2) or (i==n-1 and j==n-1):
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1],arr[i][j])
    print(dp[n-1][n-1])

    
solution()
