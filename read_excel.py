# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:36:55 2020

@author: BENHMA
"""

import xlrd
lecture = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecture")
lecturer = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecturer")
classroom = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Classroom")
lecture_has_studentgroup = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecture_has_StudentGroup")
lecturer_blacklist = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Lecturer_Blacklist")
classroom_blacklist = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="Classroom_Blacklist")
studentgroup = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="StudentGroup")
studentgroup_blacklist = pd.read_excel("TimeTableProblem_B.xlsx", sheet_name="StudentGroup_Blacklist")


