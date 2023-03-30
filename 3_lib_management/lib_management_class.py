from pathlib import Path

class Library:
    """ An attempt at modelling a library """
    def __init__(self,booklist,name):
        """ Initialize the lib """
        self.booklist = booklist
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        """ Display the books in the library """
        print(f"We have the following books in the library: {self.name}")
        for book in self.booklist:
            print(book)

    def add_book(self, book):
        """ Add books to lib """
        if book in self.booklist:
            print("This book is already in the library.")
        else:
            self.booklist.append(book)
            book_database = open(database_name,'a')
            book_database.write('\n')
            # Get a newline in text file
            book_database.write(book)
            print(f"{book.title()} added to the library.")

    def lend_book(self, book, user):
        """ Updating the lend dictionary with the current user OUT """
        if book in self.booklist:
            if book not in self.lend_dict.keys():
                self.lend_dict.update({book:user})
                print(f"{book.title()} scanned out. Enjoy!")
            else:
                print(f"{book.title()} is currently borrowed by {self.lend_dict[book]}")
        else:
            print(f"Sorry, we do not have {book.title()} in our current library.")

    def return_book(self, book):
        """ Updating the lend dictionary with the current user IN """
        if book in self.lend_dict.keys():
            self.lend_dict.pop(book)
            print(f"Thank you, {book.title()} has been returned.")
        else:
            print(f"{book.title()} does not exist in this library.")

def main():
    while True:

        print(f"Welcome to the {library.name} library")

        choice = """
        1. Display Books
        2. Borrow a book
        3. Add a book to the library
        4. Return a borrowed book
        """

        user_input = input("Press 'q' to quit or 'c' to continue: ")
        
        if user_input.lower() == 'c':
            print(choice)
            user_choice = int(input("Select an option to continue: "))

            if user_choice == 1:
                library.display_books()

            elif user_choice == 2:
                book = input("Please enter the title of the book you would  like to borrow: ")
                user = input("Please enter your name: ")
                library.lend_book(book, user)
            
            elif user_choice == 3:
                book = input("Please enter the title of the book to add to the library: ")
                library.add_book(book)

            elif user_choice == 4:
                book = input("Please enter the title of the book to return: ")
                library.return_book(book)

            else:
                print("Please choose a valid option")

        elif user_input.lower() == 'q':
            break

        else:
            print("Please choose a valid option")

if __name__ =='__main__':
    """ Program Execution """
    bookslist = []
    database_name = input("Enter the name of the database with extension: ")
    book_database = open(database_name,'r')
    for book in book_database:
        bookslist.append(book)
    library = Library(bookslist,'PythonX')  
    main()



""" READ ME File """

thoery = """A simple library management application which will allow the user to do the following - 
- Fetch available books in the library
- Add new books
- Keep track of books already borrowed 
- Update the records when books are returned

This is a project to test and exhibit my use of OOP and to implement some things I've learnt so far.
"""
path = Path('project_concept.txt')
path.write_text(thoery)

""" Creating a library (the hard way..)"""

lib = ['Python Crash Course','Head First Python','Learn Python3 - The Hard Way',
'Think Python''Automate The Boring Stuff with Python']

lib_database = ''

for book in lib:
    lib_database += f"{book}\n"

path = Path('lib_database.txt')
path.write_text(lib_database)

