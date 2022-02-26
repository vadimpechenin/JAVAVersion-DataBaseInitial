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


    # Параметры диска. ноябрь 2021
    # Толщина паза диска
    thicknessSlot_name = 'thicknessSlot' #Номинальная толщина паза
    TthicknessSlot_name = 'TthicknessSlot' #Допуск на толщину паза
    measThicknessSlot_name = 'measThicknessSlot' #Отклонение толщины паза
    #Угол разворота паза относительно оси
    angleAxisSlot_name = 'angleAxisSlot' #Номинальный угол
    TAngleAxisSlot_name = 'TAngleAxisSlot' #Допуск на угол установки
    measAngleAxisSlot_name = 'measAngleAxisSlot' #Отклонение угла
    #Угол расположения паза в радиальном направлении
    angleSlot_name = 'angleSlot' #Номинальный угол 360/84
    TAngleSlot_name = 'TAngleSlot' #Допуск на толщин
    measAngleSlot_name = 'measAngleSlot' #Отклонение угла

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
    #bladeTypesNumberBladeDiskName = 'bladeTypesNumberBladeDisk'

    # Параметры для сущности Blades
    bladesNameOfTable = 'Blades'
    bladesIDName = 'bladesID'
    bladesExternalIDName = 'bladesExternalIDName'

    # Параметры для сущности ParameterDescriptions
    parameterDescriprionsNameOfTable = 'ParameterDescriprions'
    parameterDescriprionsIDName = 'parameterDescriprionsID'
    parameterDescriprionsSystemNameName = 'parameterDescriprionsSystemName'
    parameterDescriprionsDisplayNameName = 'parameterDescriprionsDisplayName'

    # Параметры для сущности ParameterValues
    parameterValuesNameOfTable = 'ParameterValues'
    parameterValuesIDName = 'parameterValuesID'
    parameterValuesValueName = 'parameterValuesValueName'

    # Параметры для сущности Displacements
    displacementNameOfTable = 'Displacements'
    displacementIDName = 'displacementValuesID'
    displacementDisplacementTypeName = 'displacementDisplacementType'

    # Параметры для сущности DisplacementContents
    displacementContentsNameOfTable = 'DisplacementContents'
    displacementContentsIDName = 'displacementContentsID'
    displacementContentsPositionName = 'displacementContentsPosition'

    #Сущности для диска. Ноябрь 2021
    # Параметры для сущности DiskTypes
    diskTypesNameOfTable = 'DiskTypes'
    diskTypesIDName = 'diskTypesID'
    diskTypesNameName = 'diskTypesName'
    diskTypesNumberBladeDiskName = 'bladeTypesNumberBladeDisk'

    # Параметры для сущности Disks
    diskNameOfTable = 'Disks'
    diskIDName = 'disksID'

    # Параметры для сущности Slots
    slotNameOfTable = 'Slots'
    slotsIDName = 'slotsID'
    slotsExternalIDName = 'slotsExternalID'

    # Параметры для сущности ParameterDiskValues
    parameterDiskValuesNameOfTable = 'ParameterDiskValues'
    parameterDiskValuesIDName = 'parameterDiskValuesID'
    parameterDiskValuesValueName = 'parameterDiskValuesValueName'

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
        # Толщина паза диска
        self.values[self.thicknessSlot_name] = 13.316
        self.values[self.TthicknessSlot_name] = [-0.12, 0.06]
        self.values[self.measThicknessSlot_name] = None
        self.values[self.angleAxisSlot_name] = 24/180*math.pi
        self.values[self.TAngleAxisSlot_name] = [-5/60/180*math.pi, 5/60/180*math.pi]
        self.values[self.measAngleAxisSlot_name] = None
        self.values[self.angleSlot_name] = 360/84/180*math.pi
        self.values[self.TAngleSlot_name] = [-5/60/180*math.pi, 5/60/180*math.pi]
        self.values[self.measAngleSlot_name] = None


        self.values[self.nameOfDatabase] = 'set_of_blades5_uuid.db'
        self.values[self.projectsNameOfTable] = 'Projects'
        self.values[self.projectsIDName] = 1
        self.values[self.projectsDescriptionName] = 'projectsDescription'
        self.values[self.nameOfProjectsNumber] = 2 #2

        # Параметры для сущности BladesTypes
        self.values[self.bladeTypesNameOfTable] = 'BladeTypes'
        self.values[self.bladeTypesIDName] = 1
        self.values[self.bladeTypesNameName] = 'Лопатка 8 ступени'
        #self.values[self.bladeTypesNumberBladeDiskName] = 84

        # Параметры для сущности Blades
        self.values[self.bladesNameOfTable] = 'Blades'
        self.values[self.bladesIDName] = 1
        self.values[self.bladesExternalIDName] = 1

        # Параметры для сущности ParameterDescriprions
        self.values[self.parameterDescriprionsNameOfTable] = 'ParameterDescriptions'
        self.values[self.parameterDescriprionsIDName] = 1
        self.values[self.parameterDescriprionsSystemNameName] = ['T_thickness_lower',
                                                                 'T_thickness_upper',
                                                                 'T_angle_lower',
                                                                 'T_angle_upper',
                                                                 'thickness',
                                                                 'thickness_T',
                                                                 'thickness_B',
                                                                 'thickness_T_nom',
                                                                 'thickness_B_nom','angle','shelf_width_T','shelf_width_half_T',
                                                                 'T_shelf_width_half_T_lower','T_shelf_width_half_T_upper',
                                                                 'shelf_width_B','shelf_width_half_B',
                                                                 'T_shelf_width_half_B_lower','T_shelf_width_half_B_upper',
                                                                 'angle_slice','slice_B','slice_T',
                                                                 'thickness_slot','thickness_slot_upper','thickness_slot_lower',
                                                                 'angle_axis_slot','angle_axis_slot_upper','angle_axis_slot_lower',
                                                                 'angle_slot','angle_slot_upper','angle_slot_lower']
        self.values[self.parameterDescriprionsDisplayNameName] = ['Допуск на толщину нижний','Допуск на толщину верхний',
                                                                  'Допуск на угол нижний', 'Допуск на угол верхний',
                                                                  'Номинальное значение толщины, обеспечивающее натяг',
                                                                  'толщина до точки вращения со стороны корыта',
                                                                  'толщина до точки вращения со стороны спинки',
                                                                  'Номинальное значение толщины, обеспечивающее натяг с корыта',
                                                                  'Номинальное значение толщины, обеспечивающее натяг со спинки',
                                                                  'Угол антивибрационной полки','Толщина полки со стороны корыта',
                                                                  'Половина толщины полки со стороны корыта',
                                                                  'Половина допуска на толщину полки со стороны корыта нижнее',
                                                                  'Половина допуска на толщину полки со стороны корыта верхнее',
                                                                  'Толщина полки со стороны спинки',
                                                                  'Половина толщины полки со стороны спинки',
                                                                  'Половина допуска на толщину полки со стороны спинки нижнее',
                                                                  'Половина допуска на толщину полки со стороны спинки верхнее',
                                                                  'Угол для срезов лопаток',
                                                                  'Расстояния до срезов лопаток со стороны спинки',
                                                                  'Расстояния до срезов лопаток со стороны корыта',
                                                                  'Толщина паза в диске',
                                                                  'Допуск на толщину паза нижнее',
                                                                  'Допуск на толщину паза верхнее',
                                                                  'Угол наклона паза',
                                                                  'Допуск на угол наклона паза нижнее',
                                                                  'Допуск на угол наклона паза верхнее',
                                                                  'Угол паза',
                                                                  'Допуск на угол паза нижнее',
                                                                  'Допуск на угол паза верхнее'
                                                                  ]
        # Параметры для сущности ParameterValues
        self.values[self.parameterValuesNameOfTable] = 'parameterValues'
        self.values[self.parameterValuesIDName] = 1
        self.values[self.parameterValuesValueName] = [-0.1, 0.15, -1 / 6 / 180 * math.pi, 1 / 6 / 180 * math.pi,
                                                        25.13, 11.1, 25.13 - 11.1, 11.1 * 24.73 / 25.13,
                                                        24.73 -11.1 * 24.73 / 25.13, 30 / 180 * math.pi,
                                                        11.75, 6, -0.1, 0.1, 11.5,6.8,-0.1, 0.1,
                                                        50 / 180 * math.pi, 16.05, 12.7
                                                      ]

        # Параметры для сущности Displacements
        self.values[self.displacementNameOfTable] = 'Displacements'
        self.values[self.displacementIDName] = 1
        self.values[self.displacementDisplacementTypeName] = 0

        # Параметры для сущности DisplacementContents
        self.values[self.displacementContentsNameOfTable] = 'DisplacementContents'
        self.values[self.displacementContentsIDName] = 1
        self.values[self.displacementContentsPositionName] = [i + 1 for i in range(self.values[self.number_of_blades_name])]

        # Параметры для сущности DiskTypes
        self.values[self.diskTypesNameOfTable] = 'DiskTypes'
        self.values[self.diskTypesIDName] = 1
        self.values[self.diskTypesNameName] = 'Диск 8 ступени'
        self.values[self.diskTypesNumberBladeDiskName] = 84

        # Параметры для сущности Disks
        self.values[self.diskNameOfTable] = 'Disks'
        self.values[self.diskIDName] = 1

        # Параметры для сущности Slots
        self.values[self.slotNameOfTable] = 'Slots'
        self.values[self.slotsIDName] = 1
        self.values[self.slotsExternalIDName] = 1

        # Параметры для сущности ParameterDiskValues
        self.values[self.parameterDiskValuesNameOfTable] = 'parameterDiskValues'
        self.values[self.parameterDiskValuesIDName] = 1
        self.values[self.parameterDiskValuesValueName] = [13.316, 0.06,-0.12,24 / 180 * math.pi,5 / 60 / 180 * math.pi,
                                                      -5 / 60 / 180 * math.pi,360 / 84 / 180 * math.pi,
                                                      5 / 60 / 180 * math.pi, -5 / 60 / 180 * math.pi]


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