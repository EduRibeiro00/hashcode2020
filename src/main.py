import sys
from read_input import parse_input

def main(argv):
    problem = parse_input("a_example.txt")
    problem.print()
    result = problem.solve()
    with open("output/" + "a_example.txt", "w") as output:
        output.write(result.length + "\n")
        for library in result:
            output.write(library.index + " ")
            output.write(library.books_count + "\n")
            for book in library.books[:library.books_count]:
                output.write(book.index + " ")
            output.write("\n")

if __name__ == "__main__":
    main(sys.argv[1:])