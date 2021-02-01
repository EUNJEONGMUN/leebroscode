'''
# 방법1
from collections import Counter

list1 = input()
list2 = input()

list1 = dict(Counter(list1))
list2 = dict(Counter(list2))

if list1 == list2:
    print("Yes")
else:
    print("No")
'''

#방법2
list1 = list(input())
list2 = list(input())

list1.sort()
list2.sort()

if list1 == list2:
    print("Yes")
else:
    print("No")
