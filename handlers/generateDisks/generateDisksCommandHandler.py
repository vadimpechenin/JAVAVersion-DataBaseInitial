from db.UUIDClass import UUIDClass
from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.disks import Disks
import random

class GenerateDisksCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()

        # Генерация uuid для подстановки
        ID = UUIDClass.geterateUUIDWithout_()
        parameters.uuidObject.disksIDList.append(ID)
        NameOfDisk = 'Диск_№' + str(round(random.random()*100000))

        type_object = Disks(ID = ID, TypeID = parameters.uuidObject.diskTypesIDList[parameters.typeID-1],
                                 ProjectID = parameters.uuidObject.projectsIDList[parameters.projectID-1],
                            Name = NameOfDisk)

        data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers