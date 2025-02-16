class Student:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

    def display(self):
        for key in self.__dict__:
            print(f"{key} = {self.__dict__[key]}")

def main():

    print("\nBefore added studentClass: ")
    s1 = Student(213002200, "Ahmud")
    s1.display()

    print("\nAfter added studentClass: ")
    s1.studentClass = "Bsc"
    s1.display()

main()