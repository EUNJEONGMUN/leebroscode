n = int(input())

tab = [1,1]

for i in range(2,n):
    tab.append(tab[i-2]+tab[i-1])

print(tab[n-1])
    
    

