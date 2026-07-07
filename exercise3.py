#operators 

#arithmetic operators
a=100
b=50
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a//b) #floor division
print(a%b)  #modulus
print(a**b) #exponentiation

#assingment operator
a=10
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a//=5
print(a)
a%=5
print(a)
a**=5
print(a)

#relational operator
a=17
b=45
print(a==b)
print(a!=b)
print(a>10 ,b>30)
print(a<12,b<60)
print(a>=b)
print(a<=b)

#logical operator
a=10
b=15
print(a>1 and b>4)
print(a>5 or b>17)
print(not a>b)

#identity operator
a=3
b=3
print(a is b)
print( a is not b)

#membership operator
string='tamil is a language'
print('tamil' in string)
print('tamil' not in string)

#bitwise operator
a=6 #110
b=7 #111
print(a&b)
print(a|b)
print(a^b)
print(~a,~b)