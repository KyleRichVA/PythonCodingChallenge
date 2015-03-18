__author__ = 'Kyle Richardson'

class Book(object):  # The Book Object, Contains Values of it's title, author, and year of publish.
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):  # Makes it easier to print user readable information on the book.
        return "%s by %s - %s" %(self.title,self.author,str(self.year))

    def enshelf(self,shelf):  # adds this book to a shelf.
        shelf.books.append(self)
        print("%s added to the shelf." %self.title)

    def unshelf(self,library):  # tries to remove a book from a library
        for shelf in library.shelves:
            if self in shelf.books:
                shelf.books.remove(self)
                print("%s removed from the shelf" %self.title)
                return
        else:
            print("The book isn't in the Library")

class Shelf(object):  # The shelf class which is simply a container for books but can report on what it contains.
    def __init__(self):
        self.books = []

    def bookReport(self):
        print("The books on this shelf are:")
        for book in self.books:
            print(book)

class Library(object):  # The library class which is made up of multiple shelves and can report on all the books contained in it.
    def __init__(self,num_shelves):
        self.shelves = []
        for shelf in range(num_shelves):
            self.shelves.append(Shelf())

    def bookReport(self):
        print("The Books In The Library Are:")
        for shelf in self.shelves:
            for book in shelf.books:
                print(book)

    def numShelves(self):
        return len(self.shelves)

#  Create Our Library with 3 shelves
public_library = Library(3)
#  Create 5 different books and add them to various shelves of the library
book1 = Book("1984","George Orwell",1949)
book2 = Book("The Catcher in the Rye","JD Salinger",1951)
book3 = Book("Pride and Prejudice","Jane Austen",1813)
book4 = Book("The Great Gatsby","F. Scott Fitzgerald",1925)
book5 = Book("Of Mice and Men","William Golding",1954)
book1.enshelf(public_library.shelves[0])
book2.enshelf(public_library.shelves[2])
book3.enshelf(public_library.shelves[1])
book4.enshelf(public_library.shelves[0])
book5.enshelf(public_library.shelves[2])
#  unshelf a book and then attempt to unshelf a book that is already unshelfed
book3.unshelf(public_library)
book3.unshelf(public_library)
# reshelf that book to a different shelf.
book3.enshelf(public_library.shelves[0])
# give a full report on what books are on the shelves and how many shelves there are
print("There are %s shelves" %public_library.numShelves())
public_library.bookReport()
# also have a report on one of the shelves.
public_library.shelves[0].bookReport()