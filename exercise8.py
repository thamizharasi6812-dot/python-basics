#loop
#for loop 
a=(60,55,87,99)
for iteam in a:
      print(iteam)

a={66,91,30}
for i in a:
    if i>50:
        print('greater')
    else:
        print('lower')

#wlie loop
a=80
while a>=90:
    print('grade a')
    

#to create a program to find multiplication table using loop
num=int(input('Enter the number:'))
start_range=int(input('Enter the start range:'))
end_range=int(input('Enter the end range:'))
print('multiplication table of',num)
for i in range(start_range,end_range,1):
    print(num,'*',i,'=',num*i)

