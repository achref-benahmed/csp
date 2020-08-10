import pandas as pd

class ClassroomClass:

    def __init__(self, data):
        self.idClassroom = data.idClassroom
        self.name = data.Name
        self.Capacity = data.Capacity


classroom = ClassroomClass(pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Classroom"))
