import pandas as pd


class StudentGroupClass:

    def __init__(self, data):
        self.idStudentGroup = data.idStudentGroup


student_group = StudentGroupClass(pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="StudentGroup"))
