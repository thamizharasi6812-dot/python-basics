#string_methode
#capitalize() converts the first letter of the string to uppercase
string_1="thamizharsi"
print(string_1.capitalize())

#casefold() converts the string as caseless string
string_2="ThaMizHarSi"
print(string_2.casefold())

#center() add special characters or numbers infort of the string or at the back of string 
string_3='tamizh'
print(string_3.center(15,'*'))

#count() counts the number times the substring occured in the string
string_4="raja raja chozhan"
print(string_4.count('a'))

#encode() encode the string
string_5='save earth'
print(string_5.encode())

#endswith() returns whether true or false if string ends with the given suffix
string_6="python language"
print(string_6.endswith('e'))
print(string_6.startswith('y'))  #startswith()

#expandtabs() \t is used to leave specified gap between the string
string_7="computer\tscience"
print(string_7.expandtabs())

#find() find the index of the substring
string_8="hopper"
print(string_8.find('o'))
print(string_8.rfind('e'))   #rfind()

#index()  finds the index of the substring in the string
string_9='jasper'
print(string_9.index('p'))
print(string_9.rindex('j'))  #rindex() 

#isalnum() checks given string contains alphabets and number or not 
string_10='may7'
print(string_10.isalnum())

#isalpha() returns true if the string is alphabets 
string_11='danger'
print(string_11.isalpha())

#isdecimal() returns true if the string contains numbers
string_12='10'
print(string_12.isdecimal())

#isdigit() retuns true if all characters are digits
string_13='1234a'
print(string_13.isdigit())

#isidentifier() checks if the string is identifer or not
string_14='variable_name'
print(string_14.isidentifier())

#islower() checks if all charcter in string are in lowercase 
string_15='ticket to heaven'
print(string_15.islower())

#isupper()  checks if all character in a string is uppercase
string_16='JAVA'
print(string_16.isupper())

#isnumeric() returns true if all character in a string are numeric
string_17='12345'
print(string_17.isnumeric())

#isspace() returns true if all character in a string is empty space
string_18=''
print(string_18.isspace())

#istitle() retuns true if the string is in title case
string_19='Python'
print(string_19.istitle())

#lowewr() convert all the character in string to lower case
string_20='TAMIL NADU'
print(string_20.lower())

#upper()  converts all the character in astring to upper case
string_21='tamil nadu'
print(string_21.upper())

#title() convert string to title case
string_22='rupees'
print(string_22.title())

#swapecase() swape the cases of the string
string_23='ViruTHaI'
print(string_23.swapcase())

#format()
name='thamizharasi'
age=17
print("my name is {0} and my age is {1}".format(name,age))

#isprintable() returns true if the string contains numbers,alphabets,special characters
string_24='thamizharasi is a student '
print(string_24.isprintable())

#join() the tuple with specified characters
t=('thamizharsi','python','leaner')
print('*'.join(t))

#strip() 
sentence='thaimzharasi is a student and thamizharasi is good'
print(sentence.strip('thamizharasi '))
print(sentence.lstrip('thamizh'))  #lstrip()
print(sentence.rstrip('good sai'))   #rstrip()

#partion()
string_25='python is a high level language'
print(string_25.partition('high'))
print(string_25.rpartition('python'))

#zfill()
print(string_25.zfill(50))
print(string_25.split('*'))