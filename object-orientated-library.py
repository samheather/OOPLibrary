import random

class Item:
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
            self._available = False

    def setOwner(self, memberId):
        self._owner = memberId

    def editItem(self):
        choice = prompt_input("Enter 1 to change Title or 2 to change Author/Artist/Director/Publisher:", (1, 2))
        newData = raw_input("Ok.  What do you want to change it to? ")
        if (choice == 1):
            self._title = newData
        elif (choice == 2):
            self._author = newData

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    def isAvailable(self):
        return self._available

    def getUniId(self):
        return self._uniId

    def getOwner(self):
        return self._owner       

class DVD(Item):
    def __init__(self, title, author, uniId, cert):
        Item.__init__(self, title, author, uniId)
        self._cert = cert
    
    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Director : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner)

    def getCert(self):
        return self._cert

    def setCert(self, cert):
        self._cert = cert

class Book(Item):
    def __init__(self, title, author, uniId, isbn):
        Item.__init__(self, title, author, uniId)
        self.__isbn = isbn

    def setIsbn(self, isbn):
        self.__isbn = isbn

    def getIsbn(self):
        return self.__isbn

    def editBook(self):
        choice = prompt_input("Enter 1 to change title, 2 to change author, 3 to change ISBN:", (1, 2, 3))
        newData = raw_input("Enter the new value: ")
        if (choice ==  1):
            self._title = newData
        elif (choice == 2):
            self._author = newData
        elif (choice == 3):
            self._isbn = newData

    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Author : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner) + ', ISBN : ' + str(self.__isbn)

class CD(Item):
    def __init__(self, title, author, uniId):
        Item.__init__(self, title, author, uniId)
    
    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Artist : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner)

class Game(Item):
    def __init__(self, title, author, uniId, cert):
        Item.__init__(self, title, author, uniId)
        self._cert = cert
    
    def __repr__(self):
        return 'Title : ' + str(self._title) + ', Publisher : ' + str(self._author) + ', Available : ' + str(self._available) + ', ID : ' + str(self._uniId) + ', Owner : ' + str(self._owner)

    def getCert(self):
        return self._cert

    def setCert(self, cert):
        self._cert = cert
        
class Member:
    def __init__(self, uniqId, firstName, surname, postcode):
        self.__uniqId = uniqId
        self.__firstName = firstName
        self.__surname = surname
        self.__postcode = postcode
        self.__currentItems = []

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

    def borrowItem(self, itemId):
        self.__currentItems.append(itemId)

    def __repr__(self):
        return 'Unique ID : ' + str(self.__uniqId) + ', First Name : ' + str(self.__firstName) + ', Surname : ' + str(self.__surname) + ', Postcode : ' + str(self.__postcode) + ', Current Items : ' + str(self.__currentItems)

