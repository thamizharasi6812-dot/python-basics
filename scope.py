# scope
# use global to modify variable
num=530
def modify_global():
    global num
    num=531
    print(num)
modify_global()
print(num)

# create nested function using nonlocal
def outer_function():
    quotes='freedom is the oxygen of the soul'
    def inner_function():
        nonlocal quotes
        quotes='do what you love'
        print(quotes)
    inner_function()
    print(quotes)
outer_function()

hero = "Superman"
 
def director_office():
    hero = "Batman"
 
    def shooting_spot():
        print(hero)
 
    shooting_spot()
 
director_office()



 
