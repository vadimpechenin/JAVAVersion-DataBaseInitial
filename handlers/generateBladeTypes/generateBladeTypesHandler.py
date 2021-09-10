from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.bladeTypes import BladeTypes

class GenerateBladeTypesCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.nameOfDatabase)
        data_base.create_session()
        type_object = BladeTypes(ID=str(parameters.ID), Name=parameters.name, NumberBladesDisk=parameters.numberBladeDisk)
        data_base.databaseAddCommit(type_object)
        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)
        return ciphers