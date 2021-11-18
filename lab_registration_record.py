# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-22
# author: B. Schoen-Phelan
# date: 18-11-2020
# purpose: An exercise to get familiar with composition


class Student:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    POSTGRADUATE = ("postgraduate")
    UNDERGRADUATE = ("undergraduate")


    def __init__(self, study_type, f_name, l_name):
        # YOUR CODE GOES HERE
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name
        self.course = []

    def set_courses(self, val):
        self.course.append(val)

    def show_courses(self):
        return self.course



    # YOUR CODE GOES HERE



class RegistrationData:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        # YOUR CODE GOES HERE
        self.address = address
        self.registration_fee = registration_fee
        self.study_type = study_type
        self.f_name = f_name
        self.l_name = l_name
        self.s_id = s_id
        self.student_object = Student(self.study_type, self.f_name, self.l_name)

    def display_student_data(self):
        print(self.address)
        print(self.registration_fee)
        print(self.study_type)
        print(self.f_name)
        print(self.l_name)
        print(self.show_s_id())
        print(self.student_object.show_courses())

    def set_s_id(self, val):
        self.s_id = val

    def show_s_id(self):
        return self.s_id



    # YOUR CODE GOES HERE



# using the class
# NOTE: THIS CODE BELOW WILL NOT WORK YET AS __YOU__ NEED TO IMPLEMENT WHAT
# MAKES IT POSSIBLE TO RUN THE BELOW CODE!!!!
r = RegistrationData("8 Grangegorman Road Lower, Dublin 1, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.set_s_id("C12345")
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.set_courses(course)

r.display_student_data()

# print(RegistrationData.__doc__)