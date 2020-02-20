import sys
from read_input import parse_input

def main(argv):
    problem = parse_input("a_example.txt")
    problem.print()
    problem.solve()


if __name__ == "__main__":
    main(sys.argv[1:])