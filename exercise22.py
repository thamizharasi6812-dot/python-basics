# class
class student_record:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def display(self):
            print('name=',self.name)
            print('age=',self.age)
            print('roll_no=',self.roll_no)
    @classmethod
    def school(cls):
         print('school=VIRUTHAI VIKAS MATRIC SCHOOL')
    @staticmethod
    def message():
         print('records saved sucessfully')

s1=student_record('Naveena',15,1102)
s2=student_record('Hema',14,1087)
s3=student_record('Annie',15,1065)

s1.display()
s2.display()
s3.display()
student_record.school()
student_record.message()

class library:
     library_name='bangtan library'
     def __init__(self,book_name,author,price):
          self.book_name=book_name
          self.author=author
          self.price=price
     def display(self):
        print('book name=',self.book_name)
        print('author=',self.author)
        print('price=',self.price)
     @classmethod
     def show_library(cls):
          print('library name=',cls.library_name)
     @staticmethod
     def message():
          print('library is opened.')

b1=library('all the worlds a stage','william shakesphear',450)
b2=library('harry potter','JK.rowling',1100)
b3=library('jujutsu kaisen','gege akutami',3500)
b1.display()
b2.display()
b3.display()
library.show_library()
library.message()

# single inheritance
class Flower:
     def bloom(self):
          print('The flower is blooming')
class Lotus(Flower):
     def colour(self):
          print('Lotus is pink in colour')
f=Lotus()
f.diplay()
f.bloom()
f.colour()

# multiple inheritance

class father:
     def skill(self):
          print('accountance')
class mother:
     def work(self):
          print('teacher')
class child(father,mother):
     def talent(self):
          print('artist')
c=child()
c.display()
c.skill()
c.work()
c.talent()

# multilevel inhertance
class super_senior:
     def notes(self):
          print('python basics notes')
class senior(super_senior):
     pass
class junior(senior):
     pass
j=junior()
j.notes()

# hierarchical inhertance
class mother:
     def food(self):
          print('dinner is dosa')
class brother(mother):
     pass
class sister(mother):
     pass
b=brother()
s=sister()
b.food()
s.food()

# hybrid inhertance
class programming:
     def language(self):
          print('programming language')
class Python(programming):
     def python(self):
          print('python is easy to learn')
class Java(programming):
     def java(self):
          print('java is high level language')
class User(Python,Java):
     def user(self):
          print('user can use both python and java')
u=User()
u.language()
u.python()
u.java()
u.user()