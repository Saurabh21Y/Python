import os

def create(name):
    with open(name, 'x') as file:
        print("The file is created successfully")

def read(name):
   try:
    with open(name, 'r') as file:
        print(file.read())
   except FileNotFoundError:
    print("File not found")

def name_update(name, new_name):
    try:
        os.rename(name, new_name)
        print("The file is updated successfully")
    except FileNotFoundError:
        print("File not found")

def append_file(name,data):
    with open(name, 'a') as file:
        file.write(data)
        print("The file is updated successfully")

def overwrite(name, data):
    with open(name, 'w') as file:
        file.write(data)
        print("The file is updated successfully")

def delete(name):
    try:
        os.remove(name)
        print("The file is deleted successfully")
    except FileNotFoundError:
        print("File not found")


print("""
Press 1 for Create a file.
Press 2 for Read a file.
Press 3 for Update a file.
Press 4 for Delete a file.
Press 5 to exit.
""")

check = int(input("Enter your choice: "))

while check <= 4 and check >=1:
    if check == 1:
        name = input("Enter the name of the file with extension: ")
        create(name)

    elif check == 2:
        name = input("Enter the name of the file with extension: ")
        read(name)

    elif check == 3:
        print("1. Update file name.")
        print("2. Append to a file.")
        print("3. Overwrite a file.")

        check_append = int(input("Enter your option number: "))
        
        if check_append == 1:
            name = input("Enter the name of the file with extension: ")
            new_name = input("Enter the new name of the file with extension: ")
            name_update(name, new_name)

        elif check_append == 2:
            name = input("Enter the name of the file with extension: ")
            print("Enter the data you want to put in it.")
            data = input()
            append_file(name, data)

        elif check_append == 3:
            name = input("Enter the name of the file with extension: ")
            print("Enter the data you want to put in it.")
            data = input()
            overwrite(name, data)

    elif check == 4:
        name = input("Enter the name of the file with extension: ")
        delete(name)

    check = int(input("Enter your choice: "))
