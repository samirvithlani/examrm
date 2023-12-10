file = open("test.txt","r")

#data = file.readlines()
# data = file.readline()
# print(data)


while True:
    data = file.readline()
    print(data,end="")
    if data == "":
        break


# for i in data:
#     print(i,end="")