class Student:
    def __init__(self, studentName, marks):
        self.studentName = studentName
        self.marks = marks

def main():
    s1 = Student("Ahmud", 90)

    print("\nOriginal Data")
    print(f"Student Name: {s1.studentName}")
    print(f"Marks: {s1.marks}")

    s1.studentName = "Bob"
    s1.marks = 33

    print("\nModified Data")
    print(f"Student Name: {s1.studentName}")
    print(f"Marks: {s1.marks}")

main()