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
        books_count = useful_days * library.ship

        return sum([book.score for book in library.books])

    def print(self):
        print(self.num_b)
        print(self.num_l)
        print(self.num_d)
        print(self.books)
        print(self.libraries)

    def solve(self):
        
        freeDays = self.num_d
        librariesResult = []

        while(freeDays < 0):
            
            # Evaluate each libraries and get the best
            bestLibrary = self.

            # Get the chosen books
            books = [book for book in bestLibrary.books]

            # Remove repeated books from other libraries
            for library in self.libraries:
                library.removeBooks(books)

            # Update remaining days
            freeDays -= bestLibrary.signup

            # Add best library to the result
            self.librariesResult.append(bestLibrary)
            self.libraries.remove(bestLibrary)





