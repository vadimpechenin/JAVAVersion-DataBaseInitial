from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class ParameterDiskValues–°ommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, diskTypeID, parameterDescriptionID, value,uuidObject):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.diskTypeID = diskTypeID
        self.parameterDescriptionID = parameterDescriptionID
        self.value = value
        self.uuidObject = uuidObject