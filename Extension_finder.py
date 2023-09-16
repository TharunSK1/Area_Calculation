# Accept the filename from the user
filename = input("Input the Filename: ")

# Split the filename into a list using dot (.) as a separator
parts = filename.split(".")

# Extract the last part as the file extension
if len(parts) > 1:
    extension = parts[-1]
    print(f"The extension of the file is: '{extension}'")
else:
    print("No extension found in the filename.")
