# File Read & Write Challenge 
# Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

# Get the filename from the user
filename = input("Enter the name of the file: ")

try:
    # Open the file and read its contents
    with open(filename) as file:
        contents = file.read()

    # Modify the contents
    modified_contents = contents.upper()

    # Open a new file and write the modified contents
    with open(f"{filename}_modified.txt", "w") as file:
        file.write(modified_contents)

    print(f"Modified contents written to {filename}_modified.txt")

except FileNotFoundError:
    print(f"Error: {filename} not found.")
except IOError:
    print(f"Error: Unable to read {filename}.")
    