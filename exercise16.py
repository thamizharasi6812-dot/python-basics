# file haandling
# 1. Count Lines, Words, and Characters
file=open('language.txt','r')
lines=file.read()
num_lines=lines.count(lines)
data=''.join(lines)
num_words=len(data.split())
num_char=len(lines)
file.close()

# 2. Copy File Contents
file=open('source.txt','w')
file.write('python is a source of learning program')
file.close()
file=open('source.txt','r')
data=file.read()
file=open('destination.txt','x')
file.write(data)
file.close()
print('file copied successfully')

# 3. Append User Input to a File
file=open('notes.txt','w')
file.write('be proud to be who you are\n')
file.close()
data=input('enter the notes:')
file=open('notes.txt','a')
file.seek(0)
file.write( data)
file.close()
file=open('notes.txt','r')
file.read()

# 4. Find a Word in a File
word=input('enter a word:')
file=open('notes.txt','r')
data=file.read()
count=data.count(word)
print(word,':',count)
file.close()

# 5. Number Each Line
def number_line(input_file,output_file):
    infile=open(input_file,'r')
    outfile=open(output_file,'w')
    for line_num,line in enumerate(infile,start=1):
        outfile.write(f"{line_num}:{line}")
number_line('language.txt','language2.txt')

# 6. Remove Empty Lines
file=open('series.txt','w')
file.write('\nbad       buddy\n     we  are\nticket to    heaven')
file.close()
infile=open('series.txt','r')
outfile=open('series3.txt','w')
for line in infile:
   if line.strip():
       outfile.write(line)
outfile.close()
infile.close()

# 7. Store Student Marks
file=open('student2.txt','w')
for i in range(5):
    name=input('enter the student name:')
    mark=int(input('enter the mark:'))
    file.write(f"{name},{mark}\n")    
    file.close()
file=open('student2.txt','r')
file.read()
file.close()
marks=[]
file=open('student2.txt','r')
for line in file:
 name,mark=line.strip().split(',')
 mark=int(mark)
 marks.append(mark)
 print(marks)
highest=max(marks)
lowest=min(marks)
average=int(sum(marks)/len(marks))
print('highest mark=',highest)
print('lowest mark=',lowest)
print('average=',average)

# 8. Merge Two Files
outfile=open('merge.txt','w')
file=open('notes.txt','r')
data=file.read()
file=open('language.txt','r')
line=file.read()
text=data,line
outfile.write(str(text))
outfile.close()

# 9. Create a Simple To-Do List Manager
file=open('todo.txt','w')
file.write(   'TO-DO list\n1.buy vegetables\n2.pay bills\n3.wash the car')
file.close()
file=open('todo.txt','a')
file.write('\n4.cook meal')
file.close()
file=open('todo.txt','r')
file.read()
file.close()

# 10. Analyze a Log File
file=open('report.txt.','w')
file.write('INFO Login successful\n')
file.write(' ERROR Invalid password\n')
file.write('NFO Data loaded\n')
file.write('ERROR Database connection failed')
file.close()
file=open('report.txt.','r')
lines=file.read()
num_info=lines.count('INFO')
print('number of INFO :',num_info)
num_error=lines.count('ERROR')
print('number of ERROR:',num_error)
file.close()

