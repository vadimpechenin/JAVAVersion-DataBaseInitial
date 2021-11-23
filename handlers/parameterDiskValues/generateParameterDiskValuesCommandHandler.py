from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.parameterDiskValues import ParameterDiskValues

class ParameterDiskValuesСommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        for j in range(21, len(parameters.value)):

            type_object = ParameterDiskValues(ID=str(parameters.ID), BladeTypeID=str(parameters.diskTypeID),
                                          ParameterDescriptionID = str(parameters.parameterDescriptionID),
                                          Value=parameters.value[j])
            parameters.ID += 1
            parameters.parameterDescriptionID += 1
            data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers