from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateDisplacementsCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase,nameOfTable, ID, ProjectID, DisplacementType,uuidObject):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.ProjectID = ProjectID
        self.DisplacementType = DisplacementType
        self.uuidObject = uuidObject