def check_number(number):
    if number%2==0:
        print('even')
    else:
        print('odd')
check_number(67)

def max_number(a,b):
    if a>b:
        print(a)
    else:
        print(b)
max_number(55,78)

def cube(number):
    print(number**3)
cube(5)

def add(a,b,c):
    print(a+b+c)
add(15,66,94)

def square(num):
    print(num**2)
square(6)

def count_character(text):
    print(len(text))
count_character('american music awards')

def small_num(a,b):
    if a>b:
        print('Smaller number is',b)
    else:
        print('Smaller number is',a)
small_num(55,36)

def person_age(age):
    if age>=18:
        print('The person can vote')
    else:
        print('The person cannot vote')
person_age(12)