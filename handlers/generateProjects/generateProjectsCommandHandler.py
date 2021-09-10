from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.projects import Projects

class GenerateProjectsCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        type_object = Projects(ID=str(parameters.ID), Description=parameters.description)
        data_base.databaseAddCommit(type_object)
        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)
        return ciphers