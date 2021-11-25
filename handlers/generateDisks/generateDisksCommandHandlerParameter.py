from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateDisksCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, projectID, typeID):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.projectID = projectID
        self.typeID = typeID