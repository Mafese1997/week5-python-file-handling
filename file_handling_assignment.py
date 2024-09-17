# file_handling_assignment.py

def create_file():
    try:
        # Creating and writing to the file
        with open('my_file.txt', 'w') as file:
            file.write("Line 1: This is a string.\n")
            file.write("Line 2: The number 12345.\n")
            file.write("Line 3: Another string with a number 67890.\n")
        print("File created and initial content written.")
    except (PermissionError, IOError) as e:
        print(f"Error creating or writing to the file: {e}")
    finally:
        print("File creation and writing operation complete.")

def read_file():
    try:
        # Reading and displaying the file content
        with open('my_file.txt', 'r') as file:
            content = file.read()
        print("\nFile contents:")
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read the file.")
    finally:
        print("File reading operation complete.")

def append_to_file():
    try:
        # Appending to the file
        with open('my_file.txt', 'a') as file:
            file.write("Additional Line 1: More text.\n")
            file.write("Additional Line 2: Another line of text.\n")
            file.write("Additional Line 3: Yet another line.\n")
        print("Additional content appended.")
    except (PermissionError, IOError) as e:
        print(f"Error appending to the file: {e}")
    finally:
        print("File appending operation complete.")

# Execute the functions
create_file()
read_file()
append_to_file()
read_file()  # Read again to show appended content
