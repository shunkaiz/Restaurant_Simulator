# Name:  Shunkai Zhang
# ITP 115, Spring 2018
# Final Project
# USC email shunkaiz@usc.edu

from Menu import Menu
from Diner import Diner

class Waiter(object):
    def __init__(self, menu):
        self.__menu = menu
        self.__diners = []

    def addDiner(self, diner):
        self.__diners.append(diner)

    def getDiners(self):
        return self.__diners

    def getNumDiners(self):
        return len(self.__diners)

    def printDinerStatuses(self):
        seatedDiner = []
        orderingDiner = []
        eatingDiner = []
        payingDiner = []
        leavingDiner = []
        for diner in self.__diners:
            currStatus = diner.getStatusIndex()
            if currStatus == 0:
                seatedDiner.append(diner)
            elif currStatus == 1:
                orderingDiner.append(diner)
            elif currStatus == 2:
                eatingDiner.append(diner)
            elif currStatus == 3:
                payingDiner.append(diner)
            elif currStatus == 4:
                leavingDiner.append(diner)
        print('Seated diners:')
        for diner in seatedDiner:
            print(diner)
        print('Ordering diners:')
        for diner in orderingDiner:
            print(diner)
        print('Eating diners:')
        for diner in eatingDiner:
            print(diner)
        print('Paying diners:')
        for diner in payingDiner:
            print(diner)
        print('Leaving diners')
        for diner in leavingDiner:
            print(diner)

    def takeOrders(self):
        for diner in self.__diners:
            if diner.getStatusIndex() == 1:
                for type in Menu.MENU_ITEM_TYPES:
                    #self.__menu.printMenuItemsByType(type)
                    #validOption = False
                    itemNum = self.__menu.getNumMenuItemsByType(type)
                    # while not validOption:
                    #     choice = int(input('Select a menu item'))
                    #     if choice >=1 and choice <= itemNum:
                    #         validOption = True
                    #     else:
                    #         print('We dont have this option. Try again')
                    diner.addOrder(self.__menu.getMenuItem(type, 0))
                    #diner.printOrder()

    def ringUpDiners(self):
        for diner in self.__diners:
            if diner.getStatusIndex() == 3:
                cost = diner.calculateMealCost()
                print('You total cost is', end='')
                print("%.2f" % cost)

    def removeDoneDiners(self):
        for num in range(len(self.__diners)-1, -1, -1):
            if self.__diners[num].getStatusIndex() == 4:
                print()
                print('-------------',self.__diners[num].getName(), 'Thank you!')
                del self.__diners[num]

    def advanceDiners(self):
        #self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        for diner in self.__diners:
            diner.updateStatus()