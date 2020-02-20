from library import Library

class Problem:
    def __init__(self, num_b, num_l, num_d, books, libraries):
        self.num_b = num_b
        self.num_l = num_l
        self.num_d = num_d
        self.books = books
        self.libraries = libraries

    def eval(self, library, days_left):
        useful_days = days_left - library.signup
        books_count = useful_days * library.ship

        return sum([book.score for book in library.books])

    def print(self):
        print(self.num_b)
        print(self.num_l)
        print(self.num_d)
        print(self.books)
        print(self.libraries)

    def getBestLibrary(self, days_left):
        bestLibrary = None
        best = 0

        for library in self.libraries:
            current = self.eval(library, days_left)
            if current > best:
                best = current
                bestLibrary = library

        return bestLibrary
