# creating a employee class
class Employee:
    def __init__(self):
        self.__salary = 0
    def set_salary(self,salary):
        self.set_salary=salary
    def get_salary(self):
        return self.set_salary
    
class Manager(Employee):
    def __init__(self,team_size):
        super().__init__()
        self.team_size=team_size
    def display(self):
        print('Manager')
        print('set_salary:',self.set_salary)
        print('team_size:',self.team_size)

class Developer(Employee):
    def __init__(self,programming_language):
        super().__init__()
        self.programming_language=programming_language
    def display(self):
        print('Developer')
        print('programming_language:',self.programming_language)
        print('set_salary:',self.set_salary)

m=Manager(10)
m.set_salary(100000)
m.display


d=Developer('Java')
d.set_salary(80000)
d.display()


# libary class
from abc import ABC, abstractmethod

class LibraryOperations(ABC):

    @abstractmethod
    def borrow_book(self, book):
        pass


# Book Class
class Book:
    def __init__(self, name):
        self.name = name
        self.available = True

class Member(LibraryOperations):
    def __init__(self, name):
        self.name = name
        self.__limit = 3
        self.borrowed = []

    def borrow_book(self, book):
        if len(self.borrowed) >= self.__limit:
            print("Borrow limit reached!")
        elif book.available:
            book.available = False
            self.borrowed.append(book)
            print(self.name, "borrowed", book.name)
        else:
            print("Book not available.")

    def return_book(self, book):
        if book in self.borrowed:
            book.available = True
            self.borrowed.remove(book)
            print(self.name, "returned", book.name)

class PremiumMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.Member_limit = 5  

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(book.name)


# Main Program
library = Library()

b1 = Book("Python")
b2 = Book("Java")
b3 = Book("C++")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.display_books()

member = Member("Poojha")
premium = PremiumMember("Thamizh")

member.borrow_book(b1)
premium.borrow_book(b2)

library.display_books()

member.return_book(b1)

library.display_books()