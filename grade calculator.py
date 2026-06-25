class Student:
    count = 0

    def __init__(self, roll_no, marks, grade):
        self.__roll_no = roll_no
        self.__marks = marks
        self._grade = grade
        Student.count += 1
    def gpa(self):
        return sum(self.__marks) / (len(self.__marks) * 10)
    def gpa(self, marks):
        for m in marks:
            if m < 0 or m > 100:
                print("Invalid marks!")
                return
        self.__marks = marks
    def count_students(cls):
        return cls.count

s1 = Student(1, [80, 90, 70], 'A')
s2 = Student(2, [60, 50, 40], 'B')
print(s1.gpa)
print(Student.count_students())