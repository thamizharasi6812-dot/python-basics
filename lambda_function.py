# lambda function
# square of numbers
square=lambda x:x*x
print(square(5))
# find the largest number
number=lambda a,b:'a is greates'if a>b else 'b is greates'
print(number(44,82))
# sort
name=['abby','ava','anju','daniel','joseph']
name=sorted(name,key=lambda x:len(x))
print(name)
# sort student by marks
students =[("Ravi", 85),
    ("Kumar", 92),
    ("Priya", 78)]
students=sorted(students,key=lambda x:x[1],reverse=True)
print(students)