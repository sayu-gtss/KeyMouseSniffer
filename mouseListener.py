from pynput.mouse import Listener

# create a new function to take the coordinations of the mouse movement as inputs and append them to a file
def writetofile(x,y):
    print('Position of current mouse: {0}'.format((x, y))) # To format the string to print the mouse's position to relace (x,y) coordinations with {0}

# Assign the instance of the Listener to a variable called 'listener' 
with Listener(on_move=writetofile) as listener: 
    listener.join()