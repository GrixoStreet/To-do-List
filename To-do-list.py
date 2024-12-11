import os
task_lst = []
username = input("Enter your name: ")
print(f"Welcome {username} to the \"To-do list\" app")
if os.path.exists("to-do list.txt"):
    file = open("to-do list.txt", "a")
    fr = open("to-do list.txt", "r")
    i_lines = fr.readlines()
    task_lst.clear()
    for i_line in i_lines:
        i_line = i_line.strip()
        task_lst.append(i_line)
else:
    file = open("to-do list.txt", "x")


def display_menu():
    print("Operations options:- \n1-Add task \n2-Remove task \n3-View tasks \n4-Exit")

def user_choice():
    return input("Choose an operation: ").lower()


# Add task
def add_task():
    task = input("Add a new task: ")
    task_lst.append(task)
    print("===================================================")
    print(f"{task} got added")
    file.write(task+"\n")


# Remove task
def remove_task():
    task_number = int(input("Enter the task number to remove: ")) - 1
    removed_task = task_lst.pop(task_number)
    print("===================================================")
    print(f"{removed_task} got removed")
    with open("to-do list.txt" , "w") as fw:
        for i in task_lst:
            fw.write(i + "\n")

# View tasks
def view_tasks():
    print("===================================================")
    for i in range(len(task_lst)):
        print(f"{i + 1}. {task_lst[i]}")


while True:
    print("===================================================")
    display_menu()
    #User choice
    choice =user_choice()
    if choice == "1" or choice == "add task":
        add_task()
    elif choice == "2" or choice == "remove task":
        remove_task()
    elif choice == "3" or choice == "view tasks":
        view_tasks()
    elif choice == "4" or choice == "exit":
        break
    else:
        print("invalid choice")