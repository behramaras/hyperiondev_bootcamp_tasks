# datetime module is added for easy time-related operations.

from datetime import datetime

# If user selects 'r' from the menu, reg_user() function will be executed.
# However, only the admin can add a new user by selecting 'r' from the menu.
# New users are written to the users.txt file. And user_file is closed.


def reg_user():
    while username == "admin":
        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        pass_confirm = input("Re-enter the password: ")

        if new_password != pass_confirm:
            print("Given passwords are not matching.")

        if new_username in username_list:
            print("The username already exists. Please, try a different username.")
            continue

        if new_username not in username_list and new_password == pass_confirm:
            user_file.write(f"\n{new_username}, {new_password}")
            print("Username added.")
            user_file.close()
            break
    else:
        print("You don't have the permission to register a user!")


# If user selects 'a' from the menu, add_task() function will be executed.
# Users can assign a new task if they choose 'a' from the menu.
# These tasks are written to the tasks.txt file opened with the name second_tasks_file.
# Today's date is added by default with datetime module as current date.
# Then the file is closed.


def add_task():
    whom_username = input("Enter a username of the person whom the task is assigned to: ")
    title = input("Enter a title of a task: ")
    description = input("Enter a description of the task: ")
    due_date = input("Enter a due date of the task(i.e 01 Jan 2020): ")
    current_date = datetime.now().strftime('%d %b %Y')
    print(f"Current date: {current_date}")
    completed = "No\n"

    second_tasks_file = open("tasks.txt", "a+")
    second_tasks_file.write(
        f"{whom_username}, {title.capitalize()}, {description.capitalize()}, {due_date}, {current_date}, "
        f"{completed}")
    second_tasks_file.close()


# If user chooses 'va' from the menu, view_all() function will be executed.
# All tasks in the tasks.txt file will be written to the screen.


def view_all():
    for line in first_tasks_file:
        whom_username, title, description, current_date, due_date, completed = line.strip("\n").split(", ")
        print(
            f"\nTask: {title}\nAssigned to: {whom_username}\nDate assigned: "
            f"{current_date}\nDue date: {due_date}\nTask Complete:{completed}\nTask description:\n"
            f"{description}\n**************************")


# If user selects 'vm' from the menu, view_mine() function will be executed.
# The user can choose to see the all tasks which are assigned to them or a specific task.
# If the user chooses a specific task, user can mark the task as complete or edit the task if the task is not completed.


def view_mine():
    if username in [i.rstrip().split(', ')[0] for i in first_tasks_file]:

        select = input("Do you want to display all tasks or a specific task?('all or s'): ")

        if select.lower() == "all":
            first_tasks_file.seek(0)

            for line in first_tasks_file:
                whom_username, title, description, current_date, due_date, completed = line.strip("\n").split(
                    ", ")

                if whom_username == username:
                    print(
                        f"\nTask: {title}\nAssigned to: {whom_username}\nDate assigned: "
                        f"{current_date}\nDue date: {due_date}\nTask Complete:{completed}\nTask "
                        f"description:\n{description}\n**************************")

        elif select.lower() == "s":

            while True:
                num_task = int(input("Enter the task number or -1 to quit: "))
                all_value = []
                if num_task == -1:
                    break

                else:
                    first_tasks_file.seek(0)
                    contents = first_tasks_file.readlines()
                    for value, task in enumerate(contents):
                        all_value.append(value)

                        if num_task == value:
                            whom_username, title, description, current_date, due_date, completed = task.strip(
                                "\n").split(", ")

                            print(f"\n**************************"
                                  f"\nTask: {title}\nAssigned to: {whom_username}\n"
                                  f"Date assigned: {current_date}\nDue date: {due_date}\nTask Complete:{completed}\n"
                                  f"Task description:\n{description}\n**************************")

                    if num_task not in all_value:
                        print("There is no task for this value!")
                        continue

                    choose = input("Do you want to mark the task as complete or edit the task?('m/e'): ").lower()
                    split_data = contents[num_task].split(", ")

                    if choose == "m":
                        file = open("tasks.txt", "r+")

                        if split_data[-1] == "Yes\n":
                            print("The task already completed. You can't edit.")

                        else:
                            split_data[-1] = "Yes\n"
                            join_data = ", ".join(split_data)
                            contents[num_task] = join_data

                            for line in contents:
                                file.write(line)

                            file.close()
                            print("Marked the task as complete.")

                    elif choose == "e":
                        file = open("tasks.txt", "r+")

                        if split_data[-1] == "Yes\n":
                            print("The task already completed. You can't edit.")

                        else:
                            action = input("Do you want to change the assigned username or the due date?(u/d): ")

                            if action.lower() == "u":
                                new_name = input("Enter the new username: ")

                                split_data[0] = new_name
                                join_data = ", ".join(split_data)
                                contents[num_task] = join_data

                                for line in contents:
                                    file.write(line)

                                file.close()
                                print("The username is changed.")

                            elif action.lower() == "d":
                                new_date = input("Enter the new due date: ")

                                split_data[3] = new_date
                                join_data = ", ".join(split_data)
                                contents[num_task] = join_data

                                for line in contents:
                                    file.write(line)

                                file.close()
                                print("The username is changed.")

                            else:
                                print("Invalid login!")
                    else:
                        print("Invalid selection!")

        else:
            print("Invalid selection!")

    else:
        print(f"There is no Task for this user!")


# If user selects 'gr' from the menu, generate_reports() function will be executed.
# user.txt and tasks.txt are read and datas are taken from these files.
# Datas which are taken from files are written to user_overview.txt and task_overview.txt.


