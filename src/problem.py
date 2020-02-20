class Problem:
    def __init__(self, num_b, num_l, num_d, books, libraries):
        self.num_b = num_b
        self.num_l = num_l
        self.num_d = num_d
        self.books = books
        self.libraries = libraries


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
            
            librariesOrdered = evaluateLibraries(self.libraries)
            bestLibrary = librariesOrdered.getMax()
            freeDays -= bestLibrary.signup
            librariesResult.append(bestLibrary)
            



