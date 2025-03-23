# Add the pynput (only the keyboard) and the controller to the project
from pynput.keyboard import Controller

# create a new function to control the keyboard
def controlKeyboard() :
    keyboard = Controller() # Call the Controller object and store it in a variable
    keyboard.type("Hello World") # Add the text which needed to be automatically typed when the function is called

controlKeyboard() 