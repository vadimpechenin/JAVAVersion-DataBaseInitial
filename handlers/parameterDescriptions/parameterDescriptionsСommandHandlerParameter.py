from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class ParameterDescriptionsСommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, systemName, displayName):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.systemName = systemName
        self.displayName = displayName