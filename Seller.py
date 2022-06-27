import User as u
import Client as c
import Bill as b
import Program as p

class Seller(u.User):
    def __init__(self, unameNew, nameNew, snameNew):
        u.User.__init__(self, unameNew, nameNew, snameNew, 2)

    #Method for creating a new client.
    #If a true argument is passed in the end, the attributes for the new client are printed out.
    def CreateClient(self, unameNew, nameNew, snameNew, VATnumNew, printOut=False):
        newClient = c.Client(unameNew, nameNew, snameNew, VATnumNew)
        if printOut:
            print "New client created:"
            print "Username: " + newClient.getUname()
            print "First Name: " + newClient.getName()
            print "Surname: " + newClient.getSname()
            print "VAT Number: " + str(newClient.getVAT())
        return newClient

    #Method for creating the client's bill
    def CreateBill(self, givenClient):
        clientCalls = givenClient.getCalls()
        try:
            clientProgram = givenClient.getProgram()
        except ValueError as e:
            print e
            return
        newBill = b.Bill()
        newBill.bindProgram(clientProgram)
        newBill.BindCallSet(clientCalls)
        givenClient.SetBill(newBill)
