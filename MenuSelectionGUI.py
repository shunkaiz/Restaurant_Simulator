from tkinter import *
from Diner import Diner
from MenuItem import MenuItem
from Menu import Menu

class MenuSelectionGUI(Frame):
    MENU_ITEM_TYPES = ['Drink', 'Appetizer', 'Entree', 'Dessert']
    def __init__(self, root, main, diner, menu):
        super().__init__(root)
        self.grid()
        self.root = root
        self.main = main
        self.v1 = IntVar(self)
        self.v1.set(1)
        self.v2 = IntVar(self)
        self.v2.set(1)
        self.v3 = IntVar(self)
        self.v3.set(1)
        self.v4 = IntVar(self)
        self.v4.set(1)
        self.menu = menu.getMenuDic()
        self.diner = diner

        # creating radioboxes for each type in menu
        for i in range(len(self.menu['Drink'])):
            b = Radiobutton(self, variable=self.v1, value=i+1, text="Drink Option "+str(i+1))
            b.grid(row = 0, column = i)

        for i in range(len(self.menu['Appetizer'])):
            b = Radiobutton(self, variable=self.v2, value=i+1, text="Appetize Option "+str(i+1))
            b.grid(row = 1, column = i)

        for i in range(len(self.menu['Entree'])):
            b = Radiobutton(self, variable=self.v3, value=i+1, text="Entree Option "+str(i+1))
            b.grid(row = 2, column = i)

        for i in range(len(self.menu['Dessert'])):
            b = Radiobutton(self, variable=self.v4, value=i+1, text="Dessert Option "+str(i+1))
            b.grid(row = 3, column = i)

        self.__confirmButton = Button(self, text = 'Confirm Order', command = self.makeChoice)
        self.__confirmButton.grid(row=4, column=0)

        self.__currFood = Text(self)
        self.__currFood.grid(row = 5, columnspan = 4)

        self.displayMenu()

    def displayMenu(self):
        for type in MenuSelectionGUI.MENU_ITEM_TYPES:
            self.__currFood.insert(END, '\nCurrent type is'+ type + '\n\n')
            for item in self.menu[type]:
                self.__currFood.insert(END,item.getItemInfo()+'\n')



    def makeChoice(self):
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[0]][self.v1.get()-1])
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[1]][self.v2.get()-1])
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[2]][self.v3.get()-1])
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[3]][self.v4.get()-1])
        #self.main.grab_release()
        self.main.enableNext()
        self.root.quit()