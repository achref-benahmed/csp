import pandas as pd

class LectureHasStudentGroupClass:

    def __init__(self, data):
        self.idLecture = data.idLecture
        self.idStudentGroup = data.idStudentGroup
        self.numParticipants = data.numParticipants


lecture_has_studentgroup = LectureHasStudentGroupClass(pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecture_has_StudentGroup"))

