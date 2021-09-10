"""
В классе храниться названия всех переменных
"""
import math

class ApplicationSettings():
    number_of_blades_name = 'number_of_blades' # Количество лопаток
    T_thickness_name = 'T_thickness' # Допуск на толщину
    T_angle_name = 'T_angle'  # Допуск на угол
    delta_thickness_name = 'delta_thickness' # Отклонения толщины
    delta_angle_name = 'delta_angle'   # Отклонения углов
    thickness_name = 'thickness'    # Номинальное значение толщины, обеспечивающее натяг
    thickness_T_name = 'thickness_T' # толщина до точки вращения со стороны корыта
    thickness_B_name = 'thickness_B' # толщина до точки вращения со стороны спинки
    thickness_T_nom_name = 'thickness_T_nom'    # Номинальное значение толщины, обеспечивающее натяг
    thickness_B_nom_name = 'thickness_B_nom' # толщина до точки вращения со стороны корыта
    angle_name = 'angle' # Угол антивибрационной полки
    # Толщина полки со стороны корыта
    shelf_width_T_name = 'shelf_width_T'
    shelf_width_half_T_name = 'shelf_width_half_T'
    T_shelf_width_half_T_name = 'T_shelf_width_half_T'
    # Толщина полки со стороны спинки
    shelf_width_B_name = 'shelf_width_B'
    shelf_width_half_B_name = 'shelf_width_half_B'
    T_shelf_width_half_B_name = 'T_shelf_width_half_B'
    # Угол и расстояния для срезов лопаток
    angle_slice_name = 'angle_slice'
    slice_B_name = 'slice_B'
    slice_T_name = 'slice_T'
    # Название файда базы данных
    filedb_name = 'filedb'
    # Производные параметры
    pointsBackThroughParams_name = 'pointsBackThroughParams'
    # Порядок лопаток
    arrayNumberOfBlades_name = 'arrayNumberOfBlades'

    # Сборочные параметры
    assemblyChord_name = 'assemblyChord'
    assemblyGaps_name = 'assemblyGaps'
    assemblyGaps_init_name = 'assemblyGapsInit'

    #Общие для всех настройки
    nameOfDatabase = 'Database'
    nameOfProjectsNumber = 'ProjectsNumber'

    #Параметры для сущности Projects
    projectsNameOfTable = 'Projects'
    projectsIDName = 'projectsID'
    projectsDescriptionName = 'projectsDescription'

    # Параметры для сущности BladeTypes
    bladeTypesNameOfTable = 'BladeTypes'
    bladeTypesIDName = 'bladeTypesID'
    bladeTypesNameName = 'bladeTypesName'
    bladeTypesNumberBladeDiskName = 'bladeTypesNumberBladeDisk'

    values = {}

    def __init__(self):
        self.initEmptySettings()

    def initEmptySettings(self):
        #Создание всех имен переменных
        self.values[self.number_of_blades_name] = 84
        self.values[self.T_thickness_name] = [-0.1, 0.15]
        self.values[self.T_angle_name] = [-1/6/180*math.pi, 1/6/180*math.pi]
        self.values[self.delta_thickness_name] = None
        self.values[self.delta_angle_name] = None
        self.values[self.thickness_name] = 25.13
        self.values[self.thickness_T_name] = 11.1
        self.values[self.thickness_B_name] = 25.13-self.values[self.thickness_T_name]
        self.values[self.thickness_T_nom_name] = 11.1*24.73/25.13
        self.values[self.thickness_B_nom_name] = 24.73 - self.values[self.thickness_T_nom_name]
        self.values[self.angle_name] = 30/180*math.pi
        self.values[self.shelf_width_T_name] = 11.75
        self.values[self.shelf_width_half_T_name] = 6
        self.values[self.T_shelf_width_half_T_name] = [-0.1, 0.1]
        self.values[self.shelf_width_B_name] = 11.5
        self.values[self.shelf_width_half_B_name] = 6.8
        self.values[self.T_shelf_width_half_B_name] = [-0.1, 0.1]
        self.values[self.angle_slice_name] = 50/180*math.pi
        self.values[self.slice_B_name] = 16.05
        self.values[self.slice_T_name] = 12.7
        self.values[self.filedb_name] = ''
        self.values[self.pointsBackThroughParams_name] = None
        self.values[self.arrayNumberOfBlades_name] = None
        self.values[self.assemblyChord_name] = None
        self.values[self.assemblyGaps_name] = None
        self.values[self.assemblyGaps_init_name] = None

        self.values[self.nameOfDatabase] = 'set_of_blades1.db'
        self.values[self.projectsNameOfTable] = 'Projects'
        self.values[self.projectsIDName] = 1
        self.values[self.projectsDescriptionName] = 'projectsDescription'
        self.values[self.nameOfProjectsNumber] = 2

        self.values[self.bladeTypesNameOfTable] = 'BladeTypes'
        self.values[self.bladeTypesIDName] = 1
        self.values[self.bladeTypesNameName] = 'Лопатка 8 ступени'
        self.values[self.bladeTypesNumberBladeDiskName] = 84

    def getNames(self):
        #Возвращает все названия параметров, необходимых для приложения
        keys=[]
        for key, value in self.values.items():
            keys.append(key)
        return keys

    def getValue(self,name):
        #Метод для получения значения параметра
        value = self.values[name]
        return value

    def setValue(self,name,value):
        #Метод для изменения значения параметра
        for key, v in self.values.items():
            if name==key:
                self.values[name] = value