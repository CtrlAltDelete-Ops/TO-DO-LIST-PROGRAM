#assigning variables to the lists for the uncompleted and completed tasks
tasks = []
completed_tasks = []

def press_enter():
    input("press enter to try again...")

#Defining the function for adding new tasks by appending them to the 'tasks' list
def AddTask(): 
    print("Great! You are ready to Work...")
    task = input("Enter the task you want to accomplish: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to your tasks list. Good job!")
    input("press enter to continue...")

#Defining the function for marking tasks as completeing by appending them to the 'completed_tasks' list
def MarkAsCompleted(): 
    while True:
        ListTasks()
        print("Have you completed any of your tasks?")
        try:
            completed_task = int(input("Enter the number of the task you have accomplished: "))
            if completed_task >= 0 and completed_task < len(tasks):
                completed_tasks.append(tasks[completed_task])
                tasks.pop(completed_task)
                print(f"Task {completed_task} has been completed")
                break
            else:
                print("invalid input")
                press_enter()
                
        except ValueError:
            print("invalid input!")

#Defining the function for removing tasks from the 'tasks' list
def DeleteTask():
    ListTasks()
    print("Do you want to delete any tasks?")
    while True:    
        try:
            TaskToDelete = int(input("Enter the number of the task you want to delete: "))
            if TaskToDelete >= 0 and TaskToDelete < len(tasks):
                tasks.pop(TaskToDelete)
                print(f"Task {TaskToDelete} has been deleted")
                break
            else:
                print("invalid input")
                press_enter()
        except ValueError:
            print("invalid input!")
            press_enter()

    
#Defining the function for listing all tasks in both the completing and uncompleted lists
def ListTasks():
    print("\n")
    print("UNCOMPLETED TASKS")
    if not tasks:
        print("You have no uncompleted tasks")
    else:
        for index, task in enumerate(tasks):
            print(f"#{index}. {task}")
    print("\n")
    print("COMPLETED TASKS")
    if not completed_tasks:
        print("You have no completed tasks")
        print("\n")
    else:
        for index, completed_task in enumerate(completed_tasks):
            print(f"#{index}. {completed_task}")
    

print("\n")
print ("welcome To Ismail's to do list app")
#Creating a loop to make the app run until user presses quit
while True:

    print("\n")
    print("**************************************")
    print("Choose on of the following")

    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. Delete a task")
    print("4. List all tasks")
    print("5. Quit")
    #using try and except to prevent users from inputing datatypes other than int(integer)
    try: 
        #prompting the user to choose an action from the above list
        choice = int(input("Enter your choice 1-5: "))
        #calling the appropriate function for each choice
        if choice == 1:
            AddTask()

        elif choice == 2:
            MarkAsCompleted()

        elif choice == 3:
            DeleteTask()

        elif choice == 4:
            ListTasks()

        elif choice == 5:
            break
            
        else:
            print("the number is not in the list")
            press_enter()

    except ValueError: 
        print("...please choose a number form 1 to 5...")
        press_enter()


        

