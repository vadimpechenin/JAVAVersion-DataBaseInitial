import uuid


class UUIDClass():

    def __init__(self):
        self.projectsIDList = []
        self.bladesIDList = []
        self.bladesTypesIDList = []
        self.parameterValuesIDList = []
        self.parameterDiskValuesIDList = []
        self.parameterDescriptionsIDList = []
        self.diskTypesIDList = []
        self.disksIDList = []
        self.slotsIDList = []
        self.displacementsIDList = []
        self.displacementContentsIDList = []

    @staticmethod
    def geterateUUIDWithout_():
        #Генерация ключа
        myuuid = uuid.uuid4()
        myuuid_str = str(myuuid)
        # Избавление от "-"
        myuuid_str_ = myuuid_str.replace('-', '')
        return myuuid_str_