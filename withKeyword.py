# Open a file and assign it to 'file' variable and append to it
with open("log.txt", "a") as file:
    file.write("Hello World\n")