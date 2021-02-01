start, end = input().split()
start, end = int(start), int(end)

count = 0

for i in range(start, end+1):
    numsum = 0
    for n in range(1, i):
        if i%n == 0:
            numsum += n
    if i == numsum:
        count += 1
        
print(count)
            
