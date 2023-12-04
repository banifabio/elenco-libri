
class book():
    def __init__(self, title, author='Unknown', volume='', topic='', bookshelf='', comment=''):
        self.title = title
        self.author = author
        self.volume = volume
        self.topic = topic
        self.bookshelf = bookshelf
        self.comment = comment

    def __str__(self):
        name = f'{self.title} "Vol: " {self.volume} - {self.author}, {self.topic}, {self.bookshelf}, {self.comment}'
        return name


class author():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class topic():
    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


class bookshelf():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def mainpage():
    print("\nBooks list\n"
          "Search list (s)\n"
          "Add book (b)\n"
          "Add list (l)\n"
          "Export list (e)\n")
    choice = input("Select an option (default=l): ")
    if choice not in 'sble' or choice == '':
        choice = 'l'

    if choice == 's':
        listpage()
    elif choice == 'b':
        addbookpage()
    elif choice == 'l':
        addlistpage()
    elif choice == 'e':
        exportlistpage()


def listpage():
    print("\nSearch book for\n"
          "Author (a)\n"
          "Title (t)\n"
          "Topic (m)\n"
          "Bookshelf (b)\n"
          "Homepage (h)\n")
    choice = input("Select an option (default=t): ")
    if choice not in 'atmbh' or choice == '':
        choice = 't'

    if choice == 'h':
        mainpage()
    else:
        books = reserch_key(choice)
        print_books(books)
    what_now(listpage)


def reserch_key(choice):
    if choice == 'a':
        reserch_key = input("Insert the author's name: ")
    elif choice == 't':
        reserch_key = input("Insert the title: ")
    elif choice == 'm':
        print("Topic list")
        reserch_key = input("Insert the topic: ")
    elif choice == 'b':
        print("Bookshelf list")
        reserch_key = input("Insert the bookshelf: ")
    books = search_books(choice, reserch_key)
    return books


def search_books(choice, reserch_key):
    # call the database
    return books


def print_books(books):
    for book in books:
        print(book)


def what_now(originpage):
    print("What now?\n"
          "Repeat again (r)\n"
          "Homepage (h)\n")
    choice = input("Select an option (default=h): ")
    if choice not in 'rh' or choice == '':
        choice = 'h'
    if choice == 'h':
        mainpage()
    else:
        originpage()


def addbookpage():
    print("\nAdd a Book\n")
    title = input("Insert title: ")
    author = input("Insert authors: ")  # 'Unknown',
    volume = input("if has more volumes insert volume #: ")
    print("\nTopic avaible:\n"
          "Ingegneria (i)\n"
          "RPG - D&D3 (3)\n")
    topic = input("Insert topic: ")
    print("\nBookshelf avaible:\n"
          "Ar - Corridoio - dx (c)\n"
          "Ar - Studio - aperta (a)\n")
    bookshelf = input("Insert bookshelf: ")
    comment = input("Insert comment: ")
    # create book in database
    # if has more volumes ask for other ones


def addlistpage():
    pass


def exportlistpage():
    pass


if __name__ == '__main__':
    mainpage()