class Library:
    def __init__(self):
        self.__items = {}
        self.__members = {}
        self.__nextMemId = 0
        self.__nextItemId = 0

    def __getNextMemId(self):
        self.__nextMemId += 1
        return self.__nextMemId

    def __getNextItemId(self):
        self.__nextItemId += 1
        return self.__nextItemId

    def addMember(self, newFirstName, newSurname, newPostcode):
        newId = self.__getNextMemId()
        print "Member ID is: ", newId
        self.__members[newId] = Member(newId, newFirstName, newSurname, newPostcode)

    def editMember(self, memberId):
        choice = prompt_input("Enter 1 to change first name, 2 to change surname, 3 to change postcode:", (1, 2, 3))
        newData = raw_input("Ok.  What do you want to change it to? ")
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
        try:
            print self.__members[memberId]
        except KeyError:
            print 'Member not found'

    def addItem(self):
        itemType = int(raw_input("Enter 1 for DVD, 2 for book, 3 for CD, 4 for game: "))
        title = raw_input("Enter the title: ")
        author = raw_input("Enter the author/artist/director/publisher: ")
        uniId = self.__getNextItemId()
        if (itemType == 1):
            cert = raw_input("Enter the certificate rating: ")
            self.__items[uniId] = DVD(title, author, uniId, cert)
        elif (itemType == 2):
            isbn = raw_input("Enter the ISBN number: ")
            self.__items[uniId] = Book(title, author, uniId, isbn)
        elif (itemType == 3):
            self.__items[uniId] = CD(title, author, uniId)
        elif (itemType == 4):
            cert = raw_input("Enter the certificate rating: ")
            self.__items[uniId] = Game(title, author, uniId, cert)
        print "Item ID is: ", uniId

    def viewItem(self):
        uniId = int(raw_input("Enter the unique ID of the item whose information you wish to view: "))
        try:
            print self.__items[uniId]
        except KeyError:
            print 'Item not found'

    def removeItem(self):
        uniId = raw_input("Enter the ID of the item that you wish to delete: ")
        self.__items.pop(uniId)

    def rentItem(self, itemId, memId): # Think there may be a scope issue
        item = self.__items[itemId]
        member = self.__members[memId]
        if not item.isAvailable():
            print "Item unavailable"
        else:
            item.setOwner(memId)
            item.setUnavailable()
            member.borrowItem(itemId)

    def returnItem(self, itemId, memId):
        pass
        
##                          UPDATED TO HERE, UNTESTED UP TO HERE.

def prompt_input(question, acceptedAnswers):
    ans = raw_input(question + " ")
    if isinstance(acceptedAnswers[0], int):
        ans = int(ans)
    if ans in acceptedAnswers:
        return ans
    else:
        print random.choice(["Can't you even follow basic instructions?", "Follow the instructions dumbo", "Not a valid choice"])
        return prompt_input(question, acceptedAnswers)

def startApp():
    while True:
        choiceCat = prompt_input("Enter 1 for member functions, 2 for item functions or 3 to rent/return:", (1, 2, 3))
        if (choiceCat == 1):
            memberFunctions()
        elif (choiceCat == 2):
            itemFunctions()
        elif (choiceCat == 3):
            checkInOut()

def memberFunctions():
    choiceFunct = prompt_input("Enter 1 to create a member, 2 to view a member's information or 3 to delete a member:", (1, 2, 3))
    if (choiceFunct == 1):
        firstName = raw_input("Enter their First Name: ")
        lastName = raw_input("Enter their Surname: ")
        postcode = raw_input("Enter their postcode: ")
        myLibrary.addMember(firstName, lastName, postcode)
    elif (choiceFunct == 2):
        memberId = int(raw_input("Enter the ID of the member whose information you wish to view: "))
        myLibrary.viewMember(memberId)
    elif (choiceFunct == 3):
        memberId = int(raw_input("Enter the ID of the member to delete: "))
        myLibrary.deleteMember(memberId)

def itemFunctions():
    choiceFunct = prompt_input("Enter 1 to create an item, 2 to view an item's information or 3 to delete an item:", (1, 2, 3))
    if (choiceFunct == 1):
        myLibrary.addItem()
    elif (choiceFunct == 2):
        myLibrary.viewItem()
    elif (choiceFunct == 3):
        myLibrary.removeItem()

def checkInOut():
    choiceFunct = prompt_input("Enter 1 to rent or 2 to return:", (1, 2))
    if (choiceFunct == 1):
        itemId = int(raw_input("Enter item ID: "))
        memId = int(raw_input("Enter member ID: "))
        myLibrary.rentItem(itemId, memId)
    elif (choiceFunct == 2):        
        itemId = int(raw_input("Enter item ID: "))
        memId = int(raw_input("Enter member ID: "))
        myLibrary.returnItem(itemId, memId)


myLibrary = Library()
##myLibrary.addDvd('Pirates of', 'John')
##myLibrary.viewDvd(0)
##myLibrary.editMember(0)
##myLibrary.viewMember(0)
##my_dvd = dvd('Hi', 'Sam', '1')
##my_dvd

startApp()
