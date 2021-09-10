from handlers.baseCommandHandler import BaseCommandHandler
from db.mainSQL import SQLDataBase
from db.blades import Blades
import numpy as np

class GenerateBladesCommandHandler(BaseCommandHandler):
    def __init__(self):
        pass

    def execute(self, parameters):
        # Запрос к базе данных на заполнение данных
        data_base = SQLDataBase(parameters.name_of_database)
        data_base.create_session()
        thiknessMeausred = np.random.normal(parameters.thickess+(parameters.TThickness[1] + parameters.TThickness[0]) / 2,
                                        (parameters.TThickness[1] - parameters.TThickness[0]) / 6,
                                        parameters.numberBladeDisk)
        anglesMeausred = np.random.normal(parameters.angle+(parameters.TAngle[1] + parameters.TAngle[0]) / 2,
                                        (parameters.TAngle[1] - parameters.TAngle[0]) / 6,
                                        parameters.numberBladeDisk)
        for j in range(parameters.numberBladeDisk):
            type_object = Blades(ID=str(parameters.ID), Name=parameters.name, NumberBladesDisk=parameters.numberBladeDisk)
            data_base.databaseAddCommit(type_object)

        ciphers = data_base.select_all_params_in_table(parameters.nameOfTable)

        return ciphers