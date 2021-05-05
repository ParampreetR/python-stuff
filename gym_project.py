# Health management system.......
# total 3 clients, Rohan, Harry and Hamad
# total 6 files, each person 2 fiels one for food and one for exercise
# choice 1 is for food and choice 2 is for exercise
def getdate():
    import datetime
    return datetime.datetime.now()

def user_selector_check():
    """
    checks input wheather the input is valid or not
    """
    if user_selector == 1:
        print("harry bhai's profile is Locked")
  
    elif user_selector == 2:
        print("rohan bhai's profile is locked")
  
    elif user_selector == 3:
        print("hamad bhai's profile is locked")
 
    else:
        print("pls enter valid input ")
        exit()

def food_or_exercise_check():
    """
    this function checks the input between food and exercise....this funciton will exit the program if the input will be except 1 and 2
    """   
    if food_or_exercise_selector == 1:
        print("locked food section")


    elif food_or_exercise_selector == 2:
        print("locked exercise section")


    else:
        print("pls enter valid input")
        exit()

def insert_or_retrieve_check():
    if insert_or_retrieve_selector == 1:
        print("insertion is activated")


    elif insert_or_retrieve_selector == 2:
        print("retrieve data is activated")

    
    else:
        print("pls enter valid input")
        exit()
# for user 1 ----
def insert_food_data_harry():
    # user harry insert in food
    print("which u want to write in the file pls type >>>")
    content = input()
    
    dt = str(getdate())

    fcontent = "[" + dt[:19] + "]" + " >>> " + content

    with open("harry_food.txt", "a") as f:
        f.write(fcontent)
        f.write("\n")
        print("content written successfully")    

def retrieve_food_data_harry():
    with open("harry_food.txt") as f:
        print(f.read())

def insert_exercise_data_harry():
    print("which u want to write in the file pls type >>>")

    content = input()

    dt = str(getdate())

    fcontent = "[" + dt[:19] + "]" + " >>> " + content

    with open("harry_exercise.txt", "a") as f:
        f.write(fcontent)
        f.write("\n")
        print("content written successfully")
        
def retrieve_exercise_data_harry():
    with open("harry_exercise.txt") as f:
        print(f.read())

# for user 2
def insert_food_data_rohan():
    print("which u want to write in the file pls type >>>")
    content = input()

    dt = str(getdate())

    fcontent = "[" + dt[:19] + "]" + " >>> " + content

    with open("rohan_food.txt", "a") as f:
        f.write(fcontent)
        f.write("\n")
        print("content written successfully")   

def retrieve_food_data_rohan():
    with open("rohan_food.txt") as f:
        print(f.read())

def insert_exercise_data_rohan():
    print("which u want to write in the file pls type >>>")
    content = input()

    dt = str(getdate())

    fcontent = "[" + dt[:19] + "]" + " >>> " + content

    with open("rohan_exercise.txt", "a") as f:
        f.write(fcontent)
        f.write("\n")
        print("content written successfully")   

def retrieve_exercise_data_rohan():
    with open("rohan_exercise.txt") as f:
        print(f.read())

# for user 3
def insert_food_data_hamad():
    print("which u want to write in the file pls type >>>")
    content = input()

    dt = str(getdate())

    fcontent = "[" + dt[:19] + "]" + " >>> " + content

    with open("hamad_food.txt", "a") as f:
        f.write(fcontent)
        f.write("\n")
        print("content written successfully")   

def retrieve_food_data_hamad():
    with open("hamad_food.txt") as f:
        print(f.read())

def insert_exercise_data_hamad():
    print("which u want to write in the file pls type >>>")
    content = input()

    dt = str(getdate())

    fcontent = "[" + dt[:19] + "]" + " >>> " + content

    with open("hamad_exercise.txt", "a") as f:
        f.write(fcontent)
        f.write("\n")
        print("content written successfully")   

def retrieve_exercise_data_hamad():
    with open("hamad_exercise.txt") as f:
        print(f.read())

# starting of the code.....

print("\nWhich user u want to select\n\n1.Harry\n2.Rohan\n3.Hamad\n")
user_selector = int(input("Please select user : "))
user_selector_check()

print("what you want to lock\n\n1.food\n2.exercise")
food_or_exercise_selector = int(input("\nPls enter your choice : "))
food_or_exercise_check()

print("Which operation u want to perform\n")
insert_or_retrieve_selector = int(input("1.Insert data\n2.Retrieve data\n\nEnter your choice : "))
insert_or_retrieve_check()
# print(insert_or_retrieve_selector)
# print(user_selector_check.__doc__)

if user_selector == 1:
    if food_or_exercise_selector == 1:
        if insert_or_retrieve_selector == 1:
            insert_food_data_harry()
        else:
            retrieve_food_data_harry()
    else:
        if insert_or_retrieve_selector == 1:
            insert_exercise_data_harry()
        else:
            retrieve_exercise_data_harry()
    
elif user_selector == 2:
    if food_or_exercise_selector == 1:
        if insert_or_retrieve_selector == 1:
            insert_food_data_rohan()
        else:
            retrieve_food_data_rohan()
    else:
        if insert_or_retrieve_selector == 1:
            insert_exercise_data_rohan()
        else:
            retrieve_exercise_data_rohan()

elif user_selector == 3:
    if food_or_exercise_selector == 1:
        if insert_or_retrieve_selector == 1:
            insert_food_data_hamad()
        else:
            retrieve_food_data_hamad()
    else:
        if insert_or_retrieve_selector == 1:
            insert_exercise_data_hamad()
        else:
            retrieve_exercise_data_hamad()