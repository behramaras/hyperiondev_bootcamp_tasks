# The code has a class namely Course as a parent class. And has another class namely OOPCourse as a child class.


# The Course class is created. Course class has 2 class variables which are 'name' and 'contact_website'.
# The Course class also has methods namely 'contact_details' and 'head_office'.
# The contact_details method prints the contact website.
# The head_office method prints the location of head office.

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print(f"Please contact us by visiting {self.contact_website}.\n")

    def head_office(self):
        print("The head office location is Cape Town.\n")


# The OOPCourse class is created. OOPCourse class has 2 attributes namely 'description' and 'trainer'.
# The OOPCourse class also has methods namely 'trainer_details' and 'show_course_id'.
# The trainer_details method prints what the course is about and the name of the trainer.
# The show_course_id method prints the ID number of the course.

class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A.Mouse"

    def trainer_details(self):
        print(
            f"The course is about {self.description}.\n\n"
            f"The trainer's name is {self.trainer}.\n"
        )

    def show_course_id(self):
        print("The ID number of the course is #12345.\n")

course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
