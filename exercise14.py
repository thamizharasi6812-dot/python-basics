# convert names to uppercase
names = ["arun", "kavi", "swetha", "ravi"]
names=list(map(lambda x:x.upper(),names))
print(names)

# find the square number
nums=[2,4,6,8,10]
square=list(map(lambda x:x*x,nums))
print(square)

# filter even numbers
nums = [11, 22, 33, 44, 55, 66, 77, 88]
even= list(filter(lambda x:x%2==0,nums ))
print(even)

# filter long words
words = ["cat", "elephant", "dog", "developer", "ai"]
long_words=list(filter(lambda x:len(x)>5,words))
print(long_words)

# sort students by mark
students = [("Ravi", 85),
           ("Kumar", 92),
           ("Priya", 78)]
students=sorted(students,key=lambda x:x[1],reverse=False)
print(students)

# sort product by price
products = [
    ("Mouse", 500),
    ("Keyboard", 1200),
    ("Monitor", 15000),
    ("Speaker", 3000)]
products=sorted(products,key=lambda x:x[1],reverse=True)
print(products)