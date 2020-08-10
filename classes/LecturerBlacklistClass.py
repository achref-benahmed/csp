import pandas as pd


class LecturerBlacklistClass:

    def __init__(self, data):
        self.idDay = data.idDay
        self.idTimeSlot = data.idTimeSlot
        self.idLecturer = data.idLecturer


lecturer_black_list = LecturerBlacklistClass(pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecturer_Blacklist"))
