class item:
    def __init__(self, title, author, uniId):
        self._title = title
        self._author = author
        self._available = True
        self._uniId = uniId
        self._owner = None

    def setTitle(self, title):
        self._title = title

    def setAuthor(self, author):
        self._author = author

    def setAvailable(self):
        if (self._available = True):
            print 'Error - already set to this'
        else:
            self._availabe = True

    def setUnavailable(self):
        if (self._available = False):
            print 'Error - already set to this'
        else:
            self._unavailable = False

    def setOwner(self, memberId):
        self._owner = memberId

class dvd:
    def __init__(self, title, director, identifier):
        self.__title = title
        self.__director = director
        self.__available = True
        self.__identifier = identifier
        self.__owner = None

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getDirector(self):
        return self.__director

    def setDirector(self, director):
        self.__director = director

    def available(self):
        return self.__available

    def __repr__(self):
        return 'Title : ' + str(self.__title) + ', Director : ' + str(self.__director) + ', Available : ' + str(self.__available) + ', ID : ' + str(self.__identifier) + ', Owner : ' + str(self.__owner)

class book:
    def __init__(self, title, author, identifier, isbn):
        self.__title = title
        self.__author = author
        self.__available = True
        self.__identifier = identifier
        self.__owner = None
        self.__isbn = isbn

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        self.__author = author

    def available(self):
        return self.__available

    def getIsbn(self):
        return self.__isbn

    def setIsbn(self, isbn):
        self.__isbn = isbn

    def __repr__(self):
        return 'Title : ' + str(self.__title) + ', Author : ' + str(self.__author) + ', Available : ' + str(self.__available) + ', ID : ' + str(self.__identifier) + ', Owner : ' + str(self.__owner) + ', ISBN : ' + str(self.__isbn)

class cd:
    def __init__(self, title, artist, identifier):
        self.__title = title
        self.__artist = artist
        self.__available = True
        self.__identifier = identifier
        self.__owner = None

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getArtist(self):
        return self.__artist

    def setArtist(self, artist):
        self.__artist = artist

    def available(self):
        return self.__available

    def __repr__(self):
        return 'Title : ' + str(self.__title) + ', Artist : ' + str(self.__artist) + ', Available : ' + str(self.__available) + ', ID : ' + str(self.__identifier) + ', Owner : ' + str(self.__owner)

class game:
    def __init__(self, title, publisher, identifier):
        self.__title = title
        self.__publisher = publisher
        self.__available = True
        self.__identifier = identifier
        self.__owner = None

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getPublisher(self):
        return self.__publisher

    def setPublisher(self, publisher):
        self.__publisher = publisher

    def available(self):
        return self.__available

    def __repr__(self):
        return 'Title : ' + str(self.__title) + ', Publisher : ' + str(self.__publisher) + ', Available : ' + str(self.__available) + ', ID : ' + str(self.__identifier) + ', Owner : ' + str(self.__owner)

class member:
    def __init__(self, uniqId, firstName, surname, postcode):
        self.__uniqId = uniqId
        self.__firstName = firstName
        self.__surname = surname
        self.__postcode = postcode
        self.__currentItems = None

    def viewUniqId(self):
        return self.__uniqId

    def viewFirstName(self):
        return self.__firstName

    def changeFirstName(self, firstName):
        self.__firstName = firstName

    def viewSurname(self):
        return self.__surname

    def changeSurname(self, surname):
        self.__surname = surname

    def viewPostcode(self):
        return self.__postcode

    def changePostcode(self, postcode):
        self.__postcode = postcode

    def viewCurrentItems(self):
        return self.__currentItems

    def __repr__(self):
        return 'Unique ID : ' + str(self.__uniqId) + ', First Name : ' + str(self.__firstName) + ', Surname : ' + str(self.__surname) + ', Postcode : ' + str(self.__postcode) + ', Current Items : ' + str(self.__currentItems)

