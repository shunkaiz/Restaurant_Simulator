from tkinter import *
from MenuSelectionGUI import MenuSelectionGUI

class OrderingDinerGUI (Frame):
    def __init__(self, rootWindow, dinerName, menuMap, diner):
        super().__init__(rootWindow)
        self.__dinerName = Label(self, text = dinerName)
        self.__orderButton = Button(self,text='Make Order' ,command= self.openMenuList)

        self.__dinerName.grid(column = 0, row = 0)
        self.__orderButton.grid(column = 1, row = 0)

        self.menuList = menuMap

    def openMenuList(self):
        root = Tk()
        menuList = MenuSelectionGUI(root, self.menuList)
        menuList.mainloop()

