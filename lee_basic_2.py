n = int(input())
num = list(map(int, input().split()))

count = 1
my_min = num[0]

for i in range(1,n):
    if my_min == num[i]:
        count += 1
    if my_min>num[i]:
        my_min = num[i]
        count = 1
print(my_min, count)
    
