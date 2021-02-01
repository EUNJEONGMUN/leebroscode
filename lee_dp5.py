import sys
n = int(input())
arr = [0]+(list(map(int,input().split())))
INT_MIN = -sys.maxsize
dp = [-sys.maxsize for _ in range(len(arr)+1)]
dp[0] = 0


for i in range(1,n+1):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        if arr[j]<arr[i]:
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))
