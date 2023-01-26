"""
This code is an email simulation.

The Email class is defined with four variables: 'has_been_read', 'email_contents', 'is_spam' and 'from_address'.

The variables which are 'has_been_read' and 'is_spam' defined default as 'False'.

A function is created in the Email class called mark_as_read which will change has_been_read to true.

Another function is created in the Email class called mark_as_spam which will change is_spam to true.

To operate on the Email objects; add_email, get_count, get_email, get_unread_emails, get_spam_emails,
and delete functions are created.

'enumerate()' built-in function is used to enumerate the emails.

'time' module is added to make the program more realistic.

OOP is used in every step in the code which requires selection.

"""

import time


class Email:
    def __init__(self, email_contents, from_address):
        self.email_contents = email_contents
        self.from_address = from_address
        self.is_spam = False
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

    def __str__(self):
        return f"Mail's content: {self.email_contents}\n"


# A list namely 'inbox' is created to store the mails.

inbox = []


# This function adds a mail to the inbox with content.

def add_email(contents, e_mail):
    new_mail = Email(contents, e_mail)
    inbox.append(new_mail)


# This function counts the number of all mails in the inbox.

def get_count():
    return len(inbox)


# This function takes a number and shows the mail on that number.

def get_email(num):
    for number, e_mail in enumerate(inbox, 1):
        if num == number:
            e_mail.mark_as_read()
            print(f"Mail: {num}\tContents: {e_mail.email_contents}\n")


# This function stores all unread mails as a tuple in a list, namely 'unread', and shows the unread list.

def get_unread_emails():
    unread = []
    for mails in inbox:
        if not mails.has_been_read:
            unread.append((mails.email_contents, mails.from_address))

    print(f"Unread mails: {unread}")


# This function stores all spam mails as a tuple in a list, namely 'spams', and shows the spams list.

def get_spam_emails():
    spams = []
    for mails in inbox:
        if mails.is_spam:
            spams.append((mails.email_contents, mails.from_address))

    print(f"Spam mails: {spams}")


# This function takes the mail number as an input and if the user is sure, it deletes that mail.

def delete():
    for number, e_mail in enumerate(inbox, 1):
        print(f"Mail: {number}\t{e_mail}")
        time.sleep(1)

    while True:

        try:
            which_mail = int(input("Enter the mail's number which you want to delete: "))
            if 0 < which_mail <= len(inbox):

                ask = input("Are you sure?(Y/N): ")

                if ask == "Y":
                    mails = inbox[which_mail - 1]
                    inbox.remove(mails)
                    print("Mail was deleted!")
                    break

                elif ask == "N":
                    print("Operation was reversed!")
                    break

                else:
                    print("Invalid option!")
            else:
                print("Invalid index!\n")

        except ValueError:
            print("Please enter a number!\n")


# This program takes a number as an option and performs the operation according to the entered number.

while True:

    time.sleep(1)
    user_choice = input("""\nWhat would you like to do\n
1- to read an e-mail
2- to mark as a spam an e-email
3- to send an e-email
4- to add an e-mail
5- to learn the number of in the inbox
6- to see unread e-mails
7- to see spam e-mails
8- to delete an e-mail
9- quit

Enter your choice: """)

    if user_choice == "1":

        if len(inbox) == 0:
            print("Inbox is empty. Add an e-mail.\n")

        else:
            for index, mail in enumerate(inbox, 1):
                print(f"Mail: {index}")
                time.sleep(1)

            while True:
                try:
                    which = int(input("Enter the mail's index: "))

                    if 0 < which <= len(inbox):
                        get_email(which)
                        break

                    else:
                        print("Invalid index!\n")

                except ValueError:
                    print("Please enter a number!\n")

    elif user_choice == "2":

        if len(inbox) == 0:
            print("Inbox is empty. Add an e-mail.\n")

        else:

            for index, mail in enumerate(inbox, 1):
                print(f"Mail: {index}\n{mail}")
                time.sleep(1)

            while True:
                try:
                    which = int(input("Enter the mail's index: "))

                    if 0 < which <= len(inbox):
                        email = inbox[which - 1]

                        if email.is_spam:
                            print("This mail already marked as a spam.\n")
                            break

                        else:
                            email.mark_as_spam()
                            print("The mail was marked as a spam.\n")
                            break

                    else:
                        print("Invalid index!\n")

                except ValueError:
                    print("Please enter a number!\n")

    elif user_choice == "3":
        from_address_ = input("Enter your email address: ")
        email_contents_ = input("Enter email content: ")
        add_email(email_contents_, from_address_)
        print("Email sent successfully!")

    elif user_choice == "4":
        email = input("Enter an e-mail: ")
        content = input("Enter the mail's content: ")
        add_email(content, email)
        print("The mail is added.\n")

    elif user_choice == "5":
        print(f"The number of the mails: {get_count()}")

    elif user_choice == "6":
        if len(inbox) == 0:
            print("Inbox is empty. Add an e-mail.\n")

        else:
            get_unread_emails()

    elif user_choice == "7":
        if len(inbox) == 0:
            print("Inbox is empty. Add an e-mail.\n")

        else:
            get_spam_emails()

    elif user_choice == "8":
        if len(inbox) == 0:
            print("Inbox is empty. Add an e-mail.\n")

        else:
            delete()

    elif user_choice == "9":
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input\n")
