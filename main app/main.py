from app import App


app = App()

print("Hello, Welcome to the scheduler app") # print a message
print("This is your whole schedule") # print a message
app.show_all() # show all the tasks in the Todo, inProgress and Completed list
print("What do you want to do?") # print a message

while True:
    print("Select an option") # print a message
    print("0. Show all the tasks") # print a message
    print("1. Add a task to the Todo list") # print a message
    print("2. Remove a task from the Todo or inProgress list") # print a message
    print("3. Edit a task from the Todo list") # print a message
    print("4. Add a task to the inProgress list") # print a message
    print("5. Add a task to the completed list") # print a message
    print("6. RESET") # print a message
    print("7. END") # print a message

    choice = int(input("Enter your choice: ")) # ask the user to select an option

    match choice:
        case 0:
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 1:
            task = input("Enter the task: ") # ask the user to enter a task
            app.add_task(task) # add the task to the Todo list
            print("here's the whole schedule") # print a message
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 2:
            app.remove_task() # remove a task from the Todo or inProgress list
            print("here's the whole schedule") # print a message
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 3:
            app.edit_task() # edit a task from the Todo list
            print("here's the whole schedule") # print a message
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 4:
            app.add_to_in_progress() # add a task to the inProgress list
            print("here's the whole schedule") # print a message
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 5:
            app.add_to_completed() # add a task to the completed list
            print("here's the whole schedule") # print a message
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 6:
            app.reset() # delete all the tasks from the Todo, inProgress and Completed list
            print("here's the whole schedule") # print a message
            app.show_all() # show all the tasks in the Todo, inProgress and Completed list

        case 7:
            app.end() # close the connection
            break

        case _:
            print("Invalid choice") # print a message