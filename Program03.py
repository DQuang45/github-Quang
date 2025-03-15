class GreenwichException(Exception):
    pass

class CourseException(GreenwichException):
    def __init__(self, message="Course limit exceeded. A student can only enroll in up to 3 courses."):
        super().__init__(message)

class MarkException(GreenwichException):
    def __init__(self, message="Invalid mark. Marks should be between 0 and 100."):
        super().__init__(message)

class GreenwichStudent:
    def __init__(self, name):
        self.name = name
        self.marks = {}  # Dictionary to store course code and mark pairs

    def updateCourse(self, code, mark):
        if mark < 0 or mark > 100:
            raise MarkException(f"Invalid mark: {mark}. Marks should be between 0 and 100.")
        
        if code not in self.marks and len(self.marks) >= 3:
            raise CourseException()
        
        self.marks[code] = mark
        print(f"Updated: {code} - {mark}")

# Client code
def main():
    student = GreenwichStudent("John Doe")
    
    try:
        student.updateCourse("CS101", 85)
        student.updateCourse("MA102", 90)
        student.updateCourse("PH103", 75)
        student.updateCourse("CH104", 80)  # This should raise CourseException
    except GreenwichException as e:
        print(f"Exception: {e}")
    
    try:
        student.updateCourse("CS101", -5)  # This should raise MarkException
    except GreenwichException as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
