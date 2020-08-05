# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:55:47 2020

@author: BENHMA
"""

import pandas as pd
from read_excel import *
from tests import *
from backtrack import *
from openpyxl.workbook import Workbook

def search():
     schedule = []
    
     for index1, Lecture in  lecture.iterrows():
            backtrack(Lecture['idLecturer'], Lecture['idLecture'], Lecture['idLectureObject'], 1, 1, schedule, index1)

     df = pd.DataFrame.from_dict(schedule)
     df.to_excel('sched.xlsx')
     
     
                             
     



search()
           
