class Student:
    pass

class Mark:
    pass

def main():
    s1 = Student()
    m1 = Mark()

    print(isinstance(s1, Student))
    print(isinstance(s1, Mark))
    print(isinstance(m1, Mark))
    print(issubclass(Student, object))

main()