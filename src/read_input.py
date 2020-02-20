from library import Library
from problem import Problem
from book import Book

def parse_input(file):
    B = 0
    L = 0
    D = 0
    libraries = []
    books = []

    with open("../input/" + file, "r") as input:
        lines = input.readlines()
        [B, L, D] = [int(i) for i in lines[0].split(" ")]
        book_scores = [int(i) for i in lines[1].split(" ")]

        for idx, score in enumerate(book_scores):
            books.append(Book(score, idx))

        lines = lines[2:]
        for idx, line in enumerate(lines):
            if idx % 2 == 0:
                libraries.append(Library(lines[idx], lines[idx + 1], idx//2))

    return Problem(B, L, D, books, libraries)