import pandas as pd


class StudentGroupBlacklistClass:

    def __init__(self, data):
        self.idStudentGroup = data.idStudentGroup
        self.idDay = data.idDay
        self.idTimeSlot = data.idTimeSlot


student_group_blacklist = StudentGroupBlacklistClass(
    pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="StudentGroup_Blacklist"))
