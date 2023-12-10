#writeLines

file = open("filedemo5.txt", "w")
file.writelines(["Hi this is my first file\n", "Hi this is my second file\n", "Hi this is my third file\n"])
file.close()