file_path = "test.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    num_lines_to_read = 2
    lines = []
    
    # Read the specified number of lines using a loop
    for _ in range(num_lines_to_read):
        line = file.readline().strip()
        
        if not line:
            break  # Break if there are no more lines to read
        lines.append(line)

# Print the lines
for line in lines:
    print(line)
