# Add the pynput (only the mouse) and the controller to the project
from pynput.mouse import Controller

# create a new function to control the mouse
def controlMouse() :
    # Get user input for x and y coordinates
    try:
        x = int(input("Enter the X coordinate: "))
        y = int(input("Enter the Y coordinate: "))
    except ValueError:
        print("Please enter valid integer values for the coordinates.")
        return

    mouse = Controller() # Call the Controller object and store it in a variable
    mouse.position = (x,y) # Change the mouse position by (10,20) --> (Left to right 10 pixels, Top to bottom 20 pixels), move from Top-Left (0,0) of the screen

controlMouse() 