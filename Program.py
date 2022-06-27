class Program:

    def __init__(self, title, description, costPerMin, id=None):
        self.id = id
        self.title = title
        self.description = description
        #Making sure its legit...
        try:
            tempCostPerMin = float(costPerMin)
        except ValueError:
            raise ValueError("Given value must be an integer or float")
            return

        if costPerMin > 0:
            try:
                self.costPerMin = float(costPerMin)
            except TypeError:
                raise
        else:
            raise ValueError("No negative or = 0 cost is allowed")

    #Assign the cost of the program
    def SetCost(self, costPerMinNew):
        try:
            self.costPerMin = float(costPerMin)
            if self.costPerMin <= 0:
                raise ValueError("No negative or = 0 cost is allowed.")
        except ValueError:
            raise

    #Get the program's cost
    def getCost(self):
        return self.costPerMin

    #Description getters/setters
    def setDescription(self, newDescription):
        self.description = newDescription
    def getDescription(self):
        return self.description

    def setTitle(self,titleNew):
        self.title = titleNew
    def getTitle(self):
        return self.title

    def getID(self):
        return self.id
