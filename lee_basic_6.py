n = int(input())
student = []
for i in range(n):
    h, w = map(int,input().split())
    student.append((h,w,i+1))

student.sort(key = lambda x: (-x[0],-x[1],x[2]))

for elem in student:
    for i in range(len(elem)):
        print(elem[i], end = ' ')
    print()
