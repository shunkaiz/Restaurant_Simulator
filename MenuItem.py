# Name:  Shunkai Zhang
# ITP 115, Spring 2018
# Final Project
# USC email shunkaiz@usc.edu


class MenuItem:
    def __init__(self, name, type, price, description):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__description = description

    def getName(self):
        return self.__namename

    def getType(self):
        return self.__type

    def getPrice(self):
        return self.__price

    def getDescription(self):
        return self.__description

    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setPrice(self, price):
        self.__price = price

    def description(self, description):
        self.__description = description


    def getItemInfo(self):
        return self.__str__()

    def __str__(self):
        result = self.__name
        result += ' (' + self.__type + '): '
        result += str(self.__price) + '\n'
        result += '   '+ self.__description
        return result