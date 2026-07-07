# file handling
from pytest import mark


file=open('student.txt','w')
file.write('     STUDENT RECORD     \n1. Abby-87\n2. Bobby-88\n3.Charlie-99')
file.close()
file=open('student.txt','r')
file.read()


# loop
file=open('student2.txt','w')
file.write('Emma-87\nDaisy-32\nCharlie-77\nSammy-33')
file.close()
student=[]
file=open('student2.txt','r')
for line in file:
  parts=line.strip().split(',')
  student.append(int(all_marks))
  total=sum(all_marks)
num_students=len(student)
if num_students>0:
  average_mark=total/num_students
else:
  average_mark=0
print('class average=',average_mark)
above_average=0
for all_marks in student:
  if all_marks > average_mark:
    above_average += 1
print('above average students count is :',above_average)

# comprehension
student_marks={'Emma':87,
               'Daisy':32,
               'Charlie':77,
              ' Sammy':33}
top_students=[name for name, mark in student_marks.items() if mark>80]
student_grade={'name':('A'if mark>=90 else
               'B'if mark>=80 else
               'C' if mark>=70 else 'D')for grade in student_marks.items()}