class library:
    def __init__(self):
        self.__dvds = []
        self.__books = []
        self.__cds = []
        self.__games = []
        self.__members = []

    def addMember(self, newFirstName, newSurname, newPostcode):
        newId = len(self.__members)
        print "Member ID is: ", newId
        self.__members.append(member(newId, newFirstName, newSurname, newPostcode))

    def editMember(self, memberId):
        choice = input("Enter 1 to change first name, 2 to change surname, 3 to change postcode")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self.__members[memberId].changeFirstName(newData)
        elif (choice == 2):
            self.__members[memberId].changeSurname(newData)
        elif (choice == 3):
            self.__members[memberId].changePostcode(newData)
        else:
            print "Can't you even follow basic instructions?"

    def deleteMember(self, memberId):
        self.__members.pop(memberId)

    def viewMember(self, memberId):
        '''takes memberId as an input, prints member info'''
        print self.__members[memberId]

    def addDvd(self, newTitle, newDirector):
        newIdentifier = len(self.__dvds)
        print "Identifier is: ", newIdentifier
        self.__dvds.append(dvd(newTitle, newDirector, newIdentifier))

    def editDvd(self, dvdId):
        choice = input("Enter 1 to change Title, 2 to change Director")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self.__dvds[dvdId].setTitle(newData)
        elif (choice == 2):
            self.__dvds[dvdId].setDirector(newData)
        else:
            print "Can't you even follow basic instructions?"

    def viewDvd(self, dvdId):
        '''takes dvdId as an input, prints DVD info'''
        print self.__dvds[dvdId]

    def deleteDvd(self, dvdId):
        self.__dvds.pop(dvdId)

    def addBook(self, newTitle, newAuthor, newIsbn):
        newIdentifier = len(self.__books)
        print "Identifier is: ", newIdentifier
        self.__books.append(book(newTitle, newAuthor, newIdentifier, newIsbn))

    def editBook(self, bookId):
        choice = input("Enter 1 to change Title, 2 to change Author, 3to change Identifier")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self.__books[bookId].setTitle(newData)
        elif (choice == 2):
            self.__books[bookId].setAuthor(newData)
        elif (choice == 3):
            self.__books[bookId].setIsbn(newData)
        else:
            print "Can't you even follow basic instructions?"

    def viewBook(self, bookId):
        '''takes dvdId as an input, prints DVD info'''
        print self.__books[bookId]

    def deleteBook(self, bookId):
        self.__books.pop(bookId)

    def addCd(self, newTitle, newArtist):
        newIdentifier = len(self.__cds)
        print "Identifier is: ", newIdentifier
        self.__cds.append(cd(newTitle, newArtist, newIdentifier))

    def editCd(self, cdId):
        choice = input("Enter 1 to change Title, 2 to change Artist")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self.__cds[cdId].setTitle(newData)
        elif (choice == 2):
            self.__cds[cdId].setArtist(newData)
        else:
            print "Can't you even follow basic instructions?"

    def viewCd(self, cdId):
        '''takes dvdId as an input, prints DVD info'''
        print self.__cds[cdId]

    def deleteCd(self, cdId):
        self.__cds.pop(cdId)

    def addGame(self, newTitle, newPublisher):
        newIdentifier = len(self.__games)
        print "Identifier is: ", newIdentifier
        self.__games.append(game(newTitle, newPublisher, newIdentifier))

    def editGame(self, gameId):
        choice = input("Enter 1 to change Title, 2 to change Publisher")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self.__games[gameId].setTitle(newData)
        elif (choice == 2):
            self.__games[gameId].setPublisher(newData)
        else:
            print "Can't you even follow basic instructions?"

    def viewGame(self, gameId):
        '''takes dvdId as an input, prints DVD info'''
        print self.__games[gameId]

    def deleteGame(self, gameId):
        self.__games.pop(gameId)

def startApp():
    while True:
        choiceCat = int(raw_input("Enter 1 for member functions, 2 for item functions or 3 to rent/return"))
        if (choiceCat == 1):
            memberFunctions()
        elif (choiceCat == 2):
            itemFunctions()
        elif (choiceCat == 3):
            checkInOut()
        else:
            print "Follow the instructions dumbo"

def memberFunctions():
    choiceFunct = int(raw_input("Enter 1 to create a member, 2 to view a members information and 3 to delete a member"))
    if (choiceFunct == 1):
        firstName = raw_input("Enter their First Name:")
        lastName = raw_input("Enter their Surname:")
        postcode = raw_input("Enter their postcode:")
        myLibrary.addMember(firstName, lastName, postcode)
    if (choiceFunct == 2):
        memberId = int(raw_input("Enter the ID of the member whose information you wish to view:"))
        myLibrary.viewMember(memberId)
    if (choiceFunct == 3):
        memberId = int(raw_input("Enter the ID of the member to delete:"))
        myLibrary.deleteMember(memberId)

def itemFunctions():
    choiceFunct = int(raw_input("Enter 1 to create an item, 2 to view an items information and 3 to delete aan item."))
    if (choiceFunct == 1):
        firstName = raw_input("Enter their First Name:")
        lastName = raw_input("Enter their Surname:")
        postcode = raw_input("Enter their postcode:")
        myLibrary.addMember(firstName, lastName, postcode)
    if (choiceFunct == 2):
        memberId = int(raw_input("Enter the ID of the member whose information you wish to view:"))
        myLibrary.viewMember(memberId)
    if (choiceFunct == 3):
        memberId = int(raw_input("Enter the ID of the member to delete:"))
        myLibrary.deleteMember(memberId)
        
        
myLibrary = library()
myLibrary.addDvd('Pirates of', 'John')
myLibrary.viewDvd(0)
myLibrary.editMember(0)
myLibrary.viewMember(0)
##my_dvd = dvd('Hi', 'Sam', '1')
##my_dvd
