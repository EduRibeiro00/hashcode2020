from library import Library

class Problem:
    def __init__(self, num_b, num_l, num_d, books, libraries):
        self.num_b = num_b
        self.num_l = num_l
        self.num_d = num_d
        self.books = books
        self.libraries = libraries
        self.librariesResult = []

    def eval(self, library, days_left):
        useful_days = days_left - library.signup
        library.books_count = useful_days * library.ship

        if books_count > len(library.books):
           books_count = len(library.books)

        return sum([book.score for book in library.books[:library.books_count]])

    def print(self):
        print(self.num_b)
        print(self.num_l)
        print(self.num_d)
        print(self.books)
        print(self.libraries)

    def solve(self):

        daysLeft = self.num_d
        librariesResult = []

        while daysLeft > 0 and self.libraries:

            # Evaluate each libraries and get the best
            bestLibrary = self.getBestLibrary(daysLeft)

            # Remove repeated books from other libraries
            for library in self.libraries:
                library.remove_books(bestLibrary.books)

            # Update remaining days
            daysLeft -= bestLibrary.signup

            # Add best library to the result
            self.librariesResult.append(bestLibrary)
            self.libraries.remove(bestLibrary)

        return self.librariesResult

    def getBestLibrary(self, days_left):
        bestLibrary = None
        best = 0

        for library in self.libraries:
            current = self.eval(library, days_left)
            if current > best:
                best = current
                bestLibrary = library

        return bestLibrary


