# recursion function
# print numbers from 1 to 10
def number(n):
    if n==10:
        print(n)
        return
    else:
        print(n)
    number(n+1)
number(1)

# print numbers from10 to 1
def numbers(n):
    if n==1:
        print(n)
        return
    else:
        print(n)
    numbers(n-1)
numbers(10)

# find factorial of number
def factorial(n):
    if n==1:
        return 1
    else:
      return n * factorial(n-1)
print(factorial(6))
