DATABASE_FILE = "./database/books.txt"
# DATABASE_FILE = "demo.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        db.write('')
        
def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
    db = open(DATABASE_FILE , 'w')
    db.write(f'{title},{author}')

def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    with open(DATABASE_FILE , 'r') as db:
        db = db.readlines()
        for book in db:
            book = book.replace('\n' , '')
            book = book.split(',')
            if title == book[0]:
                return {"title":book[0] , "author":book[1]}
        # db = list(db)
        


def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    with open(DATABASE_FILE , 'r') as db:
        db = db.readlines()
        books = []
        for index , book in enumerate(db):
            if index == 0:
                continue
            book = book.replace('\n' , '')
            book = book.split(',')
            books.append({"title":book[0] , "author":book[1]})
            
        return books
        

# print(search_book("1984"))