from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateBladeTypesCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, name, TypeDiskID,uuidObject):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.name = name
        self.TypeDiskID = TypeDiskID
        self.uuidObject = uuidObject