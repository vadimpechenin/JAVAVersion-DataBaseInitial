from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.slots import Slots
import numpy as np
from random import randint

class GenerateSlotsCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        measThicknessSlot, measAngleAxisSlot, measAngleSlot = self.generateMeasuredParametersInSlots(parameters)

        for j in range(parameters.numberBladeDisk):
            parameters.externalID = j+1
            type_object = Slots(ID = str(parameters.ID), DiskID = str(parameters.diskID),
                                 measThicknessSlot = measThicknessSlot[j], measAngleAxisSlot = measAngleAxisSlot[j],
                                 measAngleSlot = measAngleSlot[j], ExternalID = str(parameters.externalID))
            parameters.ID += 1
            data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers

    def generateMeasuredParametersInSlots(self,parameters):
        measThicknessSlot = np.random.normal(
            parameters.thicknessSlot + (parameters.TthicknessSlot[1] + parameters.TthicknessSlot[0]) / 2,
            (parameters.TthicknessSlot[1] - parameters.TthicknessSlot[0]) / 6,
            parameters.numberBladeDisk)
        measAngleAxisSlot = np.random.normal(parameters.angleAxisSlot + (parameters.TAngleAxisSlot[1] + parameters.TAngleAxisSlot[0]) / 2,
                                          (parameters.TAngleAxisSlot[1] - parameters.TAngleAxisSlot[0]) / 6,
                                          parameters.numberBladeDisk)
        measAngleSlot = np.random.normal(parameters.angleSlot + (parameters.TAngleSlot[1] + parameters.TAngleSlot[0]) / 2,
                                          (parameters.TAngleSlot[1] - parameters.TAngleSlot[0]) / 6,
                                          parameters.numberBladeDisk)
        return measThicknessSlot, measAngleAxisSlot, measAngleSlot