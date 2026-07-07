# list comprehension
# create a list comprehension to display only the even numbers from 1 to 20
even=[x for x in range(1,21) if x%2==0]  # even numbers

#create a list comprehension to display only odd numbers from 1 to 25
odd=[x for x in range(26) if x%2==1]    #odd numbers

# create alist comprehension to display square of number from 1 to 10
square=[x**2 for x in range(11)]     # square numbers

# to convert all iteam in a list to upper case
name=['arun','swetha','kavi','ravi']
name=[x.upper() for x in name]       # uppercase

#to display only the first letter of the fruits
fruits=['apple','banana','cherry','orange']
fruits=[fruit[0]for fruit in fruits]