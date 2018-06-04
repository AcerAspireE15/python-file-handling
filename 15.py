file = open("demo.txt",'r')
read = file.read()
print(read)
file.close()

file = open("demo.txt","a")
file.write("this is a text line")
file.close()


