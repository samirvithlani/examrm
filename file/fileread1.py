#file = open("stu.txt","r")

#print(file.read()) # read all the content of the file character by character

with open("stu.txt") as file:
    data = file.read()

print(data.upper())


# for i in file:
#     print(i,end="")



