def wirte_data():
    f = open("filedemo9.txt", "w")
    f.write("Hello")
    f.write("World")
    f.close()
    
def read_data():
    f = open("filedemo9.txt", "r")
    data = f.read()
    print(data)
    f.close()    


print("enter 1 for write data in file")
print("enter 2 for read data from file")

choice = int(input("enter your choice"))
if choice == 1:
    wirte_data()
if choice == 2:
    read_data()

else:
    print("invalid choice")        




