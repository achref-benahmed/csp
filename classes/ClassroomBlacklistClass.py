import pandas as pd


class ClassroomBlacklistClass:

    def __init__(self, data):
        self.idDay = data.idDay
        self.idTimeSlot = data.idTimeSlot
        self.idClassroom = data.idTimeSlot


classroom_balcklist = ClassroomBlacklistClass(pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Classroom_Blacklist"))
