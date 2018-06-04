file = open("1.txt", 'r')
# read a file
read = file.read()
print(read)
file.close()


file = open("1.txt", 'r')
# print only 10 word
read = file.read(10)
print(read)
file.close()

file = open("1.txt", 'r')
# print 1 line
read = file.readline()
print(read)
file.close()

file = open("1.txt", 'w')
# write a data in a file and read
file.write("this is the text written to the file")
file.close()
file = open("1.txt", 'r')
read = file.read()
print(read)
file.close()
file = open("1.txt", 'a') # append mode
file.write("\n this is the new line")
file.close()


