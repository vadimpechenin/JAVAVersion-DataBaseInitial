from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateMeasureCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, thickess, TThickness, angle, TAngle, thickessT, TThicknessT,
                 numberBladeDisk, projectID, externalID, typeID,uuidObject):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.thickess = thickess
        self.TThickness = TThickness
        self.angle = angle
        self.TAngle = TAngle
        self.thickessT = thickessT
        self.TThicknessT = TThicknessT
        self.numberBladeDisk = numberBladeDisk
        self.projectID = projectID
        self.externalID = externalID
        self.typeID = typeID
        self.uuidObject = uuidObject