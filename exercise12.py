# exercise:1 student record manager problem
file=open('student.txt','w')
file.write(' STUDENT FILE \n')
file.write('101,Jhon,85\n')
file.write('102,Emma,92\n')
file.write('103,David,78')
file.close()
file=open('student.txt','a')
file.write('\n104,Charlie,59')
file.close()
file=open('student.txt','r')
file.read()
file.close()
print('Student file successfully created')

# exercise:2 
file=open('sample.txt','x')
file.write('Python is easy.\nFile handling is useful.')
file.close()
file=open('sample.txt','r')
lines=file.readlines()
num_lines=len(lines)
print('number of lines:',num_lines)
data=''.join(lines)
num_words=len(data.split())
print('number of words:',num_words)
num_char=len(data)
print('number of characters:',num_char)

# search a word in a file problem
file=open('language.txt','w')
file.write('Python Java C++ Python SQL Python')
file.close()
file=open('language.txt','r')
data=file.read()
count=data.count('Python')
if count>0:
    print('The word found and occured ',count)
else:
 print('The word not found')

#  employee salary report problem
file=open('employee.txt','w')
file.write('john,25000\nemma,30000\ndavid,28000\nsophia,35000')
file.close()
salaries=[]
file=open('employee.txt','r')
for line in file:
   name,salary=line.strip().split(',')
   salaries.append(int(salary))

   total=sum(salaries)
   average=total/len(salaries)
   highest=max(salaries)
   lowest=min(salaries)

print('total salaries:',total)
print('average salary:',average)
print('highest salary:',highest)
print('lowest salary:',lowest)

#library management system problem
file=open('books.txt','w')
file.write('  books  \nPythom programming\nJava programming\nData structure')
file.close()
file=open('books.txt','a')
file.write('\nC++')
file.close()
file=open('books.txt','r')
file.read()
file.close()
file=open('books.txt','r')
book=file.read()
count=book.count('C++')
if count>0:
   print('book found')
else:
   print('book not found')
file.close()
file=open('books.txt','w')
file.write('  books  \nJava programming\nC++\nData structure')
file.close()