class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, id, scores):
        super().__init__(first_name, last_name, id)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average_marks = sum(self.scores) / len(self.scores)
        if 90 <= average_marks <= 100:
            return 'O'
        elif 80 <= average_marks <= 90:
            return 'E'
        elif 70 <= average_marks <= 80:
            return 'A'
        elif 55 <= average_marks <= 70:
            return 'P'
        elif 40 <= average_marks <= 55:
            return 'D'
        elif average_marks < 40:
            return 'T'
