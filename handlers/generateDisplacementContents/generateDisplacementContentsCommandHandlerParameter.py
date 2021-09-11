from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateDisplacementContentsCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, displacementID, bladeID, position):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.displacementID = displacementID
        self.bladeID = bladeID
        self.position = position