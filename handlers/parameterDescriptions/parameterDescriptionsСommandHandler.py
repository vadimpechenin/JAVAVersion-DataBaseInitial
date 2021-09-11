from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.parameterDescriptions import ParameterDescriptions

class ParameterDescriptionsСommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        for j in range(len(parameters.systemName)):

            type_object = ParameterDescriptions(ID=str(parameters.ID), SystemName=parameters.systemName[j],
                             DisplayName=parameters.displayName[j])
            parameters.ID += 1
            data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers