#"Global" counter variable used to count users...
counter = 0

#Getter for the counter.
#If True is given as an argument, returns it as a string
def getCounter(retStr=False):
    if retStr:
        return str(counter)
    else:
        return counter

#Used to check whether first and last names contain any digits.
#Also checks that the length is > 0
def checkName(nameNew):
    if len(nameNew) == 0:
        return False
    containsDigits = False
    for char in list(nameNew):
        if char.isdigit():
            containsDigits = True
    if containsDigits:
        return False
    else:
        return True

class User:
    #Initializes stuff and sets all of the user's details
    def __init__(self,uname,name,sname,prop):
        global counter
        self.username=""
        self.name=""
        self.surname=""
        self.prop=""
        self.setUname(uname)
        self.setName(name)
        self.setSname(sname)
        self.setProp(prop)
        counter += 1
        #Must increment counter

    #Getters
    def getUname(self):
        return self.username
    def getName(self):
        return self.name
    def getSname(self):
        return self.surname
    def getProp(self):
        return self.prop

    #Setters
    def setUname(self, uname):
        if len(uname) == 0:
            raise TypeError("Not a valid username")
        self.username = str(uname)
    def setName(self, nameGiven):
        if checkName(nameGiven):
            self.name = nameGiven
        else:
            raise TypeError("Not a valid name")
            return
    def setSname(self, Sname):
        if checkName(Sname):
            self.surname = Sname
        else:
            raise TypeError("Not a valid surname")
            return
    def setProp(self, prop):
        try:
            self.prop = int(prop)
            if self.prop > 3 or self.prop < 1:
                raise TypeError("The Property must be a value between 1 and 3")
                self.prop = None
                return
        except ValueError:
            raise ValueError("The Property must be given as an integer")

    #I don't know what to do here yet...
    def login():
        print "User logged in..."
    def logout():
        print "Logging out..."
