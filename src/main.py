import sys
from read_input import parse_input

def main(argv):
    problem = parse_input(argv[0])
    problem.print()


if __name__ == "__main__":
    main(sys.argv[1:])