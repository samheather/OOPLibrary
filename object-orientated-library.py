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
        if (self._available == True):
            print 'Error - already set to this'
        else:
            self._availabe = True

    def setUnavailable(self):
        if (self._available == False):
            print 'Error - already set to this'
        else:
            self._unavailable = False

    def setOwner(self, memberId):
        self._owner = memberId

    def editItem(self):
        choice = input("Enter 1 to change Title, 2 to change Author/Artist/Director/Publisher.")
        while choice not in (1, 2):
            print "Can't you even follow basic instructions?"
            choice = input("Enter 1 to change Title, 2 to change Author/Artist/Director/Publisher.")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self._title = newData
        elif (choice == 2):
            self._author = newData

##              ADD IN APPROPRIATE GET METHODS FOR INFORMATION        

class dvd(item):
    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Director : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner)

class book:
    def __init__(self, isbn):
        self.__isbn = isbn

    def setIsbn(self, isbn):
        self.__isbn = isbn

    def getIsbn(self):
        return self.__isbn

    def editBook(self):
        choice = raw_input("Enter 1 to change title, 2 to change author, 3 to change ISBN: ")
        while choice not in (1, 2, 3):
            print "Can't you even follow basic instructions?"
            choice = raw_input("Enter 1 to change title, 2 to change author, 3 to change ISBN: ")
        newData = raw_input("Enter the new value: ")
        if (choice ==  1):
            self._title = newData
        elif (choice == 2):
            self._author = newData
        elif (choice == 3):
            self._isbn = newData

    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Author : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner) + ', ISBN : ' + str(self.__isbn)

class cd(item):
    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Artist : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner)

class game(item):
    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Publisher : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner)

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
        self.__items = []

    def addMember(self, newFirstName, newSurname, newPostcode):
        newId = len(self.__members)
        print "Member ID is: ", newId
        self.__members.append(member(newId, newFirstName, newSurname, newPostcode))

    def editMember(self, memberId):
        choice = input("Enter 1 to change first name, 2 to change surname, 3 to change postcode")
        while choice not in (1, 2, 3):
            print "Can't you even follow basic instructions?"
            choice = input("Enter 1 to change first name, 2 to change surname, 3 to change postcode")
        newData = raw_input("Ok.  What do you want to change it to?")
        if (choice == 1):
            self.__members[memberId].changeFirstName(newData)
        elif (choice == 2):
            self.__members[memberId].changeSurname(newData)
        elif (choice == 3):
            self.__members[memberId].changePostcode(newData)

    def deleteMember(self, memberId):
        self.__members.pop(memberId)

    def viewMember(self, memberId):
        '''takes memberId as an input, prints member info'''
        print self.__members[memberId]

    def addItem(self):
        itemType = raw_input("Enter 1 for dvd, 2 for book, 3 for cd, 4 for game: "):
        title = raw_input("Enter the title: ")
        author = raw_input("Enter the author/artist/director/publisher: ")
        uniId = raw_input("Enter the unique ID: ")
        if self.__items.has_key(uniId):
            print 'That key is not unique'
        else:
            if (itemType == 1):
                self.__items[uniId] = dvd(title, author, uniId)
            elif (itemType == 2):
                isbn = raw_input("Ente hte ISBN number: ")
                self.__items[uniId] = book(title, author, uniId, isbn)
            elif (itemType == 3):
                self.__items[uniId] = cd(title, author, uniId)
            elif (itemType == 4):
                self.__items[uniId] = game(title, author, uniId)

    def viewItem(self):
        uniId = raw_input("Enter the unique ID of the item whose information you wish to view: ")
        print self.__items[uniId]

    def removeItem(self):
        uniId = raw_input("Enter the ID of the item that you wish to delete: ")
        self.__items.pop(uniId)
        
##                          UPDATED TO HERE, UNTESTED UP TO HERE.

def startApp():
    while True:
        choiceCat = int(raw_input("Enter 1 for member functions, 2 for item functions or 3 to rent/return"))
        while choiceCat not in (1, 2, 3):
            print "Follow the instructions dumbo"
            choiceCat = int(raw_input("Enter 1 for member functions, 2 for item functions or 3 to rent/return"))
        if (choiceCat == 1):
            memberFunctions()
        elif (choiceCat == 2):
            itemFunctions()
        elif (choiceCat == 3):
            checkInOut()

def memberFunctions():
    choiceFunct = int(raw_input("Enter 1 to create a member, 2 to view a members information and 3 to delete a member"))
    if choiceFunct not in (1, 2, 3):
        print "Follow the instructions dumbo"
        choiceFunct = int(raw_input("Enter 1 for member functions, 2 for item functions or 3 to rent/return"))
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
    if choiceFunct not in (1, 2, 3):
        print "Follow the instructions dumbo"
        choiceFunct = int(raw_input("Enter 1 for member functions, 2 for item functions or 3 to rent/return"))
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
        
        
##myLibrary = library()
##myLibrary.addDvd('Pirates of', 'John')
##myLibrary.viewDvd(0)
##myLibrary.editMember(0)
##myLibrary.viewMember(0)
##my_dvd = dvd('Hi', 'Sam', '1')
##my_dvd
