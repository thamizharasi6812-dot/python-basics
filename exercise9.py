#to creat a program to analyze the student exams records
student=[{'name':'Arun','marks':(78,85,90),'language':'Python'},
{'name':'Bob','marks':(65,55,38),'language':'Java'},
{'name':'Charlie','marks':(99,92,89),'language':'C++'}]
all_average={}
for s in student:
 marks=s.get('marks')
 avg=sum(marks)/len(marks)
 all_average[s['name']]=int(avg)
print(all_average)     # average of all students

topper=max(all_average)
print('topper is',topper)  #topper amoung the students

search_name=input('Enter the name to searched:')
for s in student:
 if s['name']==search_name:
     print(search_name,'is found')
     break
else:
    print('student not found')   
     
student_name=input('Enter the name student:')   # to check whether the student have passed or not
for s in student:
   if avg>=50:
    print(student_name,'the student have passed ')
    break
else:
  print(student_name,'the student have failed')

