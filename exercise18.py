# count vowels in a string
def count_vowels(input_string):
    vowels='aeiou'
    count=0
    for char in input_string:
        if char in vowels:
            count+=1
    else:
       return count
count_vowels('programming')

# 2. Find the Second Largest Number
n=[5]
num=[10,20,30,40,50]
second_largest=sorted(set(num))
print(second_largest[-2])

# 3. Remove Duplicate Elements
num=[1,2,2,3,4,4,5]
new_num=sorted(set(num))
print(new_num)

# 4. Check for Palindrome
word_1='madam'
if word_1==word_1[::-1]:
    print('the string is palindrome')
else:
    print('the string is not palindrome')

# 5. Count Word Frequency
text='python is easy python is powerful'
a=text.split()
dict_1={}
dict_1[a[0]]=a.count(a[0])
dict_1[a[1]]=a.count(a[1])
dict_1[a[2]]=a.count(a[2])
dict_1[a[3]]=a.count(a[3])
dict_1[a[4]]=a.count(a[4])
dict_1[a[5]]=a.count(a[5])
print(dict_1)

# 6. Sort Tuples by Second Element
students = [
    ("Arun", 85),
    ("Kavi", 92),
    ("Swetha", 78)]
students.sort(key=lambda x:x[1])
print(students)

# 7. Find Common Elements
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
a=set(list1)
b=set(list2)
a.intersection(b)

# 8. Generate Prime Numbers
n=int(input('enter a number:'))
for num in range(2,n+1):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
           is_prime=False
           break
    if is_prime:
        print(num,end='')

# 9. Employee Salary Analysis
employees = {
    "Arun": 35000,
    "Kavi": 50000,
    "Swetha": 45000}
name=max(employees,key=employees.get)
print(name,employees[name])

# 10. Email Validation
import re
email=input('enter a email:')
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/'
if re.match(pattern,email):
    print('valid email')
else:
    print('invalid email')

