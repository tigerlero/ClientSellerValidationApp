import Client as c
import Seller as s
import Program as p
import User as u

class Admin(u.User):
    def __init__(self, unameNew, nameNew, snameNew):
        u.User.__init__(self, unameNew, nameNew, snameNew, 3)

    def CreateSeller(self, unameNew, nameNew, snameNew):
        return s.Seller(unameNew, nameNew, snameNew)

    def DeleteSeller(self, seller):
        if isinstance(seller, s.Seller):
            seller = None

    def DeleteClient(self, client):
        if isinstance(client, c.Client):
            client = None

    def CreateProgram(self, description, costPerMin):
        return p.Program(description, costPerMin)

    def CreateClient(self, unameNew, nameNew, snameNew, VATnumNew, printOut=False):
        newClient = c.Client(unameNew, nameNew, snameNew, VATnumNew)
        if printOut:
            print "New client created:"
            print "Username: " + newClient.getUname()
            print "First Name: " + newClient.getName()
            print "Surname: " + newClient.getSname()
            print "VAT Number: " + str(newClient.getVAT())
        return newClient
