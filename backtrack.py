# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:53:59 2020

@author: BENHMA
"""

import pandas as pd
from read_excel import *
from tests import *



def backtrack(idLecturer, idLec, idLecObj, d , ts, schedule, index1):
    check= False
    schedule1= schedule
    idClassroom= 0

    if LecturerBlacklistInBlock( idLecturer, d, ts)== False:
        if LecturerBusy ( schedule1, idLecturer, d , ts) == False:
         if StudentGroupsListBlackList(stdGroupsPerLecture (idLec), d, ts)== False:
             if StudentGroupsBusy (stdGroupsPerLecture (idLec), d, ts, schedule1):

                                 idClassroom= SearchFreeClass(d,ts, schedule1, idLec)
                                 if int(idClassroom) == 0:
                                     check= False

                                 else:
                                     check = True
    new_row= {"idDay": d,  "idTimeSlot": ts,  "idLectureObject": idLecObj, 'idClassroom': idClassroom, 'idLecturer': idLecturer}
    if check== True:

             schedule1= schedule.insert(0, new_row)
             print (new_row)
             schedule = schedule1

             return ( schedule)

    elif check == False:
        if ts<6 :
            backtrack (idLecturer, idLec, idLecObj, d , ts+1, schedule, index1)
        else:
            backtrack (idLecturer, idLec, idLecObj, d+1, 1, schedule, index1)
