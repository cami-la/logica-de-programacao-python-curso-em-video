from termcolor import cprint
from list_of_exercises.exercise110 import operations

def play():
  exercise()
  price = float(input("Enter the price: R$" ))

  operations.resume(price, 20, 15)

def exercise():
  cprint("Add the operations.py module created in the previous challenges, a function called summary (), which shows on the screen some information generated by the functions that we already have in the module created so far.\n", "green", attrs=["blink"])
