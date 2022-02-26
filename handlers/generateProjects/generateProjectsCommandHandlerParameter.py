from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateProjectsCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase,nameOfTable, ID, description,uuidObject):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.description = description
        self.uuidObject = uuidObject