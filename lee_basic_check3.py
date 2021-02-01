my_str = input()
answer = ""
count = 1
for i in range(len(my_str)-1):
    if my_str[i] == my_str[i+1]:
        count += 1
    else:
        answer += (my_str[i]+str(count))
        count = 1
answer += (my_str[-1]+str(count))
print(len(answer))
print(answer)
