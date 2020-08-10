import pandas as pd

class LectureClass:

    def __init__(self, data):
        self.idLectureObject = data.idLectureObject
        self.idLecture = data.idLectureObject
        self.idLecturer = data.idLecturer


lecture = LectureClass(pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecture"))

print (lecture.idLecturer)