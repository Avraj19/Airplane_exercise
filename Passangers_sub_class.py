class Passengers:

    def __init__(self, name, passport_id):
        self.__name = name
        self.__passport_id = passport_id

    def get_name(self):
        return self.__name

    def get_passport_id(self):
        return self.__passport_id
