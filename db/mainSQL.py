"""
Класс для работы с базой данных
"""
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from db.supportFunctions import resultproxy_to_dict

from .base import Base


#Новые объекты для новой реализации программы
from .projects import Projects
from .blades import Blades
from .bladeTypes import BladeTypes


class SQLDataBase():

    def __init__(self,name_of_database):
        #name_of_database = 'set_of_blades'
        self.engine = create_engine('sqlite:///' + name_of_database, echo = True)#+ '.db'

    def table_create(self):
        #Метод для создания таблиц и базы данных
       Base.metadata.create_all(self.engine)

    def create_session(self):
        #Создание сессии, через которую мапяться объекты
        self.session = sessionmaker(bind=self.engine)()

    def databaseAddCommit(self,type_object):
        self.session.add(type_object)
        self.session.commit()

    def init_repletion_data_base(self):
        # Создание объектов в таблице Projects
        type_object = Projects(ID='1', Description='Колесо 8 ступени')
        self.session.add(type_object)
        self.session.commit()

        type_object = BladeTypes(ID='1', Name="Лопатка 8 ступени", NumberBladesDisk=84)
        self.session.add(type_object)
        self.session.commit()

        type_object = Blades(ID='1', TypeID='1', MeasThickness=10.5, MeasAngle=0.2, ExternalID="5", ProjectID="1")
        self.session.add(type_object)
        self.session.commit()

    def select_all_params_in_table(self,name):
        # Функция для подачи запроса
        request_str = "SELECT * \
                           FROM \
                           " + str(name)
        s = self.session.execute(request_str)
        result_of_query = resultproxy_to_dict(s)
        return result_of_query

    def select_one_params_in_table(self, name, name_column):
        # Функция для подачи запроса
        request_str = "SELECT " + str(name_column) + " \
                              FROM \
                              " + str(name) +" \
                                WHERE type_id = 1"
        s = self.session.execute(request_str)
        result_of_query = resultproxy_to_dict(s)
        return result_of_query

    def request_delete_of_measured(self,name):
        #Запрос на удаление всего из таблицы measure
        request_str = "DELETE FROM " + str(name) +" \
                           WHERE type_id = 1"
        self.session.execute(request_str)

    def request_count_of_blades(self, name):
        # Запрос на подсчет количества лопаток в базе данных
        request_str = "SELECT count(part_id) AS Количество \
                        FROM " + str(name)
        s = self.session.execute(request_str)
        result_of_query = resultproxy_to_dict(s)
        return result_of_query

    def request_update_of_numbers(self, name, numbers):
        #Запрос на обновление данных в таблице

        k = 1
        for i in numbers:
            request_str = "UPDATE " + str(name) + " \
                            SET serial_number = " + str(i) + "\
                            WHERE part_id = " + str(k)
            k += 1
            self.session.execute(request_str)
            self.session.commit()