import datetime

class Call:
    #Each call object has two attributes:
    #1. The duration of the call (in seconds)
    #2. The timestamp of the call (when was it made)
    def __init__(self):
        self.duration = None
        self.timestamp = None

    #Setter for the call duration
    def setDuration(self, secondsNew):
        try:
            self.duration = int(secondsNew)
        except ValueError:
            raise ValueError("Given duration must be an integer")
        if self.duration <= 0:
            self.duration = None
            raise ValueError("No negative or = 0 call duration is allowed.")

    #Getter for the call duration
    def getDuration(self):
        if self.duration != None:
            return self.duration
        else:
            raise ValueError("Duration not set")

    #Setter for the timestamp
    def setTimestamp(self, DateTimeStampNew):
        if isinstance(DateTimeStampNew, datetime.datetime):
            self.timestamp = DateTimeStampNew
        else:
            raise TypeError("Only datetime objects are supported")

    #Returns the time of the call.
    #If True is passed as an argument, returns it in a string format.
    def getTimeStamp(self, retString=False):
        if self.timestamp != None:
            if retString:
                return str(self.timestamp)
            else:
                return self.timestamp
        else:
            raise ValueError("Timestamp not set...")
