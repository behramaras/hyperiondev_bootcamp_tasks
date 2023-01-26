"""
This code reads the user.txt file and stores the usernames and passwords in the file in separate lists.

The code searches the username and password in these lists.
If the username and password are in the list and if they match, it allows the user to login.
Otherwise, it displays a suitable text to the user.

When the user enters the program, they encounter two different menus depending on whether the user is an admin or not.

If the user is admin, unlike the other menu, admin can see statistics with 's'.
However, only the admin can add a new user by selecting 'r' from the menu. New users are written to the users.txt file.
And user_file is closed.

Users can assign a new task if they choose 'a' from the menu.
These tasks are written to the tasks.txt file opened with the name second_tasks_file.
The file is closed. Today's date is added by default with datetime module as current date.

If users choose 'va' from the menu, all tasks in the tasks.txt file are written to the screen.

If users select 'vm' from the menu, they will only see the tasks assigned to the logged in user.

If users choose 'e' from the menu, first_tasks_file is closed
and the program is closed. The menu continues to be shown to the user until exit is chosen.

When a selection is made which is not included in the menu, a suitable text is displayed.
"""

from datetime import datetime

username_list = []
pass_list = []

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_file = open("user.txt", "r+")

    for line in user_file:
        user, psw = line.strip("\n").split(", ")
        username_list.append(user)
        pass_list.append(psw)

    if username not in username_list or password not in pass_list:
        print("Invalid Username or Password")

    elif (username, password) not in list(zip(username_list, pass_list)):
        print("Username and Password are not matching")

    else:
        while True:
            first_tasks_file = open("tasks.txt", "r")

            if username == "admin":
                menu = input(
                    '''Select one of the following Options below:
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - view my task
                    s - statistics
                    e - Exit
                    : '''
                ).lower()

            else:
                menu = input(
                    '''Select one of the following Options below:
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - view my task
                    e - Exit
                    : '''
                ).lower()

            if menu == 'r':
                if username == "admin":
                    new_username = input("Enter a username: ")
                    new_password = input("Enter a password: ")
                    pass_confirm = input("Re-enter the password: ")

                    if new_password == pass_confirm:
                        user_file.write(f"\n{new_username}, {new_password}")
                        user_file.close()

                    else:
                        print("Given passwords are not matching.")

                else:
                    print("You don't have the permission to register a user!")

            elif menu == "a":
                    whom_username = input("Enter a username of the person whom the task is assigned to: ")
                    title = input("Enter a title of a task: ")
                    description = input("Enter a description of the task: ")
                    due_date = input("Enter a due date of the task: ")
                    current_date = datetime.now().strftime('%d %B %Y')
                    print(f"Current date: {current_date}")
                    complete = "No"

                    second_tasks_file = open("tasks.txt", "a+")

                    second_tasks_file.write(f"\n{whom_username}, {title.capitalize()}, {description.capitalize()}, {due_date}, {current_date}, {complete}")
                    second_tasks_file.close()

            elif menu == 'va':
                for line in first_tasks_file:
                    whom_username, title, description, current_date, due_date, complete = line.strip("\n").split(", ")
                    print(f"Task: {title}\nAssigned to: {whom_username}\nDate assigned: {current_date}\nDue date: {due_date}\nTask Complete:{complete}\nTask description:\n{description}\n**************************")

            elif menu == 'vm':
 
                if username not in [line.rstrip().split(',')[0] for line in first_tasks_file]:
                    print("There is no Task for this user!")

                first_tasks_file.seek(0)
                for line in first_tasks_file:
                    whom_username, title, description, current_date, due_date, complete = line.strip("\n").split(", ")

                    if whom_username == username:
                        print(f"Task: {title}\nAssigned to: {whom_username}\nDate assigned: {current_date}\nDue date: {due_date}\nTask Complete:{complete}\nTask description:\n{description}\n**************************")

            elif menu == 's':
                print(f"Total number of task: {len(first_tasks_file.readlines())}\nTotal number of the users: {len(username_list)}")

            elif menu == 'e':
                first_tasks_file.close()

                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")
