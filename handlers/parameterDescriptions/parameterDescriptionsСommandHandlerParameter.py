from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class ParameterDescriptions–°ommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, systemName, displayName,uuidObject):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.systemName = systemName
        self.displayName = displayName
        self.uuidObject = uuidObject