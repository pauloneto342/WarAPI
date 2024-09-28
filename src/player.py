from objective import Objective

class Player():
    def __init__(self, name, color=None, army=0):
        self.__name = name
        self.__color = color
        self.__army = army
        self.__my_territories = []
        self.__objective = None

    def get_name(self):
        return self.__name

    def get_objective(self):
        return self.__objective
    
    def set_objective(self, task):
        self.__objective = task

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    def get_army(self):
        return self.__army
    
    def add_army(self, size):
        self.__army += size



