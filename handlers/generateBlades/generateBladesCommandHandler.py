from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.blades import Blades
import numpy as np
from random import randint

class GenerateBladesCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        thiknessMeausred, anglesMeausred = self.generateThiknessAngles(parameters)
        for j in range(parameters.numberBladeDisk):
            parameters.externalID = randint(1, 1000)
            type_object = Blades(ID = str(parameters.ID), TypeID = str(parameters.typeID),
                                 MeasThickness = thiknessMeausred[j], MeasAngle = anglesMeausred[j],
                                 ExternalID = str(parameters.externalID), ProjectID = str(parameters.projectID))
            parameters.ID += 1
            data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers

    def generateThiknessAngles(self,parameters):
        thiknessMeausred = np.random.normal(
            parameters.thickess + (parameters.TThickness[1] + parameters.TThickness[0]) / 2,
            (parameters.TThickness[1] - parameters.TThickness[0]) / 6,
            parameters.numberBladeDisk)
        anglesMeausred = np.random.normal(parameters.angle + (parameters.TAngle[1] + parameters.TAngle[0]) / 2,
                                          (parameters.TAngle[1] - parameters.TAngle[0]) / 6,
                                          parameters.numberBladeDisk)
        return thiknessMeausred, anglesMeausred