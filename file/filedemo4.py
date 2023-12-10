name = "raj"
age = 20

file = open("stu.txt","a")
file.write("name =")
file.write(name)
file.write("\n")
file.write("age =")
#file.write(()age)
#typecast = str(age)
file.write(str(age))
file.close()