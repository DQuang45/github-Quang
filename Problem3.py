class Student:
    def __init__(self, name, major, ID):
        self.name = name
        self.major = major
        self.ID = ID

class FullTimeStudent(Student):
    def __init__(self, name, major, ID, project):
        super().__init__(name, major, ID)
        self.project = project

class PartTimeStudent(Student):
    def __init__(self, name, major, ID, max_hours, min_hours):
        super().__init__(name, major, ID)
        self.max_hours = max_hours
        self.min_hours = min_hours

class Lecturer:
    def __init__(self, name, ID, rank, project):
        self.name = name
        self.ID = ID
        self.rank = rank
        self.project = project

class Project:
    def __init__(self, name, budget, leader, members):
        self.name = name
        self.budget = budget
        self.leader = leader
        self.members = members
