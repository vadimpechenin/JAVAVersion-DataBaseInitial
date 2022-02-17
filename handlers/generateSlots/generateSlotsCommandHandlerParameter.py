from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateSlotsCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, thicknessSlot, TthicknessSlot, angleAxisSlot, TAngleAxisSlot,
                 angleSlot, TAngleSlot,numberBladeDisk, externalID, diskID, position):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.thicknessSlot = thicknessSlot
        self.TthicknessSlot = TthicknessSlot
        self.angleAxisSlot = angleAxisSlot
        self.TAngleAxisSlot = TAngleAxisSlot
        self.angleSlot = angleSlot
        self.TAngleSlot = TAngleSlot
        self.numberBladeDisk = numberBladeDisk
        self.externalID = externalID
        self.diskID = diskID
        self.position = position