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
        for j in parameters.position:
            type_object = DisplacementContents(ID = str(parameters.ID), DisplacementID = str(parameters.displacementID),
                                               BladeID = str(parameters.bladeID), Position = j)
            parameters.bladeID += 1
            parameters.ID += 1
            data_base.databaseAddCommit(type_object)
        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)
        return ciphers