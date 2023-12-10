try:
    with open("exam.txt","x") as file:
        file.write("hello world")
except FileExistsError:
    print("file already exists")        
    
    