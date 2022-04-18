from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        #self.client = MongoClient('mongodb://localhost:54482') #load without auth
        
        self.client = MongoClient('mongodb://{}:{}@localhost:54482/AAC'.format(username,password)) #load with auth
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary    
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, data):
        cursor = self.database.animals.find(data,{'_id':False}) #return the pointer of a list of results
        return cursor
# Creating method to implement the U in CRUD
    def update(self, find, data):
        if data is not None or find is not None:
            cur = self.database.animals.update_many(find,data)
            return cur #return what was updated
        else:
            raise Exception("Parameters are not formatted correctly")
        
# Creating method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result
        else:
            raise Exception("No data provided")
            
    #This will be used to help my pie chart
    # This just gets all distinct values in a specific catagory
    def getDistinct(self,data):
        return self.database.animals.find().distinct(data)
        