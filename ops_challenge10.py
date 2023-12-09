# Import necessary library
import os

# Define filename
filename = "tommy.txt"

# Create the file and open it for writing
with open(filename, "t") as f:
    # Append three lines to the file
    f.write("Tommy is the greatest")
    

# Open the file for reading
with open(filename, "r") as f:
    # Read the first line
    first_line = f.readline()

# Print the first line
print(first_line)

# Close the file
f.close()

# Delete the file
os.remove(filename)

print(f"File '{filename}' successfully created, appended to, read from, and deleted.")
