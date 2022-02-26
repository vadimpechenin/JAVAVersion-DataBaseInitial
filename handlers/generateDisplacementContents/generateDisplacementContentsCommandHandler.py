from db.UUIDClass import UUIDClass
from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.displacementContents import DisplacementContents

class GenerateDisplacementContentsCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        for j in range(parameters.numberBladeDisk):

            # Генерация uuid для подстановки
            ID = UUIDClass.geterateUUIDWithout_()
            parameters.uuidObject.displacementContentsIDList.append(ID)

            type_object = DisplacementContents(ID = ID, DisplacementID = parameters.uuidObject.displacementsIDList[parameters.displacementID-1],
                                               BladeID =  parameters.uuidObject.bladesIDList[parameters.bladeID-1],
                                               SlotID = parameters.uuidObject.slotsIDList[parameters.slotID-1])
            parameters.bladeID += 1
            parameters.ID += 1
            parameters.slotID += 1
            data_base.databaseAddCommit(type_object)
        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)
        return ciphers