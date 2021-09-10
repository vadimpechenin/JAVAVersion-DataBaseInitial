"""
Описывает базовый класс для тестирования комплектации лопаток
"""

from handlers.generateProjects.generateProjectsCommandHandler import GenerateProjectsCommandHandler
from handlers.generateBladeTypes.generateBladeTypesHandler import GenerateBladeTypesCommandHandler

class MainHandler():
    def __init__(self):
        self.dict = {}
        self.dict[0] = GenerateProjectsCommandHandler()
        self.dict[1] = GenerateBladeTypesCommandHandler()

    def initFunction(self,code_request, parameter):
        result = None
        if code_request in self.dict:
            handler = self.dict[code_request]
            result = handler.execute(parameter)

        return result