import User as u
import Call as C
import Bill as b

#Custom Exception used for indicating a client validation Error:
#If "VAT" is used as an argument, it indicates something is wrong with the VAT number, and displays an according message.
#Same with "Name"
#IO is used when loading data from the file in CreateUsers.
class ClientValidationError(Exception):
    def __init__(self, mode="VAT"):
        if mode == "VAT":
            self.ret = "Invalid VAT Number"
        elif mode == "Name":
            self.ret = "Invalid First Name or Surname"
        elif mode == "IO":
            self.ret = "The input file is corrupted"
    def __str__(self):
        return self.ret

#Main Client Class
class Client(u.User):
    def __init__(self, unameNew, nameNew, snameNew, VATnumNew):
        #Creates a client object
        u.User.__init__(self, unameNew, nameNew, snameNew, 1)
        #Parse the VAT # and check if it is an integer by casting it.
        #if something's wrong, then spit it out...
        try:
            self.VATnum = int(VATnumNew)
        except ValueError:
            raise ValueError("VAT Number must be an integer")

        #The client's calls
        self.calls = []
        #The program he selected
        self.programSelected = None
        #His bill
        self.Bill = None

    #Assign VAT number for the client
    def getVAT(self):
        return self.VATnum
    def setVAT(self, VATNew):
        self.VATnum = VATNew

    #For showing the Bill in detail, if it exists
    def ShowBill(self):
        if self.Bill == None:
            print "Bill hasn't been created yet. Please contact customer service..."
            return
        callCounter = 1
        for call in self.calls:
            print "Call #" + str(callCounter) + " Duration:" + str(call.getDuration())
            callCounter += 1
        print "Final Cost: " + str(self.Bill.getFinalCost())

    #For showing all the calls made by the client
    def ShowHistory(self):
        print "Call history: "
        callCounter = 1
        for call in self.calls:
            print "Call #" + str(callCounter) + " | Made at: " + call.getTimeStamp(True) + " | Duration:" + str(call.getDuration()) + " seconds"

    #Methods for binding the client's program/bill/calls
    def bindProgram(self, programNew):
        self.programSelected = programNew
    def SetBill(self, billNew):
        if isinstance(billNew, b.Bill):
            self.Bill = billNew
        else:
            raise TypeError("Not valid Bill object")
    def AddCall(self, CallGiven):
        self.calls.append(CallGiven)

    #For returning all the calls made by the client
    def getCalls(self):
        return self.calls

    #For returning the client's program.
    def getProgram(self):
        if self.programSelected != None:
            return self.programSelected
        else:
            raise ValueError("No program selected")
