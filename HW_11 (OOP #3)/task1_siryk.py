'''
Program with a class structure that implements a library.
Classes:
1) Library
2) Book
3) Author
All 3 classes have a readable _repr_ and _str_ methods.
'''


class Author:
    '''
    Class with base info of author, including books list
    '''
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print('Already exist!')

    def aut_check(self, b_name):
        '''
        Checking whether such a book exists with the author
        :param b_name: name of book
        :return: Book object or "False"
        '''
        for i in self.books:
            if i.name == b_name:
                return i
        else:
            return False

    def __repr__(self):
        return f'{self.name} from {self.country} B.D. {self.birthday}'

    def __str__(self):
        return self.name


class Book:
    '''
    A Book class with a class variable which holds the amount of all existing books
    '''
    amount = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        author.add_book(self)
        Book.amount += 1

    def __repr__(self):
        return f'{self.name} {self.year} ({self.author})'

    def __str__(self):
        return f'Book: {self.name}, year:{self.year}, by {self.author}'

    def __len__(self):
        return Book.amount


class Library:
    '''
    Class with author and books lists
    '''
    def __init__(self, name):
        self.name = name
        self.list_books = []
        self.list_authors = []

    def new_book(self, name, year, author: Author):
        '''
        Creates an instance of Book class and adds the book to the books list for the current library
        or adds currently existing Book
        :param name: name of book
        :param year: year of publication
        :param author: Author of book
        '''
        if author.aut_check(name) == False:
            b = Book(name, year, author)
            self.list_books.append(b)
        else:
            self.list_books.append(author.aut_check(name))
        if author not in self.list_authors:
            self.list_authors.append(author)

    def group_by_author(self, author: Author):
        '''
        :return: a list of all books grouped by the specified author
        '''
        if author not in self.list_authors:
            raise IndexError(f'No books by {author} in library!')
        else:
            list_by_aut = [i for i in self.list_books if i.author == author]
            return list_by_aut

    def group_by_year(self, year):
        '''
        :return: a list of all the books grouped by the specified year
        '''
        if year not in [i.year for i in self.list_books]:
            raise IndexError(f'No books from {year} in library!')
        else:
            list_by_y = [i for i in self.list_books if i.year == year]
            return list_by_y

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'Library: {self.name}'


aut1 = Author('first', 'USA', 1909)
aut2 = Author('second', 'USA', 1929)
book1 = Book('book1', 1950, aut1)
book2 = Book('book2', 1960, aut1)

libr = Library('My')
libr.new_book('book3', 1970, aut2)
libr.new_book('book1', 1950, aut1)
libr.new_book('book2', 1960, aut1)
libr.new_book('book4', 1950, aut2)
print(aut1.books)
print(aut2.books)
print(libr.list_authors)
print(libr.list_books)
print(libr.group_by_author(aut2))
print(libr.group_by_year(1950))
print(len(book1))