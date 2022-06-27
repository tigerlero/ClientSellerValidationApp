from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

"""
    DB Declaration file. The DB schema is defined here.
"""

class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    password_hash = Column(String(260), nullable=False)
    fname = Column(String(64), nullable=False)
    sname = Column(String(64), nullable=False)
    accesslvl = Column(Integer, nullable=False)

class Client(Base):
    __tablename__ = "client"
    cid = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("user.uid"), nullable=False)
    vatnum = Column(Integer, nullable=False)
    programbinded = Column(Integer, ForeignKey("program.prog_id"))
    billbinded = Column(Integer, ForeignKey("bill.bill_id"))

class Seller(Base):
    __tablename__ = "seller"
    sid = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("user.uid"), nullable=False)


class Admin(Base):
    __tablename__ = "admin"
    aid = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("user.uid"), nullable=False)

class Bill(Base):
    __tablename__ = "bill"
    bill_id = Column(Integer, primary_key=True)
    description = Column(Text)
    programbinded = Column(Integer, ForeignKey("program.prog_id"))
    paid = Column(Integer, nullable=False, default=0) #0= Not paid, 1 = Paid

class Program(Base):
    __tablename__ = "program"
    prog_id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    description = Column(Text)
    costpermin = Column(Float, nullable=False)

class Call(Base):
    __tablename__ = "call"
    call_id = Column(Integer, primary_key=True)
    caller_id = Column(Integer, ForeignKey("client.cid"), nullable=False)
    reciever = Column(Integer, ForeignKey("client.cid"))
    timestamp = Column(Date, nullable=False)
    duration = Column(Integer, nullable=False)

class PhoneNumber(Base):
    __tablename__ = "phone_number"
    phone_no = Column(String(10), primary_key=True)
    owner = Column(Integer, ForeignKey("client.cid"), nullable=False)


engine = create_engine("sqlite:///app.db")

# Base.metadata.create_all(engine)
# print "Database init successful"
