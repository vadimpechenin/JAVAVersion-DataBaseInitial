from db.UUIDClass import UUIDClass
from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.parameterDiskValues import ParameterDiskValues

class ParameterDiskValuesСommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        for j in range(len(parameters.value)):

            # Генерация uuid для подстановки
            ID = UUIDClass.geterateUUIDWithout_()
            parameters.uuidObject.parameterDiskValuesIDList.append(ID)

            type_object = ParameterDiskValues(ID=ID, DiskTypeID= parameters.uuidObject.diskTypesIDList[parameters.diskTypeID-1],
                                          ParameterDescriptionID = parameters.uuidObject.parameterDescriptionsIDList[parameters.parameterDescriptionID-1],
                                          Value=parameters.value[j])
            parameters.ID += 1
            parameters.parameterDescriptionID += 1
            data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers