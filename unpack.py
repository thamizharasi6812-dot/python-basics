# create a function using *args that finds the largest number
def numbers(*args):
    return max(*args)
numbers(89,55,66)

# create a function using*args that calculates the average
def average_num(*args):
    return int(sum(args)/len(args))
average_num(55,83,66)

# create a function using **kwargs that prints employee details
def employee(**kwargs):
    for name,emp_id in kwargs.iteam():
      print(name,emp_id)
employee('Alice',1234)

# unpack
data = ["Python", "Java", "C++"]
a,b,c = data
print(a)
print(b)
print(c)