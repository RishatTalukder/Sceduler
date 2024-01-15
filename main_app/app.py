from database import Database
from itertools import zip_longest


class App:
    def __init__(self):
        self.db = Database()  # Create a Database object

    def show_all(self):
        todos = self.db.fetch("Todo")
        
        # fetch all the tasks from the in_progress table
        in_progress = self.db.fetch("inProgress")

        # fetch all the tasks from the completed table
        completed = self.db.fetch("Completed")


        # Find the maximum length of data in each column
        max_len_todo = max((len(str(todo[0])) for todo in todos), default=20) if todos else 20
        max_len_inp = max((len(str(inp[0])) for inp in in_progress), default=20) if in_progress else 20
        max_len_comp = max((len(str(comp[0])) for comp in completed), default=20) if completed else 20

        # Use the maximum length to format the table
        print(f"|{'TODOs':^{max_len_todo}}|{'in progress':^{max_len_inp}}|{'completed':^{max_len_comp}}|")
        print(f"|{'-'*max_len_todo}|{'-'*max_len_inp}|{'-'*max_len_comp}|")
        for todo, inp, comp in zip_longest(todos, in_progress, completed, fillvalue=" "):
            print(f"|{str(todo[0]):^{max_len_todo}}|{str(inp[0]):^{max_len_inp}}|{str(comp[0]):^{max_len_comp}}|")
        print(f"|{'-'*max_len_todo}|{'-'*max_len_inp}|{'-'*max_len_comp}|")

    def add_task(self, task):
        self.db.insert("Todo", task) 
        print(
            f"Task '{task}' added to the Todo list"
        )  # print a message to the user that the task has been added

    def removable_tasks(
        self,
    ):
        todos = self.db.fetch("Todo")
        in_progress = self.db.fetch("inProgress")

        print(f"|{'index':^5}|{'TODOs':^20}|{'in progress':^20}|")
        print(f"|{'-'*5}|{'-'*20}|{'-'*20}|")

        for i in range(max(len(todos), len(in_progress))):
            try:
                print(f"|{i:^5}|{todos[i][0]:^20}|{in_progress[i][0]:^20}|")
            except IndexError:
                if len(todos) > len(in_progress):
                    print(f"|{i:^5}|{todos[i][0]:^20}|{'':^20}|")
                elif len(in_progress) > len(todos):
                    print(f"|{i:^5}|{'':^20}|{in_progress[i][0]:^20}|")

        print(f"|{'-'*5}|{'-'*20}|{'-'*20}|")

        return todos, in_progress

    def remove_task(
        self,
    ):
        todos, in_progress = self.removable_tasks()
        table = int(
            input("1 for Todo, 2 for inProgress, 0 to Cancel: ")
        )  # ask the user to select a table
        index = int(
            input("Enter the index of the task you want to remove: ")
        )  # ask the user to select a task

        if table == 1:
            self.db.delete("Todo", todos[index][0])
            print(
                f"Task '{todos[index][0]}' removed from the Todo list"
            )  # print a message to the user that the task has been removed

        elif table == 2:
            self.db.delete("inProgress", in_progress[index][0])
            print(
                f"Task '{in_progress[index][0]}' removed from the inProgress list"
            )  # print a message to the user that the task has been removed

        elif table == 0:
            print(
                "Canceled"
            )  # print a message to the user that the task has been removed

    def edit_task(self):
        todos = self.db.fetch("Todo")

        print(f"|{'index':^5}|{'TODOs':^20}|")

        for i in range(len(todos)):
            print(f"|{i:^5}|{todos[i][0]:^20}|")

        print(f"|{'-'*5}|{'-'*20}|")

        index = int(
            input("Enter the index of the task you want to edit: ")
        )  # ask the user to select a task

        new_task = input(
            "Enter the edtied task: "
        )  # ask the user to enter the new task

        self.db.update("Todo", todos[index][0], new_task)

        print(
            f"Task '{todos[index][0]}' edited to '{new_task}'"
        )  # print a message to the user that the task has been edited

    def empty_todo(self):
        print(
            "do you want to add a task to the Todo list?"
        )  # ask the user if they want to add a task to the Todo list
        choice = input("y/n: ")  # ask the user to select an option
        if choice == "y":
            task = input("Enter the task: ")  # ask the user to enter a task
            self.add_task(task)  # add the task to the Todo list
            return True
        else:
            print("Canceled")  # print a message
            return False

    def add_to_in_progress(
        self,
    ):
        (
            todos,
            in_progress,
        ) = self.removable_tasks()  # show all the tasks in the Todo or inProgress list
        if len(in_progress) == 0:  # if the inProgress list is empty
            if len(todos) == 0:  # if the Todo list is empty
                print("No tasks to add to the inProgress list")  # print a message
                added_to_the_todo = self.empty_todo()  # call the empty_todo method

                if added_to_the_todo:
                    self.add_to_in_progress()  # call the add_to_in_progress method again

            else:
                self.db.insert(
                    "inProgress", todos[0][0]
                )  # insert the first task from the Todo list to the inProgress list
                self.db.delete(
                    "Todo", todos[0][0]
                )  # delete the task from the Todo list
                print(
                    f"Task '{todos[0][0]}' was directly added to the inProgress list because the in progress list was empty"
                )  # print a message

        else:
            if len(todos) == 0:  # if the Todo list is empty
                print("No tasks to add to the inProgress list")  # print a message
                added_to_the_todo = self.empty_todo()  # call the empty_todo method

                if added_to_the_todo:
                    self.add_to_in_progress()  # call the add_to_in_progress method again

            else:
                print(
                    f"Task '{todos[0][0]}' can be added to the inProgress list"
                )  # print a message
                print(
                    "Do you want to add it?"
                )  # ask the user if they want to add the task to the inProgress list
                choice = input("y/n: ")  # ask the user to select an option
                if choice == "y":
                    self.db.insert(
                        "inProgress", todos[0][0]
                    )  # insert the first task from the Todo list to the inProgress list
                    self.db.delete(
                        "Todo", todos[0][0]
                    )  # delete the task from the Todo list
                    print(
                        f"Task '{todos[0][0]}' added to the inProgress list"
                    )  # print a message
                else:
                    print("Canceled")  # print a message

    def show_in_progress(self):
        in_progress = self.db.fetch('inProgress') # fetch all the tasks from the inProgress table

        # print all the tasks
        print(f"|{'index':^5}|{'in progress':^20}|")
        print(f"|{'-'*5}|{'-'*20}|")

        for i in range(len(in_progress)):
            print(f"|{i:^5}|{in_progress[i][0]:^20}|")

        print(f"|{'-'*5}|{'-'*20}|")

    def add_to_completed(self):
        in_progress = self.db.fetch('inProgress') # fetch all the tasks from the inProgress table
        if len(in_progress) == 0: # if the inProgress list is empty
            print("No tasks to add to the completed list") # print a message
            print("Do you want to add a task to the inProgress list?") # ask the user if they want to add a task to the inProgress list
            choice = input("y/n: ") # ask the user to select an option
            if choice == 'y':
                self.add_to_in_progress() # call the add_to_in_progress method
                self.add_to_completed() # call the add_to_completed method again
            else:
                print("Canceled") # print a message

        else:
            print(f"which task do you want to add to the completed list?")
            self.show_in_progress() # call the show_in_progress method
            index = int(input("Enter the index of the task: "))
            self.db.insert('Completed', in_progress[index][0])
            self.db.delete('inProgress', in_progress[index][0])
            print(f"Task '{in_progress[index][0]}' added to the completed list")

    def reset(self):
        self.db.delete_all()
        print("All tasks deleted")

    def end(self):
        self.db.close()
        print("Bye!")
