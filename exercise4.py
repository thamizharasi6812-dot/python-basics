#list[] is ordered,mutable,allow duplicates,indexed

a=[1,2,3,4,5,6,7,8]
b=[1,1,1]
a.append(9)

a.count(5)

a.extend(b)

a.index(7)

a.insert(10,11)

a.pop(11)

a.remove(11)

a.reverse()

a.sort()

a.sort(reverse=True)

a.clear()


#list exercise
a=['orange','apple']
b=['pineapple','banana']
c=a
a.extend(b)
print(c)

#tuple()  is ordered,immutable,allow duplicates,indexed

a=(1,2,3,4,5,6,7,8)
a.count(4)

a.index(8)