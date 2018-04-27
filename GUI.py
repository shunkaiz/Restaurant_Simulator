# main GUI for the simulator
# Name:  Shunkai Zhang
# ITP 115, Spring 2018
# Final Project
# USC email shunkaiz@usc.edu



from tkinter import *
from Diner import Diner
from MenuSelectionGUI import MenuSelectionGUI

class GUI(Frame):
    def __init__(self, rootWindow, waiter, dinerList):
        super().__init__(rootWindow)
        self.grid(row = 0)
        self.waiter = waiter
        self.menuMap = waiter.getMenuDic()
        self.dinerList = dinerList
        self.__nextCounter = 0
        self.__labResturantName = Label(self, text='Resturant Name:', font="veranda 16 bold",bg="#44ab3d")
        self.__labResturantName.grid(column = 0,row =0, sticky = 'e',padx=50)

        self.__resturantName = Label(self, font="veranda 16 bold",fg='red', text= 'Wuxi')
        self.__resturantName.grid(row = 0, column = 1, ipadx = 100, sticky = 'w')

        self.__labCurrTime = Label(self, text= 'Current Time:', font="veranda 16 bold")
        self.__labCurrTime.grid(column = 0, row =1, padx = 50, sticky = 'e')

        self.__currTime = Label(self, text = '{:20s}'.format('') , font="veranda 16 bold")
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

        self.__nextButton = Button(self, text = 'Next 15 Min', command = self.updateDiner)
        self.__nextButton.grid(row = 7, column= 1)

        self.__menuButton = Button(self, text= 'make Order', command = self.makeOrder, state = 'disable')
        self.__menuButton.grid(row = 7, column = 0)
        self.__currOrderDiner = None

        self.__payingBox = Text(self, font= 'veranda 16 bold', height = 8)
        self.__payingBox.grid(row = 8,column = 0,columnspan = 2, pady = 10)

        self.__leavingBox = Text(self, font= 'veranda 16 bold', height = 8)
        self.__leavingBox.grid(row = 9, column = 0, columnspan = 2, pady = 10)


    def updateDiner(self):
        self.__newDiner.config(text='')
        self.__payingBox.delete('1.0',END)
        self.__leavingBox.delete('1.0',END)
        if self.__nextCounter < len(self.dinerList):
            if type(self.dinerList[self.__nextCounter])is str:
                self.__currTime.config(text = '{:20s}'.format(str(self.dinerList[self.__nextCounter])))
            elif type(self.dinerList[self.__nextCounter])is Diner:
                self.__currTime.config(text='{:20s}'.format(self.dinerList[self.__nextCounter].getTime()))
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

        # update labels for each type of diner
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
            textVar += diner.getName() + ', '
        self.__payingDiners.config(text = textVar)

        textVar = ''
        self.__leavingDiners.config(text='')
        for diner in leavingDiners:
            textVar += diner.getName() + ', '
        self.__leavingDiners.config(text = textVar)


        # disable next button when making order
        # open new window for menu selection
        if len(orderingDiners) > 0:
            self.enableMenu()
            self.disableNext()
            self.__currOrderDiner = orderingDiners[0]

        # update box text messages for paying and leaving diners
        if len(payingDiners) > 0:
            message = self.waiter.ringUpDiners()
            self.__payingBox.insert(END, message + '\n')

        if len(leavingDiners) >0:
            message = self.waiter.removeDoneDiners()
            self.__leavingBox.insert(END, message + '\n')

        self.waiter.advanceDiners()


    # create a new MenuSelection GUI window
    def makeOrder(self):
        self.disableNext()
        self.disableMenu()
        root = Tk()
        self.__menuOrder  = MenuSelectionGUI(root, self, self.__currOrderDiner, self.menuMap)
        self.__menuOrder.grid(row=8, column=0, columnspan=2)
        root.mainloop()
        root.destroy()


    def disableNext(self):
        self.__nextButton.config(state = 'disable')

    def enableNext(self):
        self.__nextButton.config(state = 'normal')

    def disableMenu(self):
        self.__menuButton.config(state='disable')

    def enableMenu(self):
        self.__menuButton.config(state= 'normal')