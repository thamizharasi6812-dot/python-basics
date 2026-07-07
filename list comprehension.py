#list comprehension is a way to create anew list from existing iteratable tuple,list,range
#it is faster and more understable the for loop
#syntax=[expression for iteam in iterable if condition]

#basic list comprehension (simple type of list comprehension):
a=[x/2 for x in range(6)]   

#list comprehension with if condition(filtering):
a=['apple','banana','cashew','durian']
fruits=[b for b in a if b=='apple']

# list comprehension with if else(transformation):
a=[1,2,3,4,5,6,7]
number=['even' if a % 2 == 0 else 'odd' for a in a]

# nested list comprehension :
numbers=[ [i for i in range(4)]  for j in range(5)]