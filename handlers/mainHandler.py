"""
Описывает базовый класс для тестирования комплектации лопаток
"""

from handlers.generateProjects.generateProjectsCommandHandler import GenerateProjectsCommandHandler
from handlers.generateBladeTypes.generateBladeTypesHandler import GenerateBladeTypesCommandHandler
from handlers.generateBlades.generateBladesCommandHandler import GenerateBladesCommandHandler
from handlers.parameterDescriptions.parameterDescriptionsСommandHandler import ParameterDescriptionsСommandHandler
from handlers.parameterValues.parameterValuesСommandHandler import ParameterValuesСommandHandler
from handlers.generateDisplacements.generateDisplacementsCommandHandler import GenerateDisplacementsCommandHandler
from handlers.generateDisplacementContents.generateDisplacementContentsCommandHandler import GenerateDisplacementContentsCommandHandler

from handlers.generateDiskTypes.generateDiskTypesHandler import GenerateDiskTypesCommandHandler
from handlers.parameterDiskValues.generateParameterDiskValuesCommandHandler import ParameterDiskValuesСommandHandler
from handlers.generateDisks.generateDisksCommandHandler import GenerateDisksCommandHandler
from handlers.generateSlots.generateSlotsCommandHandler import GenerateSlotsCommandHandler

class MainHandler():
    def __init__(self):
        self.dict = {}
        self.dict[0] = GenerateProjectsCommandHandler()
        self.dict[1] = GenerateBladeTypesCommandHandler()
        self.dict[2] = GenerateBladesCommandHandler()
        self.dict[3] = ParameterDescriptionsСommandHandler()
        self.dict[4] = ParameterValuesСommandHandler()
        self.dict[5] = GenerateDisplacementsCommandHandler()
        self.dict[6] = GenerateDisplacementContentsCommandHandler()

        self.dict[7] = GenerateDiskTypesCommandHandler()
        self.dict[8] = ParameterDiskValuesСommandHandler()
        self.dict[9] = GenerateDisksCommandHandler()
        self.dict[10] = GenerateSlotsCommandHandler()

    def initFunction(self,code_request, parameter):
        result = None
        if code_request in self.dict:
            handler = self.dict[code_request]
            result = handler.execute(parameter)

        return result