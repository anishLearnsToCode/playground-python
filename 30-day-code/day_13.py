from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


class MyBook(Book):
    price = 0

    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f'Price: {price}')
