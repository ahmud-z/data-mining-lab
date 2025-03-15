class Student:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName
        self.studentClass = None

    def display(self):
        for key in self.__dict__:
            print(f"{key} = {self.__dict__[key]}")

def main():
    s1 = Student(213002200, "Ahmud")
    s1.studentClass = "Bsc"

    print("\nBefore delete studentClass:")
    s1.display()

    del s1.studentClass
    print("\nAfter delete studentClass:")
    s1.display()

main()