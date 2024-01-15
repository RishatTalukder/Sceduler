<h1 align="center"> SCHEDULER </h1>
<h4 align="center"> A command line Time Management Application </h4> 

SO, I have been doing a lot of stuff lately, and I have been learning a lot stuff too. And It became hard for me to keep track of all the things I have in mind. So, I decided to make a command line application to keep track of all the things I have in mind. I don't know what to name it, so i named it ***`SCHEDULER`***. I know it's not a good name, but I will change it later.

Linkedin: https://www.linkedin.com/in/md-rishat-talukder-a22157239/
Github: https://github.com/RishatTalukder/leetcoding
Youtube: https://www.youtube.com/@itvaya

prerequisites:

- basics of python
- basics of sqlite3
- OOP(object oriented programming)

# Table of contents

- [Table of contents](#table-of-contents)
  - [Database](#database)
- [SCHEUDLER](#scheudler)
  - [Building the Database](#building-the-database)
  - [Building the Application](#building-the-application)
  - [Building the Command Line Application](#building-the-command-line-application)
- [Conclusion](#conclusion)


*** Idea behind it:

So, This application will keep track of `Todo`, `in progress` and `completed` tasks. Also I wanted to make it as simple as possible. It's just a list of tasks, and you can add, remove, edit and mark tasks as completed. That's it.

*** Features:

- [x] Add tasks
- [x] Remove tasks
- [x] Edit tasks
  
When, a task is completed, it will be moved to `completed` list. And the item will be removed from `in progress` list. 

We can also add task to `in progress` list manually.

If the In progress list is empty, then the application will ask you to Autometically add a task from `Todo` list to `in progress` list. 

*** Why this is a good beginner project?

This is a good beginner project because it's simple and it's not that hard to make. Also, it's a good project to learn about `database management` and `command line applications`.

*** how will I approach this project?

I will be using `python` and `sqlite3` for this project and I will follow the `OOP` approach. 

First build the `database` and then build the `command line application` and then connect them together.

let's do this.

## Database

So, I will be using `sqlite3` for this project. I will be using `python` to interact with the database.

I will be using `3 tables` for this project.

- `Todo`
- `in progress`
- `Completed`

*** Todo table:

This table will contain all the tasks that we have in mind.

| id | task |
|----|------|
| 1  | task1|
| 2  | task2|
| 3  | task3|

*** in progress table:

This table will contain all the tasks that we are currently working on.

| id | task |
|----|------|
| 1  | task1|
| 2  | task2|
| 3  | task3|

*** completed table:

This table will contain all the tasks that we have completed.

| id | task |
|----|------|
| 1  | task1|
| 2  | task2|
| 3  | task3|

*** How to connect to the database?

```python

# pip install sqlite3
import sqlite3

# connect to the database
conn = sqlite3.connect('scheduler.db')

# create a cursor
cur = conn.cursor()

# execute some sql; there is no table in the database yet
cur.execute("SELECT * FROM Todo")

# fetch all the data
data = cur.fetchall()

# print the data
print(data)

# commit the changes
conn.commit()

# close the connection
conn.close()

```

This is how we `connect` to a `sqlite3` database using `python` and fetch all the data from the already built table `Todo`.

*** How to create a table?

```python

import sqlite3

connection = sqlite3.connect('scheduler.db')

cursor = connection.cursor()

# create a table
cursor.execute("""CREATE TABLE Todo (
    id INTEGER PRIMARY KEY,
    task TEXT
)""")

# commit the changes

connection.commit()

# close the connection

connection.close()

```

This is how we create a table in `sqlite3` using `python`.

*** How to insert data into a table?

```python

import sqlite3

connection = sqlite3.connect('scheduler.db')

cursor = connection.cursor()

# insert data into the table
cursor.execute("INSERT INTO Todo VALUES (1, 'task1')")

# inserting multiple data
cursor.execute("INSERT INTO Todo VALUES (2, 'task2'), (3, 'task3')")

# commit the changes

connection.commit()

# close the connection

connection.close()

```

This is how we insert data into a table in `sqlite3` using `python`.

*** How to fetch data from a table?

```python

import sqlite3

connection = sqlite3.connect('scheduler.db')

cursor = connection.cursor()

# fetch all the data
cursor.execute("SELECT * FROM Todo")

# fetch one data
cursor.execute("SELECT * FROM Todo WHERE id=1")

# fetch multiple data
cursor.execute("SELECT * FROM Todo WHERE id=1 OR id=2")

# fetch data using LIKE
cursor.execute("SELECT * FROM Todo WHERE task LIKE 'task%'")

# commit the changes
connection.commit()

# close the connection
connection.close()

```

There are other ways to fetch data from a table in `sqlite3` using `python`. But these are the most common ways.

*** How to update data in a table?

```python

import sqlite3

connection = sqlite3.connect('scheduler.db')

cursor = connection.cursor()

# update data
cursor.execute("UPDATE Todo SET task='task1 updated' WHERE id=1")

# commit the changes
connection.commit()

# close the connection
connection.close()

```

This is how we update data in a table in `sqlite3` using `python`.

*** How to delete data from a table?

```python

import sqlite3

connection = sqlite3.connect('scheduler.db')

cursor = connection.cursor()

# delete data
cursor.execute("DELETE FROM Todo WHERE id=1")

# commit the changes
connection.commit()

# close the connection
connection.close()

```

This is how we delete data from a table in `sqlite3` using `python`.

*** how to delete a table?

```python

import sqlite3

connection = sqlite3.connect('scheduler.db')

cursor = connection.cursor()

# delete a table
cursor.execute("DROP TABLE Todo")

# commit the changes
connection.commit()

# close the connection
connection.close()

```

This is how we delete a table in `sqlite3` using `python`.

Now, that we know how to interact with the database, let's build the command line application.

# SCHEUDLER 

## Building the Database

I've said earlier that I will be using `OOP(object oriented programming)` approach for this project. So, I will be creating a class for the database.

```python

import sqlite3

class Database:
    def __init__(self,):
        self.conn = sqlite3.connect('scheduler.db') # connect to the database
        self.cur = self.conn.cursor() # create a cursor

```

I just simple created a class called `Database` and Inside the constructor I created a connection to the database and a cursor.

Now, we create a method to create a table.

```python

import sqlite3

class Database:
    def __init__(self,):
        self.conn = sqlite3.connect('scheduler.db') # connect to the database
        self.cur = self.conn.cursor() # create a cursor
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Todo (
            task TEXT
        )""") # create a table named Todo if it doesn't exist

```

> We don't really need an `id` column for this project. So, I didn't create one.

I just created a method called `create_table` and inside the method I created a table named `Todo` if it doesn't exist. Now we can create the other two tables.

```python

import sqlite3

class Database:
    def __init__(self,):
        self.conn = sqlite3.connect('scheduler.db') # connect to the database
        self.cur = self.conn.cursor() # create a cursor

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Todo (
            task TEXT,
        )""") # create a table named Todo if it doesn't exist

        self.cur.execute("""CREATE TABLE IF NOT EXISTS inProgress (
            task TEXT,
        )""") # create a table named inProgress if it doesn't exist

        self.cur.execute("""CREATE TABLE IF NOT EXISTS Completed (
            task TEXT,
        )""") # create a table named completed if it doesn't exist

```

Now, we have 3 tables in our database. Now, we need to create a method to insert data into the table.

```python

import sqlite3

class Database:
    def __init__(self,):
        .....

    def insert(self, table, task):
        self.cur.execute(f"INSERT INTO {table} VALUES (?)", (task,)) # insert data into the table
        self.conn.commit() # commit the changes

```

I created a method called `insert` and inside the method I used `f-string` to insert data into the table. This table will take two arguments, `table` and `task`. The `table` argument will take the name of the table and the `task` argument will take the task that we want to insert into the table. And then I committed the changes.

Now, we need to create a method to fetch data from the table.

```python

import sqlite3

class Database:
    def __init__(self,):
        .....

    def insert(self, table, task):
        .....

    def fetch(self, table):
        self.cur.execute(f"SELECT * FROM {table}") # fetch all the data from the table
        data = self.cur.fetchall() # fetch all the data
        return data # return the data

```

I created a method called `fetch` and inside the method I used `f-string` to fetch data from the table. This method will take one argument, `table`. The `table` argument will take the name of the table that we want to fetch data from. And then I returned the data.

Now, we need to create a method to update data in the table.

```python

import sqlite3

class Database:
    def __init__(self,):
        .....

    def insert(self, table, task):
        .....

    def fetch(self, table):
        .....

    def update(self, table, task, new_task):
        self.cur.execute(f"UPDATE {table} SET task=? WHERE task=?", (new_task, task)) # update data in the table
        self.conn.commit() # commit the changes

```

SO, the update method will take 3 arguments, `table`, `task` and `new_task`. The `table` argument will take the name of the table that we want to update data in. The `task` argument will take the task that we want to update. 

And the `new_task` argument will take the new task that we want to update the old task with. And then I committed the changes.

Now, we need to create a method to delete data from the table.

```python

import sqlite3

class Database:
    def __init__(self,):
        .....

    def insert(self, table, task):
        .....

    def fetch(self, table):
        .....

    def update(self, table, task, new_task):
        .....

    def delete(self, table, task):
        self.cur.execute(f"DELETE FROM {table} WHERE task=(?)", (task,)) # delete data from the table
        self.conn.commit() # commit the changes
```

SO, the delete method will take 2 arguments, `table` and `task`. The `table` argument will take the name of the table that we want to delete data from. The `task` argument will take the task that we want to delete. And then I committed the changes.

Now for good practice, we need to create a method to close the connection and another method to just delete all the table so that we can start fresh.

```python

import sqlite3

class Database:
    def __init__(self,):
        .....

    def insert(self, table, task):
        .....

    def fetch(self, table):
        .....

    def update(self, table, task, new_task):
        .....

    def delete(self, table, task):
        .....

    def close(self,):
        self.conn.close() # close the connection

    def delete_all(self, table = None):
        if table:
            self.cur.execute(f"DELETE FROM {table}") # delete all the data from the table

        else:
            self.cur.execute("DROP TABLE Todo") # delete the Todo table
            self.cur.execute("DROP TABLE inProgress") # delete the inProgress table
            self.cur.execute("DROP TABLE Completed") # delete the completed table

        self.conn.commit() # commit the changes
```

I created a method called `close` and inside the method I closed the connection.

And I created a method called `delete_all` and inside the method I used `if statement` to check if the `table` argument is passed or not. 

This will give the user the option to delete all the data from a specific table or delete all the tables.

Now, we have a class called `Database` and it has all the methods that we need to interact with the database. Now, we need to create a class for the `application`.

## Building the Application

Before starting to keep your code clean, you can make a file for the `database` and a file for the `application`. I'll name my `database` file `database.py` and I'll name my `application` file `app.py`.

> database.py will contain the `class Database` and app.py will contain the `class Application`.

Now, let's make the `application` class.

```python

# TO use the Database class, we need to import it
from database import Database
import sqlite3 # we also need to import sqlite3


class Application:
    def __init__(self,):
        self.db = Database() # create an instance of the Database class which will create a connection to the database and create the tables if they don't exist.

```

I created a class called `Application` and inside the constructor I created an instance of the `Database` class. This will create a connection to the database and create the tables if they don't exist.

Now, let's see what scenarios we might face while using the application.

- Add a task to the `Todo` list.
- Remove a task from the `Todo` list.
- Edit a task from the `Todo` list.
- Add a task to the `in progress` list from the `Todo` list. and if the `in progress` list is empty, then the application will automatically add a task from the `Todo` list to the `in progress` list.
- Remove a task from the `in progress` list which will then be added back to the `Todo` list.
- Add a task to the `completed` list from the `in progress` list.
- See all the tasks in the `Todo`, `in progress` and `completed` list.
- Delete all the tasks from the `Todo`, `in progress` and `completed` list.

I'll add all these scenarios as methods in the `Application` class one by one.

before that, let's create a method to show all the tasks in the `Todo`, `in progress` and `completed` list.

```python

..... # same as before
from itertools import zip_longest # we need to import zip_longest to handle the index error

class Application:
    def __init__(self,):
        .....

    def show_all_tasks(self,):
        todos = self.db.fetch('Todo')

        # fetch all the tasks from the inProgress table
        in_progress = self.db.fetch('inProgress')

        # fetch all the tasks from the Completed table
        completed = self.db.fetch('Completed')

        # print all the tasks
        print(f"|{'TODOs':^20}|{'in progress':^20}|{'completed':^20}|")
        print(f"|{'-'*20}|{'-'*20}|{'-'*20}|")
        for todo, inp, comp in zip_longest(todos, in_progress, completed, fillvalue=" "):
            print(f"|{todo[0]:^20}|{inp[0]:^20}|{comp[0]:^20}|")

        print(f"|{'-'*20}|{'-'*20}|{'-'*20}|")

```

Lot of codes right? But maybe it's the easiest `python` code I have ever written. Just fetch all the tasks from the `Todo`, `in progress` and `completed` list and loop through the lists and print the tasks.

When we are printing the whole list at once, we might get an `IndexError` because the length of the lists are not the same. So, we need to handle that By using `zip_longest` from `itertools`.

This will give us a `list` of tuple where each tuple will contain the tasks from the `Todo`, `in progress` and `completed` list. And if the length of the lists are not the same, then the `fillvalue` will be used to fill the empty space.

> Now, let's create a method to add a task to the `Todo` list.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    def show_all_tasks(self,):
        .....

    def add_task(self, task):
        self.db.insert('Todo', task) # insert the task into the Todo table
        print(f"Task '{task}' added to the Todo list") # print a message

```

So, I only `inserted` the task into the `Todo` table because we only want to add a task to the `Todo` list. Then we printed a message.

> Now let's create a method to remove a task from the `Todo` or `in progress` list.

But before that we need a way to select a task from the `Todo` or `in progress` list for the user to remove. So, we will show the user all the tasks in the `Todo` or `in progress` list and then ask the user to select a table. And then we will ask the user to select a task from the table. And then we will remove the task from the table.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    def show_all_tasks(self,):
        .....

    def add_task(self, task):
        .....

    def removable_tasks(self):
        # fetch all the tasks from the Todo table
        todos = self.db.fetch('Todo')

        # fetch all the tasks from the inProgress table
        in_progress = self.db.fetch('inProgress')

        # print all the tasks
        print(f"|{'index':^5}|{'TODOs':^20}|{'in progress':^20}|")
        print(f"|{'-'*5}|{'-'*20}|{'-'*20}|")

        for i in range(max(len(todos), len(in_progress))):
            # we will use try and except to handle the index error because the length of the lists are not the same
            try:
                print(f"|{i:^5}|{todos[i][0]:^20}|{in_progress[i][0]:^20}|")
            except IndexError:
                # find the list with the most length
                # if todos list has the most length print the todos list and leave the other two empty
                if len(todos) > len(in_progress):
                    print(f"|{i:^5}|{todos[i][0]:^20}|{'':^20}|")
                # if in_progress list has the most length print the in_progress list and leave the other two empty
                elif len(in_progress) > len(todos):
                    print(f"|{i:^5}|{'':^20}|{in_progress[i][0]:^20}|")

        print(f"|{'-'*5}|{'-'*20}|{'-'*20}|")

        return (todos, in_progress)

        def remove_task(self,):
            todos, in_progress = self.removable_tasks() # show all the tasks in the Todo or inProgress list
            table = int(input("1 for Todo, 2 for inProgress, 0 to Cancel: ")) # ask the user to select a table
            index = int(input("Enter the index of the task you want to remove: ")) # ask the user to select a task
            if table == 1:
                self.db.delete('Todo', todos[index][0]) # delete the task from the Todo table
                print(f"Task '{todos[index][0]}' removed from the Todo list") # print a message
            elif table == 2:
                self.db.delete('inProgress', in_progress[index][0]) # delete the task from the inProgress table
                print(f"Task '{in_progress[index][0]}' removed from the inProgress list") # print a message

            else:
                print("Canceled")  # print a message
```

This is a bit tricky. I implemented the `removable_tasks` method to show all the tasks in the `Todo` or `in progress` list just like we did in the `show_all_tasks` method, Now, whenever user wants to remove a task, we will call the `removable_tasks` method and show all the tasks in the `Todo` or `in progress` list. And then we will ask the user to select a table. And then we will ask the user to select a task from the table. And then we will remove the task from the table.

To avoid messing up the code, I created a method called `remove_task` and inside the method I called the `removable_tasks` method and showed all the tasks in the `Todo` or `in progress` list. And then the `removal` will take place.

> Now, let's create a method to edit a task from the `Todo` list.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    def show_all_tasks(self,):
        .....

    def add_task(self, task):
        .....

    def removable_tasks(self):
        .....

    def remove_task(self, table):
        .....

    def edit_task(self,):
        todos = self.db.fetch('Todo') # fetch all the tasks from the Todo table

        # print all the tasks
        print(f"|{'index':^5}|{'TODOs':^20}|")

        for i in range(len(todos)):
            print(f"|{i:^5}|{todos[i][0]:^20}|")

        print(f"|{'-'*5}|{'-'*20}|")

        index = int(input("Enter the index of the task you want to edit: ")) # ask the user to select a task

        new_task = input("Enter the edited task: ") # ask the user to enter the edited task

        self.db.update('Todo', todos[index][0], new_task) # update the task in the Todo table
        print(f"Task '{todos[index][0]}' updated to '{new_task}'") # print a message

```

Pretty straight forward I think. We would give user the ability to edit a task from the `Todo` list only because once the task is moved to the `in progress` list, we can't edit it. So, we will show all the tasks in the `Todo` list and then ask the user to select a task. And then ask the user to enter the edited task. And then we will update the task in the `Todo` table.

> Now, let's create a method to add a task to the `in progress` list from the `Todo` list.

Now, how do we add a task to the `in progress` list from the `Todo` list? I don't mean how do we add it in the database but how do we add it in the `application`? Which logic do we follow.

SO, we need to think about how we suppose to use the application if the `in progress` list is empty. We would want to add a task to the `in progress` list from the `Todo` list. if the `todo` list is empty, then we would want to add a task to the `todo` list. 

There can be another scenario, what if a `task` is completed and the `in progress` list is empty. Then we would want to add the first task from the `Todo` list to the `in progress` list.

> I want this app to work as a queue. That's why the first task from the `Todo` list will be added to the `in progress` list.

SO, let's first create a method to show the user which task can be added to the `in progress` list.

Oh, wait we have already created a method to show all the tasks in the `Todo` and `in progress` list, we named it `removable_tasks`. We can use that method to show the user which task can be added to the `in progress` list. Which will return the `Todo` and `in progress` list.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    def show_all_tasks(self,):
        .....

    def add_task(self, task):
        .....

    def removable_tasks(self):
        .....

    def remove_task(self, table):
        .....

    def edit_task(self,):
        .....

    def add_to_in_progress(self,):
        todos, in_progress = self.removable_tasks() # show all the tasks in the Todo or inProgress list
        if len(in_progress) == 0: # if the inProgress list is empty
            if len(todos) == 0: # if the Todo list is empty
                print("No tasks to add to the inProgress list") # print a message
                print("Do you want to add a task to the Todo list?") # ask the user if they want to add a task to the Todo list
                choice = input("y/n(this task will be added to the inProgress list): ") # ask the user to select an option
                if choice == 'y':
                    task = input("Enter the task: ") # ask the user to enter a task
                    self.add_task(task) # add the task to the Todo list
                    self.add_to_in_progress() # call the add_to_in_progress method again
                else:
                    print("Canceled") # print a message

            else:
                self.db.insert('inProgress', todos[0][0]) # insert the first task from the Todo list to the inProgress list
                self.db.delete('Todo', todos[0][0]) # delete the task from the Todo list
                print(f"Task '{todos[0][0]}' added to the inProgress list") # print a message

        else:
            if len(todos) == 0: # if the Todo list is empty
                print("No tasks to add to the inProgress list") # print a message
                print("Do you want to add a task to the Todo list?") # ask the user if they want to add a task to the Todo list
                choice = input("y/n(this task will be added to the inProgress list): ") # ask the user to select an option
                if choice == 'y':
                    task = input("Enter the task: ") # ask the user to enter a task
                    self.add_task(task) # add the task to the Todo list
                    self.add_to_in_progress() # call the add_to_in_progress method again
                else:
                    print("Canceled") # print a message

            else:
                print(f"Task '{todos[0][0]}' can be added to the inProgress list") # print a message
                print("Do you want to add it?") # ask the user if they want to add the task to the inProgress list
                choice = input("y/n: ") # ask the user to select an option
                if choice == 'y':
                    self.db.insert('inProgress', todos[0][0]) # insert the first task from the Todo list to the inProgress list
                    self.db.delete('Todo', todos[0][0]) # delete the task from the Todo list
                    print(f"Task '{todos[0][0]}' added to the inProgress list") # print a message
                else:
                    print("Canceled") # print a message

```

Now that's a lot of code. 

- First we called the `removable_tasks` method and showed all the tasks in the `Todo` and `in progress` list.
- Then we checked if the `in progress` list is empty or not. If the `in progress` list is empty, then we checked if the `Todo` list is empty or not. If the `Todo` list is empty, then we asked the user if they want to add a task to the `Todo` list. If the user wants to add a task to the `Todo` list, then we asked the user to enter a task and then we called the `add_task` method and added the task to the `Todo` list. And then we called the `add_to_in_progress` method again. If the user doesn't want to add a task to the `Todo` list, then we printed a message.
- Then same process if the `in progress` list is not empty. We checked if the `Todo` list is empty or not. If the `Todo` list is empty, then we asked the user if they want to add a task to the `Todo` list. If the user wants to add a task to the `Todo` list, then we asked the user to enter a task and then we called the `add_task` method and added the task to the `Todo` list. And then we called the `add_to_in_progress` method again. If the user doesn't want to add a task to the `Todo` list, then we printed a message.

Now this happend because of `repeatition` we checked the same thing and wrote the same code twice. We can avoid this by creating a method to check if the `Todo` list is empty or not and if the `Todo` list is empty, then we will ask the user if they want to add a task to the `Todo` list. And then we will ask the user to enter a task and then we will call the `add_task` method and added the task to the `Todo` list. And then we will call the `add_to_in_progress` method again. If the user doesn't want to add a task to the `Todo` list, then we will print a message.

So, I'll make a new `method` just to chech do the above mentioned things. Then edit the `add_to_in_progress` method.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    .....


    def empty_todo(self):
        print("do you want to add a task to the Todo list?") # ask the user if they want to add a task to the Todo list
        choice = input("y/n: ") # ask the user to select an option
        if choice == 'y':
            task = input("Enter the task: ") # ask the user to enter a task
            self.add_task(task) # add the task to the Todo list
            return True
        else:
            print("Canceled") # print a message
            return False


    def add_to_in_progress(self,):
        todos, in_progress = self.removable_tasks() # show all the tasks in the Todo or inProgress list
        if len(in_progress) == 0: # if the inProgress list is empty
            if len(todos) == 0: # if the Todo list is empty
                print("No tasks to add to the inProgress list") # print a message
                added_to_the_todo = self.empty_todo() # call the empty_todo method

                if added_to_the_todo:
                    self.add_to_in_progress() # call the add_to_in_progress method again

            else:
                self.db.insert('inProgress', todos[0][0]) # insert the first task from the Todo list to the inProgress list
                self.db.delete('Todo', todos[0][0]) # delete the task from the Todo list
                print(f"Task '{todos[0][0]}' was directly added to the inProgress list because the in progress list was empty") # print a message

        else:
            if len(todos) == 0: # if the Todo list is empty
                print("No tasks to add to the inProgress list") # print a message
                added_to_the_todo = self.empty_todo() # call the empty_todo method

                if added_to_the_todo:
                    self.add_to_in_progress() # call the add_to_in_progress method again

            else:
                print(f"Task '{todos[0][0]}' can be added to the inProgress list") # print a message
                print("Do you want to add it?") # ask the user if they want to add the task to the inProgress list
                choice = input("y/n: ") # ask the user to select an option
                if choice == 'y':
                    self.db.insert('inProgress', todos[0][0]) # insert the first task from the Todo list to the inProgress list
                    self.db.delete('Todo', todos[0][0]) # delete the task from the Todo list
                    print(f"Task '{todos[0][0]}' added to the inProgress list") # print a message
                else:
                    print("Canceled") # print a message

```

Now, we have a clear and concise code. And Now we can add the last method.

> Now, let's create a method to add a task to the `completed` list from the `in progress` list.


THis is a mix of all the other methods. We will show all the tasks in the `in progress` list and then ask the user to select a task. And then we will remove the task from the `in progress` list and then add the task to the `completed` list. So, this is like the `remove_task` method and the `add_task` method combined.

and also we need to check if the `in progress` list is empty or not. If the `in progress` list is empty, then we will ask the user if they want to add a task to the `in progress` list. If the user wants to add a task to the `in progress` list, then we will ask the user to enter a task and then we will call the `add_task` method and added the task to the `in progress` list. And then we will call the `add_to_completed` method again. If the user doesn't want to add a task to the `in progress` list, then we will print a message.

so, we will make a method which will give a `in progress` list then we will ask the user to select a task and then we will remove the task from the `in progress` list and then add the task to the `completed` list.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    .....

    def show_in_progress(self,):
        in_progress = self.db.fetch('inProgress') # fetch all the tasks from the inProgress table

        # print all the tasks
        print(f"|{'index':^5}|{'in progress':^20}|")
        print(f"|{'-'*5}|{'-'*20}|")

        for i in range(len(in_progress)):
            print(f"|{i:^5}|{in_progress[i][0]:^20}|")

        print(f"|{'-'*5}|{'-'*20}|")

        return in_progress
```

this will show the user all the tasks in the `in progress` list and return the `in progress` list.

Now we can create the `add_to_completed` method, where we will show all the tasks in the `in progress` list and then ask the user to select a task and then remove the task from the `in progress` list and then add the task to the `completed` list and before that we will check if the `in progress` list is empty or not. If the `in progress` list is empty, then we will ask the user if they want to add a task to the `in progress` list. If the user wants to add a task to the `in progress` list, then we will ask the user to enter a task and then we will call the `add_task` method and added the task to the `in progress` list. And then we will call the `add_to_completed` method again. If the user doesn't want to add a task to the `in progress` list, then we will print a message.

which is exactly what we did in the `add_to_in_progress` method. So, we will just copy the code from the `add_to_in_progress` method and make some changes.

Let's do it.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    .....

    def add_to_completed(self,):
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
            print(f"which task do you want to add to the completed list?") # print a message
            in_progress = self.show_in_progress() # show all the tasks in the inProgress list

            index = int(input("Enter the index of the task you want to add to the completed list: ")) # ask the user to select a task

            self.db.insert('Completed', in_progress[index][0]) # insert the task to the completed list

            self.db.delete('inProgress', in_progress[index][0]) # delete the task from the inProgress list

            print(f"Task '{in_progress[index][0]}' added to the completed list") # print a message

```

And we have successfully created all the methods for the `application` class. But there is one more thing left to do. We need to create a method to delete all the tasks from the `Todo`, `in progress` and `completed` list and also a method to close the connection when we are done using the application.

We will create a method called `reset` to delete all the tasks from the `Todo`, `in progress` and `completed` list and also a method called `end` to close the connection when we are done using the application.

```python

..... # same as before

class Application:
    def __init__(self,):
        .....

    .....

    def reset(self,):
        self.db.delete_all() # delete all the tasks from the Todo, inProgress and Completed table
        print("All the tasks deleted") # print a message

    def end(self,):
        self.db.close() # close the connection
        print("GOODBYE") # print a message

```

And that's it for the `application` class.

I think we have all the things we need to build the `command line application`.

## Building the Command Line Application

Now, we will create a file called `main.py` and import the `Application` class from the `app.py` file.

```python

from app import Application

```

Now, we will create an instance of the `Application` class.

```python

from app import Application

app = Application()

```

Now, we will create a `while loop` to run the application.

```python

from app import Application

app = Application()

print("Hello, Welcome to the scheduler app") # print a message
print("This is your whole schedule") # print a message
app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list

while True:
    
    print("What do you want to do?") # print a message
    print("0 to see all the tasks") # print a message
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
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list
        case 1:
            task = input("Enter the task: ") # ask the user to enter a task
            app.add_task(task) # add the task to the Todo list
            print("here's the whole schedule") # print a message
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list


        case 2:
            app.remove_task() # remove a task from the Todo or inProgress list
            print("here's the whole schedule") # print a message
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list

        case 3:
            app.edit_task() # edit a task from the Todo list
            print("here's the whole schedule") # print a message
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list

        case 4:
            app.add_to_in_progress() # add a task to the inProgress list
            print("here's the whole schedule") # print a message
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list


        case 5:
            app.add_to_completed() # add a task to the completed list
            print("here's the whole schedule") # print a message
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list
            

        case 6:
            app.reset() # delete all the tasks from the Todo, inProgress and Completed list
            print("here's the whole schedule") # print a message
            app.show_all_tasks() # show all the tasks in the Todo, inProgress and Completed list

        case 7:
            app.end() # close the connection
            break

        case _:
            print("Invalid choice") # print a message

```

And that's it. We have successfully created a `command line application` using `python` and `sqlite3`.

What happend there. Nothing much really because we have already created all the methods for the `application` class. We just called the methods according to the user's choice.

SO, we took the user's choice and matched it with the cases and called the methods according to the user's choice.

And that's it. We have successfully created a `command line application` using `python` and `sqlite3`.

# Conclusion

SO, how was it guys? I hope you guys liked it. I know it's a bit long but I tried to explain everything as much as I can. I hope you guys learned something new from this tutorial. If you guys have any questions or suggestions, then please let me know in the comment section down below.


            