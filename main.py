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
from handlers.generateDisplacements.generateDisplacementsCommandHandlerParameter import GenerateDisplacementsCommandHandlerParameter
from handlers.generateDisplacementContents.generateDisplacementContentsCommandHandlerParameter import GenerateDisplacementContentsCommandHandlerParameter

from handlers.generateDiskTypes.generateDiskTypesHandlerParameter import GenerateDiskTypesCommandHandlerParameter
from handlers.parameterDiskValues.generateParameterDiskValuesCommandHandlerParameter import ParameterDiskValuesСommandHandlerParameter
from handlers.generateDisks.generateDisksCommandHandlerParameter import GenerateDisksCommandHandlerParameter
from handlers.generateSlots.generateSlotsCommandHandlerParameter import GenerateSlotsCommandHandlerParameter


nameOfDatabase = appSettings.getValue(appSettings.nameOfDatabase)

data_base = SQLDataBase(nameOfDatabase)
data_base.table_create()
#data_base.create_session()

#Последовательное заполнение таблиц проекта
projectsNumber = appSettings.getValue(appSettings.nameOfProjectsNumber)

for number in range(projectsNumber):
    #1. Заполнение таблицы Projects
    NameOfTable = appSettings.getValue(appSettings.projectsNameOfTable)
    projectsID = appSettings.getValue(appSettings.projectsIDName)
    DescriptionName = appSettings.getValue(appSettings.projectsDescriptionName)

    parameters = GenerateProjectsCommandHandlerParameter(nameOfDatabase, NameOfTable, projectsID, DescriptionName)
    initInTable = handler.initFunction(0, parameters)
    print(initInTable)
    #2. Заполнение таблицы DiskTypes
    if (number == 0):
        NameOfTable = appSettings.getValue(appSettings.diskTypesNameOfTable)
        diskTypesID = appSettings.getValue(appSettings.diskTypesIDName)
        diskTypesName = appSettings.getValue(appSettings.diskTypesNameName)
        diskTypesNumberBladeDisk = appSettings.getValue(appSettings.diskTypesNumberBladeDiskName)
        parameters = GenerateDiskTypesCommandHandlerParameter(nameOfDatabase, NameOfTable,
                                                               diskTypesID, diskTypesName, diskTypesNumberBladeDisk)
        initInTable = handler.initFunction(7, parameters)

        print(initInTable)

    #3. Заполнение таблицы BladeTypes

        NameOfTable = appSettings.getValue(appSettings.bladeTypesNameOfTable)
        bladeTypesID = appSettings.getValue(appSettings.bladeTypesIDName)
        bladeTypesName = appSettings.getValue(appSettings.bladeTypesNameName)
        #bladeTypesNumberBladeDisk= appSettings.getValue(appSettings.bladeTypesNumberBladeDiskName)
        parameters = GenerateBladeTypesCommandHandlerParameter(nameOfDatabase, NameOfTable,
                                                             bladeTypesID, bladeTypesName, diskTypesID)
        initInTable = handler.initFunction(1, parameters)
        #appSettings.setValue(appSettings.bladeTypesIDName,
        #                     bladeTypesID + 1)
        print(initInTable)

    #4. Заполнение таблицы Blades.
    NameOfTable = appSettings.getValue(appSettings.bladesNameOfTable)
    bladesID = appSettings.getValue(appSettings.bladesIDName)
    thickess = appSettings.getValue(appSettings.thickness_name)
    TThickness = appSettings.getValue(appSettings.T_thickness_name)
    angle = appSettings.getValue(appSettings.angle_name)
    TAngle = appSettings.getValue(appSettings.T_angle_name)
    externalID = appSettings.getValue(appSettings.bladesExternalIDName)

    parameters = GenerateMeasureCommandHandlerParameter(nameOfDatabase, NameOfTable, bladesID, thickess,
                                                        TThickness, angle, TAngle, diskTypesNumberBladeDisk,
                                                        projectsID, externalID, bladeTypesID)

    initInTable = handler.initFunction(2, parameters)
    print(initInTable)

    if (number == 0):
        #5. Заполнение таблицы ParameterDescriptions
        NameOfTable = appSettings.getValue(appSettings.parameterDescriprionsNameOfTable)
        parameterDescriprionsID = appSettings.getValue(appSettings.parameterDescriprionsIDName)
        parameterDescriprionsSystemName= appSettings.getValue(appSettings.parameterDescriprionsSystemNameName)
        parameterDescriprionsDisplayName = appSettings.getValue(appSettings.parameterDescriprionsDisplayNameName)

        parameters = ParameterDescriptionsСommandHandlerParameter(nameOfDatabase, NameOfTable, parameterDescriprionsID,
                                                                  parameterDescriprionsSystemName,
                                                                  parameterDescriprionsDisplayName)
        initInTable = handler.initFunction(3, parameters)
        print(initInTable)

        #6. Заполнение таблицы ParameterValues
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
                             parameterDescriprionsID + len(parameterValuesValue))
        appSettings.setValue(appSettings.parameterValuesIDName, parameterValuesID + len(parameterValuesValue))

        #7. Заполнение таблицы ParameterDiskValues
        parameterDescriprionsID = appSettings.getValue(appSettings.parameterDescriprionsIDName)
        NameOfTable = appSettings.getValue(appSettings.parameterDiskValuesNameOfTable)
        parameterValuesID = appSettings.getValue(appSettings.parameterDiskValuesIDName)
        parameterValuesValue = appSettings.getValue(appSettings.parameterDiskValuesValueName)
        parameters = ParameterDiskValuesСommandHandlerParameter(nameOfDatabase, NameOfTable, parameterValuesID,
                                                            diskTypesID, parameterDescriprionsID,
                                                            parameterValuesValue)
        initInTable = handler.initFunction(8, parameters)
        print(initInTable)
        # Увеличение ID для параметров
        appSettings.setValue(appSettings.parameterDescriprionsIDName,
                             parameterDescriprionsID + len(parameterValuesValue))
        appSettings.setValue(appSettings.parameterDiskValuesIDName, parameterValuesID + len(parameterValuesValue))

    #8. Заполнение таблицы Disks
    NameOfTable = appSettings.getValue(appSettings.diskNameOfTable)
    diskID = appSettings.getValue(appSettings.diskIDName)

    parameters = GenerateDisksCommandHandlerParameter(nameOfDatabase, NameOfTable,
                                                          diskID, projectsID, bladeTypesID)
    initInTable = handler.initFunction(9, parameters)

    print(initInTable)


    #9. Заполнение таблицы Slots
    NameOfTable = appSettings.getValue(appSettings.slotNameOfTable)
    slotsID = appSettings.getValue(appSettings.slotsIDName)

    thicknessSlot = appSettings.getValue(appSettings.thicknessSlot_name)
    TthicknessSlot = appSettings.getValue(appSettings.TthicknessSlot_name)
    angleAxisSlot = appSettings.getValue(appSettings.angleAxisSlot_name)
    TAngleAxisSlot = appSettings.getValue(appSettings.TAngleAxisSlot_name)
    angleSlot = appSettings.getValue(appSettings.angleSlot_name)
    TAngleSlot = appSettings.getValue(appSettings.TAngleSlot_name)
    externalID = appSettings.getValue(appSettings.slotsExternalIDName)

    parameters = GenerateSlotsCommandHandlerParameter(nameOfDatabase, NameOfTable, slotsID, thicknessSlot, TthicknessSlot,
                                                        angleAxisSlot, TAngleAxisSlot, angleSlot, TAngleSlot,
                                                    diskTypesNumberBladeDisk, externalID, diskID)
    initInTable = handler.initFunction(10, parameters)

    print(initInTable)

    #10. Заполнение таблицы Displacements
    NameOfTable = appSettings.getValue(appSettings.displacementNameOfTable)
    displacementID= appSettings.getValue(appSettings.displacementIDName)
    displacementType = appSettings.getValue(appSettings.displacementDisplacementTypeName)
    parameters = GenerateDisplacementsCommandHandlerParameter(nameOfDatabase, NameOfTable, displacementID,
                                                              projectsID,
                                                              displacementType)
    initInTable = handler.initFunction(5, parameters)
    print(initInTable)

    #11. Заполнение таблицы DisplacementContents
    NameOfTable = appSettings.getValue(appSettings.displacementContentsNameOfTable)
    displacementContentsID = appSettings.getValue(appSettings.displacementContentsIDName)
    displacementContentsPosition= appSettings.getValue(appSettings.displacementContentsPositionName)
    parameters = GenerateDisplacementContentsCommandHandlerParameter(nameOfDatabase, NameOfTable, displacementContentsID,
                                                              displacementID,
                                                              bladesID, displacementContentsPosition)
    initInTable = handler.initFunction(6, parameters)
    print(initInTable)

    appSettings.setValue(appSettings.displacementContentsIDName, displacementContentsID + diskTypesNumberBladeDisk)
    appSettings.setValue(appSettings.displacementIDName, displacementID + 1)
    appSettings.setValue(appSettings.diskIDName, diskID + 1)
    appSettings.setValue(appSettings.bladesIDName, bladesID + diskTypesNumberBladeDisk)
    appSettings.setValue(appSettings.slotsIDName, slotsID + diskTypesNumberBladeDisk)
    appSettings.setValue(appSettings.projectsIDName, projectsID + 1)



