import Call as c
import Program as p

class Bill:
    #Initialization...
    def __init__(self):
        self.calls = []
        self.programBinded = None
        self.description = None

    #Getters and setters for the description of the bill
    def setDescription(self, DescNew):
        self.description = DescNew
    def getDescription(self):
        if self.description != None:
            return self.description
        else:
            raise ValueError("No description passed")

    #Add the call made to the list
    def AddCall(self, CallNew):
        if isinstance(CallNew, c.Call):
            self.calls.append(CallNew)
        else:
            raise TypeError("Not an instance of a call...")

    #Get all calls made...
    def getCalls(self):
        if len(self.calls) > 0:
            return self.calls
        else:
            return 0

    #Method used by sellers to transfer call sets
    def BindCallSet(self, callSet):
        self.calls = callSet

    #Return the client's program
    def bindProgram(self, programNew):
        if isinstance(programNew, p.Program):
            self.programBinded = programNew
        else:
            raise TypeError("Not valid program object...")

    #Calculate the final bill
    def getFinalCost(self):
        finalCost = 0
        for call in self.calls:
            #Find out the duration each call lasted in seconds
            callinMin = call.getDuration() / 60
            #Calculate the cost of each call
            callCost = callinMin * self.programBinded.getCost()
            #Add the cost of each call to the bill
            finalCost += callCost
        #Return the bill that the caller has to pay
        return finalCost
