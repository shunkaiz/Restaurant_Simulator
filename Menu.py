# Name:  Shunkai Zhang
# ITP 115, Spring 2018
# Final Project
# USC email shunkaiz@usc.edu

from  MenuItem import MenuItem
class Menu(object):
    MENU_ITEM_TYPES = ['Drink', 'Appetizer', 'Entree', 'Dessert']
    def __init__(self, fileName):
        self.__menuItemDictionary = {}
        fileIn = open(fileName, 'r')
        for line in fileIn:
            attr = line.strip().split(',')
            type = attr[1]
            item = MenuItem(attr[0], attr[1], float(attr[2]), attr[3])
            if type in self.__menuItemDictionary:
                self.__menuItemDictionary[type].append(item)
            else:
                itemList = [item]
                self.__menuItemDictionary[type] = itemList

    def getMenuItem(self, type, index):
        return self.__menuItemDictionary[type][index]

    def getMenuDic(self):
        return self.__menuItemDictionary

    def printMenuItemsByType(self, type):
        list = self.__menuItemDictionary[type]
        print('Lets now select', type)
        count = 1
        for item in list:
            print('OPTION',str(count),item)
            count += 1

    def getNumMenuItemsByType(self, type):
        if type in self.__menuItemDictionary:
            return len(self.__menuItemDictionary[type])
        else:
            return 0
