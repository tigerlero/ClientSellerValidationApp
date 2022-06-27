import User as u
import sys
import Client as c
args = sys.argv

#If less than the required arguments are supplied...
if len(args) < 5:
    print "Please input all the required data as arguments"
    print "Usage: python CreateUsers.py <username> <First Name> <Surname> <Property>"
    print "Properties: 1 -> Client, \n 2 -> Seller \n 3 -> Admin"
    exit(1)

######################
# Erwthma 1.1
######################

#Parse the arguments...
username = args[1]
Fname = args[2]
Sname = args[3]
prop = args[4]

try:
    #Create the new user
    user1 = u.User(username, Fname, Sname, prop)
    print "User created successfully:"
    print "Username: " + user1.getUname()
    print "First Name: " + user1.getName()
    print "Surname: " + user1.getSname()
    #Display his property...
    if user1.getProp() == 1:
        print "Property: Client"
    elif user1.getProp() == 2:
        print "Property: Seller"
    elif user1.getProp() == 3:
        print "Property: Admin"
except Exception as e:
    print e
    exit(1)
print "That was user #" + u.getCounter(True)

print "-------------------------------------"

######################
# Erwthma 2.1
######################
print "Creating user by keyboard input:"
#Get the user's input...
username = raw_input("Username: ")
Fname = raw_input("First Name: ")
Sname = raw_input("Surname: ")
prop = raw_input("Property (Values between 1 and 3 are accepted): ")

try:
    user2 = u.User(username, Fname, Sname, prop)
    print "User created successfully:"
    print "Username: " + user2.getUname()
    print "First Name: " + user2.getName()
    print "Surname: " + user2.getSname()
    if user2.getProp() == 1:
        print "Property: Client"
    elif user2.getProp() == 2:
        print "Property: Seller"
    elif user2.getProp() == 3:
        print "Property: Admin"
except Exception as e:
    print e
    exit(1)
print "That was user #" + u.getCounter(True)

print "-------------------------------------"

####################
# Erwthma 3.1
###################
print "Creating client. Please fill in all the required data:"
username = raw_input("Username: ")
Fname = raw_input("First Name: ")
Sname = raw_input("Surname: ")
VATNumNew = raw_input("VAT #: ")

try:
    user3 = c.Client(username, Fname, Sname, VATNumNew)
    print "Client created successfully:"
    print "Username: " + user3.getUname()
    print "First Name: " + user3.getName()
    print "Surname: " + user3.getSname()
    print "VAT #: " + str(user3.getVAT())
except Exception as e:
    print e
    exit(1)
print "That was user #" + u.getCounter(True)
print "-------------------------------------"

####################
# Erwthma 3.2
###################
from Client import ClientValidationError

print "Creating client with custom exception handling. Please fill in all the required data:"
username = raw_input("Username: ")
Fname = raw_input("First Name: ")
Sname = raw_input("Surname: ")
VATNumNew = raw_input("VAT #: ")
try:
    try:
        user4 = c.Client(username, Fname, Sname, VATNumNew)
        print "Client created successfully:"
        print "Username: " + user4.getUname()
        print "First Name: " + user4.getName()
        print "Surname: " + user4.getSname()
        print "VAT #: " + str(user4.getVAT())
    #First try to get the error type...
    #If it catches a TypeError, then it has to do with the names provided.
    #If a ValueError is caught, then it has to do with the VAT number.
    #For more info, refer to ClientValidationError -> Client.py
    except TypeError:
        raise ClientValidationError("Name")
        exit(1)
    except ValueError:
        raise ClientValidationError("VAT")
        exit(1)
except ClientValidationError as e: #Then print it out
    print e
    exit(1)
print "That was user #" + u.getCounter(True)
print "-------------------------------------"

#########################
# Erwthma 4.1
#########################
print "Creating a single client from file IO..."
try:
    fin = open("clientInput.txt","r")
    lines = fin.readlines()
    if len(lines) == 0:
        raise IOError("The Input File is empty")
    fin.close()
except IOError as e:
    print e
    exit(1)

loop = 1
for line in lines:
    #Used to make sure that only one client gets parsed
    if loop > 1:
        break
    else:
        loop += 1
    line = line.split(",")
    try:
        try:
            #The format used in the file is:
            #<username>,<Name>,<Surname>,<VAT #>
            client1 = c.Client(line[0], line[1], line[2], line[3])
            print "Client created successfully:"
            print "Username: " + client1.getUname()
            print "First Name: " + client1.getName()
            print "Surname: " + client1.getSname()
            print "VAT #: " + str(client1.getVAT())

        except TypeError:
            raise ClientValidationError("Name")
        except ValueError:
            raise ClientValidationError("VAT")
        except IndexError:
            raise ClientValidationError("IO")
    except ClientValidationError as e:
        print e
        exit(1)
print "----------------------------------------"
#######################
# Erwthma 4.2
#######################
print "Creating clients from file IO (Part 2):"
clientList = [] #List of clients
for line in lines:
    line = line.split(",")
    try:
        try:
            client1 = c.Client(line[0], line[1], line[2], line[3])
            print "Client created successfully:"
            print "Username: " + client1.getUname()
            print "First Name: " + client1.getName()
            print "Surname: " + client1.getSname()
            print "VAT #: " + str(client1.getVAT())
            clientList.append(client1)
        except TypeError as e: #Error with name validation
            raise ClientValidationError("Name")
            exit(1)
        except ValueError: #Error with VAT validation
            raise ClientValidationError("VAT")
            exit(1)
        except IndexError: #Corrupted File
            raise ClientValidationError("IO")
    except ClientValidationError as e:
        print e
        exit(1)

print "Outputting all clients to different files"
counterNew = 1 #Counter used for numbering files
for client in clientList:
    try:
        fin = open("client" + str(counterNew) + ".txt", "w")
        fin.write(client.getUname() + "\t #Username \n")
        fin.write(client.getName() + "\t #FirstName \n")
        fin.write(client.getSname() + "\t #Surname \n")
        fin.write(str(client.getVAT()) + "\t #VAT Number \n")
        fin.close()
        counterNew += 1
    except IOError as e:
        print e
        exit(1)
