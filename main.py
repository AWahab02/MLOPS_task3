class StudentsInMLOPs:
    def __init__(self):
        self.students = []
        self.className = "MLOPS"

    def enrollStudents(self, student:int):
        if student not in self.students:
            self.students.append(student)
            return True
        else:
            return False

    def dropStudents(self, student:int):
        if student in self.students:
            self.students.remove(student)
            return True
        else:
            return False

    def getTotalStudents(self):
        return len(self.students)
    
    def getClassName(self):
        return self.className
    
# test comment