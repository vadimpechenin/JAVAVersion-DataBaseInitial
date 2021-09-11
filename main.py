"""
Тестовая программа для создания и наполнения базы данных
"""
from db.mainSQL import SQLDataBase

#Основные параметры для заполнения
from appSettings.applicationSettings import ApplicationSettings
appSettings = ApplicationSettings()

#Обработчики событий
from handlers.mainHandler import MainHandler
handler= MainHandler()

#Параметры для обработчиков событий
from handlers.generateProjects.generateProjectsCommandHandlerParameter import GenerateProjectsCommandHandlerParameter
from handlers.generateBladeTypes.generateBladeTypesHandlerParameter import GenerateBladeTypesCommandHandlerParameter
from handlers.generateBlades.generateBladesCommandHandlerParameter import GenerateMeasureCommandHandlerParameter
from handlers.parameterDescriptions.parameterDescriptionsСommandHandlerParameter import ParameterDescriptionsСommandHandlerParameter
from handlers.parameterValues.parameterValuesСommandHandlerParameter import ParameterValuesСommandHandlerParameter

nameOfDatabase = appSettings.getValue(appSettings.nameOfDatabase)

data_base = SQLDataBase(nameOfDatabase)
data_base.table_create()
#data_base.create_session()

#Последовательное заполнение таблиц проекта
projectsNumber = appSettings.getValue(appSettings.nameOfProjectsNumber)

for number in range(projectsNumber):
    #Заполнение таблицы Projects
    NameOfTable = appSettings.getValue(appSettings.projectsNameOfTable)
    projectsID = appSettings.getValue(appSettings.projectsIDName)
    DescriptionName = appSettings.getValue(appSettings.projectsDescriptionName)

    parameters = GenerateProjectsCommandHandlerParameter(nameOfDatabase, NameOfTable, projectsID, DescriptionName)
    initInTable = handler.initFunction(0, parameters)
    print(initInTable)

    # Заполнение таблицы BladeTypes
    if (number==0):
        NameOfTable = appSettings.getValue(appSettings.bladeTypesNameOfTable)
        bladeTypesID = appSettings.getValue(appSettings.bladeTypesIDName)
        bladeTypesName = appSettings.getValue(appSettings.bladeTypesNameName)
        bladeTypesNumberBladeDisk= appSettings.getValue(appSettings.bladeTypesNumberBladeDiskName)
        parameters = GenerateBladeTypesCommandHandlerParameter(nameOfDatabase, NameOfTable,
                                                             bladeTypesID, bladeTypesName, bladeTypesNumberBladeDisk)
        initInTable = handler.initFunction(1, parameters)
        #appSettings.setValue(appSettings.bladeTypesIDName,
        #                     bladeTypesID + 1)
        print(initInTable)

    # Заполнение таблицы Blades
    NameOfTable = appSettings.getValue(appSettings.bladesNameOfTable)
    bladesID = appSettings.getValue(appSettings.bladesIDName)
    thickess = appSettings.getValue(appSettings.thickness_name)
    TThickness = appSettings.getValue(appSettings.T_thickness_name)
    angle = appSettings.getValue(appSettings.angle_name)
    TAngle = appSettings.getValue(appSettings.T_angle_name)
    externalID = appSettings.getValue(appSettings.bladesExternalIDName)

    parameters = GenerateMeasureCommandHandlerParameter(nameOfDatabase, NameOfTable, bladesID, thickess,
                                                        TThickness, angle, TAngle, bladeTypesNumberBladeDisk,
                                                        projectsID, externalID, bladeTypesID)

    appSettings.setValue(appSettings.bladesIDName, bladesID + bladeTypesNumberBladeDisk)
    initInTable = handler.initFunction(2, parameters)
    print(initInTable)

    # Заполнение таблицы ParameterDescriptions
    if (number == 0):
        NameOfTable = appSettings.getValue(appSettings.parameterDescriprionsNameOfTable)
        parameterDescriprionsID = appSettings.getValue(appSettings.parameterDescriprionsIDName)
        parameterDescriprionsSystemName= appSettings.getValue(appSettings.parameterDescriprionsSystemNameName)
        parameterDescriprionsDisplayName = appSettings.getValue(appSettings.parameterDescriprionsDisplayNameName)

        parameters = ParameterDescriptionsСommandHandlerParameter(nameOfDatabase, NameOfTable, parameterDescriprionsID,
                                                                  parameterDescriprionsSystemName,
                                                                  parameterDescriprionsDisplayName)
        initInTable = handler.initFunction(3, parameters)
        print(initInTable)

        # Заполнение таблицы ParameterValues
        NameOfTable = appSettings.getValue(appSettings.parameterValuesNameOfTable)
        parameterValuesID = appSettings.getValue(appSettings.parameterValuesIDName)
        parameterValuesValue= appSettings.getValue(appSettings.parameterValuesValueName)
        parameters = ParameterValuesСommandHandlerParameter(nameOfDatabase, NameOfTable, parameterValuesID,
                                                                  bladeTypesID, parameterDescriprionsID,
                                                                  parameterValuesValue)
        initInTable = handler.initFunction(4, parameters)
        print(initInTable)
        #Увеличение ID для параметров
        appSettings.setValue(appSettings.parameterDescriprionsIDName,
                             parameterDescriprionsID + len(parameterDescriprionsSystemName))
        appSettings.setValue(appSettings.parameterValuesIDName, parameterValuesID + len(parameterValuesValue))

    appSettings.setValue(appSettings.projectsIDName, projectsID + 1)
#data_base.init_repletion_data_base()
"""
N = 84
T_thickness_lower = -0.1
T_thickness_upper = 0.15
delta_thickness = np.random.normal((T_thickness_upper+T_thickness_lower)/2,(T_thickness_upper-T_thickness_lower)/6,
                 size = N)
T_angle_lower = -1/6/180*np.pi
T_angle_upper = 1/6/180*np.pi
delta_angle = np.random.normal((T_angle_upper + T_angle_lower)/2,
                                                   (T_angle_upper - T_angle_lower)/6, size = N)

data_base.generated_data_save_data_base(delta_thickness,delta_angle)
"""


