# Simple GUI
# Demonstrates creating a window
from tkinter import *
import random
from Diner import Diner
from MenuSelectionGUI import MenuSelectionGUI
from Waiter import Waiter
class GUI(Frame):
    def __init__(self, rootWindow, menuMap, waiter, dinerList):
        super().__init__(rootWindow)
        self.grid(row = 0)
        self.menuMap = menuMap
        self.waiter = waiter
        self.dinerList = dinerList
        self.__nextCounter = 0
        self.__labResturantName = Label(self, text='Resturant Name:', font="veranda 16 bold",bg="#44ab3d")
        self.__labResturantName.grid(column = 0,row =0, sticky = 'e',padx=50)

        self.__resturantName = Label(self, font="veranda 16 bold",fg='red', text= 'Wuxi')
        #self.__resturantName.insert(0, 'Wuxi Grand Resturant')
        self.__resturantName.grid(row = 0, column = 1, ipadx = 100, sticky = 'w')

        self.__labCurrTime = Label(self, text= 'Current Time:', font="veranda 16 bold")
        self.__labCurrTime.grid(column = 0, row =1, padx = 50, sticky = 'e')

        self.__currTime = Label(self, text = '{:20s}'.format('') , font="veranda 16 bold")
        #self.__currTime.insert(0,'sss')
        self.__currTime.grid(row= 1, column = 1, ipadx= 100, sticky = 'w')

        self.__labDiner = Label(self, text='Seated Diner(s):',font= 'veranda 16 bold', anchor= 'w')
        self.__labDiner.grid(column = 0, row = 2, sticky = 'e', padx=50)

        self.__newDiner = Label(self, text = '{:20s}'.format(''), font="veranda 12 bold")
        self.__newDiner.grid(column = 1, row = 2, ipadx = 100, sticky = 'w')

        self.__labelOrderingDiner = Label(self, text='Ordering Diner(s):',font= 'veranda 16 bold', anchor= 'w')
        self.__labelOrderingDiner.grid(column = 0, row = 3, sticky = 'e', padx=50)
        self.__orderingDiners = Label(self,text = '{:20s}'.format(''),font="veranda 12 bold")
        self.__orderingDiners.grid(column = 1, row = 3, ipadx = 100, sticky = 'w')

        self.__labEatingDiner = Label(self, text='Eating Diner(s):',font= 'veranda 16 bold', anchor= 'w')
        self.__labEatingDiner.grid(column = 0, row = 4, sticky = 'e', padx=50)
        self.__eatingDiners = Label(self,text = '{:20s}'.format(''),font="veranda 12 bold")
        self.__eatingDiners.grid(column = 1, row = 4, ipadx = 100, sticky = 'w')

        self.__labPayingDiner = Label(self, text='Paying Diner(s):',font= 'veranda 16 bold', anchor= 'w')
        self.__labPayingDiner.grid(column = 0, row = 5, sticky = 'e', padx=50)
        self.__payingDiners = Label(self,text = '{:20s}'.format(''),font="veranda 12 bold")
        self.__payingDiners.grid(column = 1, row = 5, ipadx = 100, sticky = 'w')

        self.__labLeavingDiner = Label(self, text='Leaving Diner(s):', font='veranda 16 bold', anchor='w')
        self.__labLeavingDiner.grid(column=0, row=6, sticky='e', padx=50)
        self.__leavingDiners = Label(self, text = '{:20s}'.format(''),font="veranda 12 bold")
        self.__leavingDiners.grid(column = 1, row = 6, ipadx = 100, sticky = 'w')

        # menuList = ['milk', 'beer', 'pork']
        # self.__ordingDiner = OrderingDinerGUI(self,'James', self.menuMap, self.dinerList[self.__nextCounter])
        # self.__ordingDiner.grid(row = 7, column = 0, columnspan = 2)


        self.__nextButton = Button(self, text = 'Next 15 Min', command = self.updateDiner)
        self.__nextButton.grid(row = 3, column= 0, columnspan = 2, sticky = 'e')

        self.__menuButton = Button(self, text= 'make Order', command = self.makeOrder, state = 'disable')
        self.__menuButton.grid(row = 7, sticky = 'e')
        self.__currOrderDiner = None

    def updateDiner(self):
        #print(self.dinerList[self.__nextCounter].getName(), str(len(self.dinerList)), str(self.__nextCounter))
        self.__newDiner.config(text='')
        if self.__nextCounter < len(self.dinerList):
            if type(self.dinerList[self.__nextCounter])is str:
                self.__currTime.config(text = '{:20s}'.format(str(self.dinerList[self.__nextCounter])))
            elif type(self.dinerList[self.__nextCounter])is Diner:
                self.__currTime.config(text='{:20s}'.format(self.dinerList[self.__nextCounter].getTime()))
                print(self.dinerList[self.__nextCounter].getName())
                self.__newDiner.config(text='{:20s}'.format(self.dinerList[self.__nextCounter].getName()))
                self.waiter.addDiner(self.dinerList[self.__nextCounter])

            self.__nextCounter += 1
        else:
            self.__newDiner.config(text = 'Restaurant closed')
        orderingDiners = []
        eatingDiners = []
        payingDiners = []
        leavingDiners = []
        diners = self.waiter.getDiners()
        for diner in diners:
            currStatus = diner.getStatusIndex()
            if currStatus == 1:
                orderingDiners.append(diner)
            elif currStatus == 2:
                eatingDiners.append(diner)
            elif currStatus == 3:
                payingDiners.append(diner)
            elif currStatus == 4:
                leavingDiners.append(diner)
        textVar = ''
        self.__orderingDiners.config(text='')
        for diner in orderingDiners:
            textVar += diner.getName() + ', '
        self.__orderingDiners.config(text = textVar)

        textVar = ''
        self.__eatingDiners.config(text='')
        for diner in eatingDiners:
            textVar += diner.getName() + ', '
        self.__eatingDiners.config(text = textVar)

        textVar = ''
        self.__payingDiners.config(text='')
        for diner in payingDiners:
            print(diner.getName())
            textVar += diner.getName() + ', '
        self.__payingDiners.config(text = textVar)

        textVar = ''
        self.__leavingDiners.config(text='')
        for diner in leavingDiners:
            textVar += diner.getName() + ', '
        self.__leavingDiners.config(text = textVar)

        if len(orderingDiners) > 0:
            self.__menuButton.config(state = 'normal')
            self.__nextButton.config(state = 'disable')
            self.__currOrderDiner = orderingDiners[0]

        self.waiter.advanceDiners()

    def makeOrder(self):
        self.disableNext()
        self.grab_set()
        root = Tk()
        self.__menuOrder  = MenuSelectionGUI(root, self, self.__currOrderDiner, self.menuMap)
        self.__menuOrder.grid(row=8, column=0, columnspan=2)
        root.mainloop()

    def disableNext(self):
        self.__nextButton.config(state = 'disable')

    def enableNext(self):
        self.__nextButton.config(state = 'normal')

    def disableMenu(self):
        self.__menuButton.config(state='disable')