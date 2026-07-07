# to display square using loop
n=10
for i in range(1,5):
    print('*'*(n-1))

#to display square using nested loop
for i in range(1,5):
    for j in range(n-i):
        print('*',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()

#to display triangle using loop
n=5
for i in range(1,n+1):
    print(' '*(n-i)+" * "*i)

#to display triangle using nested loop

for i in range(1,5):
    for j in range(n-i):
        print(" ",end='')
    for k in range(i):
        print("*",end=" ")
    print()

a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)
for i in range(5):
    print(i)

b=[i for i in range(1,6)]