# Exercise 1: Safe Division Calculator
try:
    a=int(input('enter a number:'))
    b=int(input('enter a number:'))
    division=int(a/b)
    print(division)
except ValueError:
    print('only numeric input')
except ZeroDivisionError:
    print('cannot be divided by zero')
finally:
    print('safe division has been created successfully')

# Exercise 2: List Index Access
try:
    fruits=['apple','banana','cherry','orange','durian']
    print( fruits[6])
except ValueError:
    print('invalid index')
except IndexError:
    print('index doesnot exists')
 
# Exercise 3: Read a File Safely
filename=input('enter the file name:')
try:
    file=open(filename,'r')
    file.read()
except FileNotFoundError:
    print('file is not found')
except PermissionError:
    print('you donot have permission to open the file')
finally:
    print('File operation completed.')

# Exercise 4: Student Marks Validator
mark=int(input('enter mark:'))
try:
        if mark>0 and mark>100:
          print('value error')
        if mark>=90:
           print('A grade')
        elif mark>=75:
           print('B grade')
        elif mark>=50:
           print('C grade')
        else:
           print('fail')

except ValueError:
     print('value does not exists')

# Exercise 5: Bank Withdrawal System (Custom Exception)
class InsufficientBalanceError(Exception):
    pass
balance=5000
try:
    user_input=input('enter the amount:')
    amount=float(user_input)
    if amount>balance:
        raise InsufficientBalanceError('you donot have that much ammount')
    balance-=amount
    print(balance)
except InsufficientBalanceError:
    print('you donot have that much ammount')
except ValueError:
    print('value does not found')
finally:
    print('thank you for with drawing money')