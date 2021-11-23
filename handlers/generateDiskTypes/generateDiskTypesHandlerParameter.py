from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateDiskTypesCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, name, numberBladeDisk):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.name = name
        self.numberBladeDisk = numberBladeDisk