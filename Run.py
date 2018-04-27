"""
ITP 115, SP18 Final project
Run this file in order to start the restaurant simulation program
"""

# Name:  Shunkai Zhang
# ITP 115, Spring 2018
# Final Project
# USC email shunkaiz@usc.edu

import datetime
from tkinter import *

#from GUI import GUI
# TODO 0: uncomment the following 3 import statements when you create these files
from Menu import Menu
from Waiter import Waiter
from RestaurantHelper import RestaurantHelper
from GUI import GUI
from Diner import Diner
def main():
    RESTAURANT_NAME = "Wuxi"  # TODO 1: add your own restaurant name in the quotes
    restaurantTime = datetime.datetime(2017, 5, 1, 5, 0)
    #Create the menu object
    menu = Menu("menu.csv")  # TODO 2: uncomment this once the Menu class is implemented
    #create the waiter object using the created Menu we just created
    waiter = Waiter(menu)  # TODO 4: uncomment this one the Waiter class is implemented

    dinerList = []

    print("Welcome to " + RESTAURANT_NAME + "!")
    print(RESTAURANT_NAME + " is now open for dinner.\n")

    for i in range(21):
        restaurantTime += datetime.timedelta(minutes=15)
        potentialDiner = RestaurantHelper.randomDinerGenerator(restaurantTime)
        if potentialDiner is not None:
            dinerList.append(potentialDiner)
        else:
            dinerList.append(str(restaurantTime))

    # create main GUI
    root = Tk()
    root.title("Resturant")
    root.geometry("800x600")
    myAPP = GUI(root, waiter, dinerList)
    myAPP.mainloop()
    print('end of gui')
    print("Goodbye!")

main()
