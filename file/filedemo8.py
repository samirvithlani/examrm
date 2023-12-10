wordtocheck = "oki"
foundline = 0
with open("test.txt","r") as file:
    ln = 1
    for line in file:
        if wordtocheck in line:
            foundline = ln
            break
        else:
            foundline = -1
                            
        ln += 1
        
if(foundline == -1):
    print("Word not found")
else:
    print("Word found at line number",foundline)            

            