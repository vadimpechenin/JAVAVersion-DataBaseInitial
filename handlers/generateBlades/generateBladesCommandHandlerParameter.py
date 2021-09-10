from handlers.baseCommandHandlerParameter import BaseCommandHandlerParameter

class GenerateMeasureCommandHandlerParameter(BaseCommandHandlerParameter):
    def __init__(self, nameOfDatabase, nameOfTable, ID, thickess, TThickness, angle, TAngle, numberBladeDisk):
        self.nameOfDatabase = nameOfDatabase
        self.nameOfTable = nameOfTable
        self.ID = ID
        self.thickess = thickess
        self.TThickness = TThickness
        self.angle = angle
        self.TAngle = TAngle
        self.numberBladeDisk = numberBladeDisk