from tkinter import *
from Diner import Diner
from MenuItem import MenuItem
from Menu import Menu

class MenuSelectionGUI(Frame):
    MENU_ITEM_TYPES = ['Drink', 'Appetizer', 'Entree', 'Dessert']
    def __init__(self, root, main, diner, menu):
        super().__init__(root)
        self.grid()
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

        for i in range(len(self.menu['Drink'])):
            b = Radiobutton(self, variable=self.v1, value=i+1, text="Drink Option "+str(i+1))
            b.grid(row = 0, column = i)

        # self.__drinkOptionOne = Radiobutton(self, variable=self.__v1, value = 1, text="Drink Option 1")
        # self.__drinkOptionTwo = Radiobutton(self, variable=self.__v1, value = 2,  text="Drink Option 2")
        # self.__drinkOptionThree = Radiobutton(self, variable=self.__v1, value = 3, text="Drink Option 3")
        # self.__drinkOptionFour = Radiobutton(self, variable=self.__v1, value = 4,  text="Drink Option 4")

        for i in range(len(self.menu['Appetizer'])):
            b = Radiobutton(self, variable=self.v2, value=i+1, text="Appetize Option "+str(i+1))
            b.grid(row = 1, column = i)

        # self.__AppetizerOptionOne = Radiobutton(self, variable=self.__v2, value = 1, text="Appetize Option 1")
        # self.__AppetizerOptionTwo = Radiobutton(self, variable=self.__v2, value = 2, text="Appetize Option 2")
        # self.__AppetizerOptionThree = Radiobutton(self, variable=self.__v2, value = 3, text="Appetize Option 3")
        # self.__AppetizerOptionFour = Radiobutton(self, variable=self.__v2, value = 4, text="Appetize Option 4")

        for i in range(len(self.menu['Entree'])):
            b = Radiobutton(self, variable=self.v3, value=i+1, text="Entree Option "+str(i+1))
            b.grid(row = 2, column = i)

        # self.__EntreeOptionOne = Radiobutton(self, variable=self.__v3, value = 1, text="Entree Option 1")
        # self.__EntreeOptionTwo = Radiobutton(self, variable=self.__v3, value = 2, text="Entree Option 2")
        # self.__EntreeOptionThree = Radiobutton(self, variable=self.__v3, value = 3, text="Entree Option 3")
        # self.__EntreeOptionFour = Radiobutton(self, variable=self.__v3, value = 4, text="Entree Option 4")

        for i in range(len(self.menu['Dessert'])):
            b = Radiobutton(self, variable=self.v4, value=i+1, text="Dessert Option "+str(i+1))
            b.grid(row = 3, column = i)

        # self.__DessertOptionOne = Radiobutton(self, variable=self.__v4, value=1, text="Dessert Option 1")
        # self.__DessertOptionTwo = Radiobutton(self, variable=self.__v4, value=2, text="Dessert Option 2")
        # self.__DessertOptionThree = Radiobutton(self, variable=self.__v4, value=3, text="Dessert Option 3")
        # self.__DessertOptionFour = Radiobutton(self, variable=self.__v4, value=4, text="Dessert Option 4")

        self.__confirmButton = Button(self, text = 'Confirm Order', command = self.makeChoice)


        # self.__drinkOptionOne.grid(row = 0, column = 0)
        # self.__drinkOptionTwo.grid(row = 0, column = 1)
        # self.__drinkOptionThree.grid(row = 0, column = 2)
        # self.__drinkOptionFour.grid(row = 0, column = 3)
        #
        # self.__AppetizerOptionOne.grid(row = 1, column = 0)
        # self.__AppetizerOptionTwo.grid(row = 1, column = 1)
        # self.__AppetizerOptionThree.grid(row = 1, column = 2)
        # self.__AppetizerOptionFour.grid(row = 1, column = 3)
        #
        # self.__EntreeOptionOne.grid(row = 2, column = 0)
        # self.__EntreeOptionTwo.grid(row = 2, column = 1)
        # self.__EntreeOptionThree.grid(row = 2, column = 2)
        # self.__EntreeOptionFour.grid(row = 2, column = 3)
        #
        # self.__DessertOptionOne.grid(row = 3, column = 0)
        # self.__DessertOptionTwo.grid(row = 3, column = 1)
        # self.__DessertOptionThree.grid(row = 3, column = 2)
        # self.__DessertOptionFour.grid(row = 3, column = 3)


        self.__confirmButton.grid(row=4, column=0)

        self.__currFood = Text(self)
        self.__currFood.grid(row = 5, columnspan = 4)
        self.displayMenu()

    def displayMenu(self):
        #print(self.menu)
        for type in MenuSelectionGUI.MENU_ITEM_TYPES:
            self.__currFood.insert(END, '\nCurrent type is'+ type + '\n\n')
            for item in self.menu[type]:
                self.__currFood.insert(END,item.getItemInfo()+'\n')



    def makeChoice(self):
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[0]][self.v1.get()-1])
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[1]][self.v2.get()-1])
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[2]][self.v3.get()-1])
        self.diner.addOrder(self.menu[MenuSelectionGUI.MENU_ITEM_TYPES[3]][self.v4.get()-1])
        self.main.grab_release()
        self.main.enableNext()
        self.main.disableMenu()
        self.quit()
        self.destroy()
