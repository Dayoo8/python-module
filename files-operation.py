file = open("newfile.pdf", "w")
file.write("Hello world. welcome to my first line if code")

file = open("newfile.pdf", "r")
data = file.read()
print(data)

modified_lines = [line.upper() + '\n' for line in data.splitlines()]
with open("outputfile.txt", "w") as outfile:
	outfile.writelines(modified_lines)
print("File modified successfully.")



try:
    with open("newfile.pdf", "r") as file:
        content = file.read()
        print("\n Hello world. welcome to my first line if code \n")
        print(content)
except FileNotFoundError:
    print(f"Error: The file 'newfile.pdf' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read 'newfile.pdf'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    