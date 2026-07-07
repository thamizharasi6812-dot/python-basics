#condition
# program to check if a man is able to vote or not
age=int(input('Enter the age:'))
if age >= 18:
    print('man can vote')
else:
    print('man cannot vote')    

# program to find the greatest number between two numbers using if elif
a=25
b=30
if a==b:
    print('a is equal to b')
elif a>b:
    print('a is greater than b')
else:
    print('a is less than b')

# program to find the greatest number between three numbers using if elif
a=35
b=20
c=50
if a>b and a>c:
    print('a is greater')
elif b>a and b>c:
    print('b is greater')
else:
    print('c is greater')

# program to find the greatest number between three number using nested if 
a=35
b=60
c=70
if a>b:
    if a>c:
        print(' a is greater') 
    else:
        print('c is greater') 
else:
    if c>b:
        print(' c is greater')  
    else:
        print('b is greater')

# program to create a calculator using if elif
num_1=int(input('Enter a number1:'))
num_2=int(input('Enter a number2:'))
operation=int(input('select an opertion (1-4):'))
if operation==1:
    print(num_1+num_2)
elif operation==2:
    print(num_1-num_2)
elif operation==3:
    print(num_1*num_2)
elif operation==4:
    print(num_1/num_2)
else:
    print('invalid input')

# program to create a list of fruits and perform some operations
fruits=['banana','apple','jackfruit','papaya']
fruits.append('orange')
fruits.insert(2,'mango')
fruits.remove('apple')
fruits.sort()
fruits.reverse()

# create a list of subject and perform some operations
subject=['Tamil','English','Maths','Science','Social']
subject[3]='Computer'
subject.index('Tamil')
total_subject=len(subject)
print(total_subject)
