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
        print("Enter the name of the Book you want:")
        