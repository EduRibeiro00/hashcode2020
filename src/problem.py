class Problem:
    def __init__(self, num_b, num_l, num_d, books, libraries):
        self.num_b = num_b
        self.num_l = num_l
        self.num_d = num_d
        self.books = books
        self.libraries = libraries
        self.librariesResult = []

    def print(self):
        print(self.num_b)
        print(self.num_l)
        print(self.num_d)
        print(self.books)
        print(self.libraries)

    def solve(self):
        
        freeDays = self.num_d
        librariesResult = []

        while(freeDays != 0):
            
            # Evaluate each libraries
            librariesOrdered = evaluateLibraries(self.libraries)
            bestLibrary = librariesOrdered.getMax()

            bookIndexes = [book for book in bestLibrary.books]

            for library in self.libraries:
                library.removeBooks(bookIndexes)

            freeDays -= bestLibrary.signup
            self.librariesResult.append(bestLibrary)
            self.libraries.remove(bestLibrary)





