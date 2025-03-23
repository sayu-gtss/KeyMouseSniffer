# Open a file and assign it to a variable
file = open("log.txt", "w") 

# Write to the log.txt file and close it
file.write("I am Sayuni")
file.close()

# Append to the file
file = open("log.txt", "a")
file.write("\nHello World")
file.close()

# Read the file 
file = open("log.txt", "r")
filedata = file.read()
print(filedata)
file.close()