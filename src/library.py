from book import Book, sort_func

class Library:
    """
    n_books -> number of books in library
    signup -> signup cost in days
    ship -> number of books it can ship per day
    books -> list of books it contains
    """
    def __init__(self, line1, line2, index):
        self.index = index
        self.books = [int(i) for i in line2.split(" ")]
        [self.n_books, self.signup, self.ship] = [int(i) for i in line1.split(" ")]
        self.sort_books()

    def sort_books(self):
        self.books.sort(key=sort_func)
