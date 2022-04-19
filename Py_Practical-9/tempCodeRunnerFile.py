#20CE133 - Prachi Shah

#Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

class Student:
    def __init__(self, rollNumber, name):
        self.rollNumber = rollNumber
        self.name = name
    
    def display(self):
        print(f'Student Roll No: {self.rollNumber}')
        print(f'Student Name: {self.name}')

class Exam(Student):
    def __init__(self, rollNumber, name, subject):
        super().__init__(rollNumber, name)
        self.subject = subject
    
    def display(self):
        super().display()
        for i in range(len(self.subject)):
            print(f'Subject {i+1} Marks: {self.subject[i]}')

class Result(Exam):
    total_marks = 0
    def __init__(self, rollNumber, name, subject):
        super().__init__(rollNumber, name, subject)
        self.total_marks = sum(subject)
    
    def display(self):
        super().display()
        print(f'Total Marks: {self.total_marks}')


if __name__ == '__main__':
    student = Student(1, 'Prachi')
    student.display()
    print()

    exam = Exam(2, 'Hit', [10, 20, 30])
    exam.display()
    print()

    result = Result(3, 'Ish', [40, 50, 60])
    result.display()
    print()