def generate_reports():

    user_file = open("user.txt", "r")
    task_file = open("tasks.txt", "r")
    user_overview = open("user_overview.txt", "w+")
    task_overview = open("task_overview.txt", "w+")

    user_tasks = 0
    user_overdue_counter = 0
    user_completed_counter = 0

    task_date_counter = 0
    task_overdue_counter = 0
    task_completed_counter = 0
    task_uncompeleted_counter = 0

    num_all = len(task_file.readlines())
    task_file.seek(0)

    for line in task_file:
        split_data = line.split(", ")
        user = split_data[0]
        date = split_data[3]
        complete = split_data[-1]

        if complete == "Yes\n":
            task_completed_counter += 1
        else:
            task_uncompeleted_counter += 1

        if datetime.strptime(date, '%d %b %Y') < datetime.now():
            task_overdue_counter += 1
        else:
            task_date_counter += 1

        if user == username:
            user_tasks += 1

        if (user == username) and (complete == "Yes\n"):
            user_completed_counter += 1

        if (user == username) and (datetime.strptime(date, '%d %b %Y') < datetime.now()):
            user_overdue_counter += 1

    task_overview.write(
        f"The total number of tasks: {len(first_tasks_file.readlines())}\n"
        f"\nThe total number of completed tasks: {task_completed_counter}\n"
        f"\nThe total number of uncompleted tasks: {task_uncompeleted_counter}\n"
        f"\nThe total number of tasks that haven’t been completed and that are overdue: "
        f"{task_overdue_counter}\n"
        f"\nThe percentage of tasks that are incomplete: "
        f"%{(100 * task_uncompeleted_counter / (task_completed_counter + task_uncompeleted_counter))}\n"
        f"\nThe percentage of tasks that are overdue: "
        f"%{100 * task_overdue_counter / (task_overdue_counter + task_date_counter)}\n"
    )
    if user_tasks == 0:
        user_overview.write(
            f"The total number of users: {len(user_file.readlines())}\n"
            f"\nThe total number of tasks: {num_all}\n"
            f"\nThe total number of tasks assigned to you: 0\n"
            f"\nThe percentage of the total number of tasks that have been assigned to you: "
            f"%{(100 * user_tasks) / num_all}\n"
            f"\nThe percentage of the tasks assigned to you that have been completed: "
            f"%0\n"
            f"\nThe percentage of the tasks assigned to you that still be completed: "
            f"%0\n"
            f"\nThe percentage of the tasks assigned to you that have not yet been completed and "
            f"are overdue: %0\n"
        )

    else:
        user_overview.write(
            f"The total number of users: {len(user_file.readlines())}\n"
            f"\nThe total number of tasks: {num_all}\n"
            f"\nThe total number of tasks assigned to you: {user_tasks}\n"
            f"\nThe percentage of the total number of tasks that have been assigned to you: "
            f"%{(100 * user_tasks) / num_all}\n"
            f"\nThe percentage of the tasks assigned to you that have been completed: "
            f"%{(100 * user_completed_counter) / user_tasks}\n"
            f"\nThe percentage of the tasks assigned to you that still be completed: "
            f"%{(100 * (user_tasks - user_completed_counter)) / user_tasks}\n"
            f"\nThe percentage of the tasks assigned to you that have not yet been completed and "
            f"are overdue: %{(100 * user_overdue_counter) / user_tasks}\n"
        )

    print("Users report and tasks report are generated.\n")

    task_overview.close()
    user_overview.close()
    user_file.close()
    task_file.close()


"""
This code reads the user.txt file and stores the usernames and passwords in the file in separate lists.
The code searches the username and password in these lists.
If the username and password are in the list and if they match, it allows the user to login.
Otherwise, it displays a suitable text to the user.

When the user enters the program, they encounter two different menus depending on whether the user is an admin or not.
If the user is admin, unlike the other menu, admin can see statistics with 'ds'.

If users choose 'e' from the menu, the program is closed.

When a selection is made which is not included in the menu, a suitable text is displayed.
"""


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
            first_tasks_file = open("tasks.txt", "r+")

            if username == "admin":
                menu = input(
                    '''Select one of the following options below:
                    r - registering a user
                    a - adding a task
                    va - view all tasks
                    vm - view my task
                    gr - generate reports
                    ds - display statistics
                    e - exit
                    : '''
                ).lower()

            else:
                menu = input(
                    '''\nSelect one of the following options below:
                    r - registering a user
                    a - adding a task
                    va - view all tasks
                    vm - view my task
                    gr - generate reports
                    e - exit
                    : '''
                ).lower()

            if menu == 'r':
                reg_user()

            elif menu == "a":
                add_task()

            elif menu == 'va':
                view_all()

            elif menu == 'vm':
                view_mine()

            elif menu == 'ds':

                if username != "admin":
                    print("You don't have the permission to display the statistics !")

                else:
                    generate_reports()

                    task_file = open("task_overview.txt", "r")
                    user_file = open("user_overview.txt", "r")
                    task_contents = task_file.readlines()
                    user_contents = user_file.readlines()

                    for value, task in enumerate(task_contents):
                        pass
                    task_split_data = task_contents[0].split(", ")

                    for value, task in enumerate(user_contents):
                        pass
                    user_split_data = user_contents[0].split(", ")

                    print(
                        f"Total number of task: {task_split_data[-1]}\nTotal number of the users: "
                        f"{user_split_data[-1]}")

            elif menu == 'gr':
                generate_reports()

            elif menu == 'e':
                first_tasks_file.close()
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")
