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
