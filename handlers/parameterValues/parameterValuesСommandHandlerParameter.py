from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class ParameterValuesСommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, bladeTypeID, parameterDescriptionID, value):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.bladeTypeID = bladeTypeID
        self.parameterDescriptionID = parameterDescriptionID
        self.value = value