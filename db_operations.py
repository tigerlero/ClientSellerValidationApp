from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import User as u
import Client as client_or
import Call as call_or
import Program as p
import Bill as b
import Seller as s

from passlib.hash import sha256_crypt

from db_structure import Base, User, Client, Admin, Call, Seller, Bill, Program, PhoneNumber

"""
    All DB operations are defined here. Includes all the create methods, some read methods, and one delete method.
    No update methods have been added yet. (To be added with the final commit)
"""

engine = create_engine("sqlite:///app.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

################
#   Create     #
################

######## USER CREATION ###############

def insertUser(uNew, passWish):
    passedUname = uNew.getUname()
    if (session.query(User).filter_by(username=passedUname).count()) > 0:
        return False
    hashedpw = sha256_crypt.encrypt(passWish)
    userToBeIns = User(username=uNew.getUname(), password_hash=hashedpw, fname=uNew.getName(), sname=uNew.getSname(), accesslvl=uNew.getProp())
    session.add(userToBeIns)
    session.commit()
    return True

def insertClient(uNew, passWish):
    if insertUser(uNew, passWish):
        retUser = session.query(User).filter_by(username=uNew.getUname()).one()
        cNew = Client(uid=retUser.uid, vatnum=uNew.getVAT())
        session.add(cNew)
        session.commit()
        return True
    else:
        return False

def insertSeller(uNew, passWish):
    if insertUser(uNew, passWish):
        retUser = session.query(User).filter_by(username=uNew.getUname()).one()
        sNew = Seller(uid=retUser.uid)
        session.add(sNew)
        session.commit()
        return True
    else:
        return False

def insertAdmin(uNew, passWish):
    if insertUser(uNew, passWish):
        retUser = session.query(User).filter_by(username=uNew.getUname()).one()
        aNew = Admin(uid=retUser.uid)
        session.add(aNew)
        session.commit()
        return True
    else:
        return False

#########################################

######## Calls, Programs, Bills, Phone numbers #####################

def insertCall(callGiven, cid, rid=None):
    try:
        if rid == None:
            callNew = Call(caller_id=cid, timestamp=callGiven.getTimeStamp(), duration=callGiven.getDuration())
        else:
            callNew = Call(caller_id=cid,reciever=rid, timestamp=callGiven.getTimeStamp(), duration=callGiven.getDuration())
    except Exception:
        return False
    session.add(callNew)
    session.commit()
    return True

def insertProgram(program):
    if session.query(Program).filter_by(title=program.getTitle()).count() > 0:
        return False
    try:
        progNew = Program(title=program.getTitle(), description=program.getDescription(), costpermin=program.getCost())
        session.add(progNew)
        session.commit()
    except Exception:
        return False
    return True

def insertBill(bill):
    try:
        billNew = Bill(description=bill.getDescription(), programbinded=pid)
        session.add(progNew)
        session.commit()
    except ValueError:
        billNew = Bill(programbinded=pid)
        session.add(progNew)
        session.commit()
    finally:
        return True

def generatePhoneNumber(ownerid):
    if (session.query(PhoneNumber).filter_by(owner=ownerid).count()) > 0:
        return False
    else:
        import random
        phoneNumbernew = PhoneNumber(phone_no=random.randrange(1000000000, 9999999999), owner=ownerid)
        session.add(phoneNumbernew)
        session.commit()

##########################################
################
#   Login      #
################

def TryLogin(username, passGiven):
    userRet = session.query(User).filter_by(username=username)
    if (userRet.count()) > 0:
        userRet = userRet.one()
        if sha256_crypt.verify(passGiven, userRet.password_hash):
            return True
        else:
            return False
    else:
        return False

#########################################
################
#   Getters    #
################

def getPrograms():
    programsRet = session.query(Program)
    retPrograms = []
    for pro in programsRet:
        progImport = p.Program(pro.title, pro.description, pro.costpermin, pro.prog_id)
        retPrograms.append(progImport)
    return retPrograms

def getUidFromUsername(username):
    userRet = session.query(User).filter_by(username=username)
    retUsr = userRet.one()
    return retUsr.uid

def getUserProp(uid):
    userRet = session.query(User).filter_by(uid=uid)
    retUsr = userRet.one()
    return retUsr.accesslvl

def deleteProgram(pid):
    if session.query(Program).filter_by(prog_id=pid).count() > 0:
        programsRet = session.query(Program).filter_by(prog_id=pid).delete()
        session.commit()
