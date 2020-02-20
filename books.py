import sys

B = 0
L = 0
D = 0
books = []
libraries = []

class Library:
    def __init__(self, line1, line2):
        self.books = [int(i) for i in line2.split(" ")]
        [self.n_books, self.signup, self.ship] = [int(i) for i in line1.split(" ")]
        print(self.books)

def parse_input(file):
    with open("input/" + file, "r") as input:
        lines = input.readlines()
        [B, L, D] = [int(i) for i in lines[0].split(" ")]
        books = [int(i) for i in lines[1].split(" ")]

        lines = lines[2:]
        for idx, line in enumerate(lines):
            if idx % 2 == 0:
                libraries.append(Library(lines[idx], lines[idx + 1]))

def main(argv):
    parse_input(argv[0])











if __name__ == "__main__":
    main(sys.argv[1:])