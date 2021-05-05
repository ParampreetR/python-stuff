#!/usr/bin/python3

# Health management system.......
# total 3 clients, Rohan, Harry and Hamad
# total 6 files, each person 2 fiels one for food and one for exercise
# choice 1 is for food and choice 2 is for exercise
import datetime

users = ["harry", "rohan", "hamad"]
tasks = ["food", "exercise"]

def get_user_input():
    """
    take user input and checks wheather the input is valid or not
    """
    
    print("\nWhich user u want to select?\n1.Harry\n2.Rohan\n3.Hamad\n")
    user_selector = int(input("Please select user : "))
    
    if user_selector == 1:
        print("+ Harry bhai's profile loaded successfully")
  
    elif user_selector == 2:
        print("+ Rohan bhai's profile loaded successfully")
  
    elif user_selector == 3:
        print("+ Hamad bhai's profile loaded successfully")
 
    else:
        print("- Pls enter valid input")
        exit()

    return users[user_selector - 1]

def get_task_input():
    """
    take task input and checks the input between food and exercise....this funciton will exit the program if the input is anything except 1 and 2
    """   
    
    print("\nWhich task you want to lock?\n1.food\n2.exercise\n")
    task_selector = int(input("Pls enter your choice : "))
    
    if task_selector == 1:
        print("+ Selected food section")

    elif task_selector == 2:
        print("+ Selected exercise section")

    else:
        print("- Pls enter valid input")
        exit()

    return tasks[task_selector - 1]

def get_operation_input():
    """
    take operation input and return symbolic number to represent operation. 1 for insert and 2 for retrieve

    """
    print("\nWhich operation u want to perform?")
    task_selector = int(input("1.Insert data\n2.Retrieve data\n\nEnter your choice : "))

    if task_selector == 1:
        print("+ OK! Insertion activated")
        return task_selector


    elif task_selector == 2:
        print("+ OK! Retrieving activated")
        return task_selector

    else:
        print("- Pls enter valid input")
        exit()


def insert_data(username, taskname):
    filename = username + "_" + taskname + ".txt"

    try:
        with open(filename, "a") as f:
            data_to_insert = input("Input data to be inserted\n> ")
            dt = str(datetime.datetime.now())
            file_content = "[" + dt[:19] + "]" + " >>> " + data_to_insert + "\n"
            f.write(file_content)
    
        print("+ Content written successfully")
    
    except Exception as err:
        print("!! Unexpected error in creating file and saving data\n" + err)
        exit(-1)
        


def retrieve_data(username, taskname):
    filename = username + "_" + taskname + ".txt"
    
    try:
        with open(filename) as f:
            return f.read()

    except FileNotFoundError:
        return "! No data found"

    except Exception as err:
        print("!! Unexpected error in retrieving file\n" + err)
        exit(-1)

# starting of the code.....
if __name__ == "__main__":
    username = get_user_input()
    taskname = get_task_input()
    operation = get_operation_input()


    if operation == 1:
        insert_data(username, taskname)
    elif operation == 2:
        data = retrieve_data(username, taskname)
        print(data)
    
    exit(0)
