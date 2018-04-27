# Name:  Shunkai Zhang
# ITP 115, Spring 2018
# Final Project
# USC email shunkaiz@usc.edu

class Diner(object):
    STATUSES = ['seated', 'ordering', 'eating', 'paying', 'leaving']

    def __init__(self, name, enterTime):
        self.__name = name
        self.__order = []
        self.__status = 0
        self.__enterTime = enterTime

    def getName(self):
        return self.__name

    def getTime(self):
        #print(self.__enterTime)
        return self.__enterTime

    def setName(self, name):
        self.__name = name

    def getOrder(self, order):
        return self.__order

    def addOrder(self, order):
        self.__order.append(order)

    def getStatus(self):
        return Diner.STATUSES[self.__status]

    def setStatus(self, status):
        self.__status = status

    def getStatusIndex(self):
        return self.__status

    def updateStatus(self):
        self.__status += 1

    def printOrder(self):
        for food in self.__order:
            print(food)

    def calculateMealCost(self):
        total = 0.0
        for food in self.__order:
            total += food.getPrice()
        return total

    def __str__(self):
        result = ""
        result += self.__name
        status = Diner.STATUSES[self.__status]
        result += ' is currently '+ status
        return result