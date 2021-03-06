class Library:
    def __init__(self,listbooks):
        self.availablebooks = listbooks

    def display_available_books(self):
        print("The books we have in our Library are as follows:")
        print("=================================================")        

        for book in self.availablebooks:
            print(book)
    def lend_books(self , requestedBook):
        if requestedBook in self.availablebooks:
            print("The book you requested has now borrowed")
            self.availablebooks.remove(requestedBook)
        else:
            print("the book isn't in the bookshelf")
    
    def add_book(self , returnBook):
        self.availablebooks.append(returnBook)
        print("Thanks for returning the book!")
class Student:
    def requestedBook(self):
        print("Enter the name of the Book you want to Borrow:")
        self.book = input()
        return self.book
    def returnedBook(self):
        print("Enter the name of the Book you want to Return:")
        self.book = input()
        return self.book


def main():
    Library = Library(["The last Battle " ,"Haary porter" ,"The Great Divorce"])
    student = Student()

    while True:
        print('''################# Library Numbers #########
        
        1.Display Book
        2. Request Book
        3.Return a Book

        4.Exit
        
        
        ''')    
        choice = int(input("Enter Your choice Number:"))

        if choice == 1 :
            Library.display_available_books()
        elif choice == 2 :
            Library.lend_books(student.requestedBook())
        elif choice == 3:
            Library.lend_books(student.returnedBook())

        elif choice == 4:
            Library.exit()            

main()      
            