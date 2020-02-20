class Book:
    """
    index -> index of the book
    score -> score of the book
    """
    def __init__(self, score, index):
        self.score = score
        self.index = index

    def __eq__(self, other):
        return self.index == other.index


def sort_func(book):
    return book.score
