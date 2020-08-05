# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:42:13 2020

@author: BENHMA
"""



import pandas as pd
import time
from read_excel import *
import numpy as np




def LecturerBlacklistInBlock (x, d, ts):
         result = False
         for indexLB, rowLB in lecturer_blacklist.iterrows():
                
                if x == rowLB['idLecturer']:
                    if rowLB['idDay'] == d:
                        if rowLB['idTimeSlot'] == ts :                       
                            return True
         return result
     
                            

def StudentGroupBlacklistInBlock (x, d, ts):
         result = False
         for indexSB, rowSB in studentgroup_blacklist.iterrows():               
                if x == rowSB['idStudentGroup']  :
                    if rowSB['idDay'] == d:
                    
                       if rowSB['idTimeSlot'] == ts:
                            result = True
         return result




def StudentGroupsListBlackList(list, d, ts):
    for l in list:
        if StudentGroupBlacklistInBlock(l, d,ts)== True:
            return True
    return False



def ObjectPerLecture (idObj):
    for index, row in lecture.iterrows():
        if row['idLectureObject']== idObj:
            return int(row['idLecture'])
        


def checkGroup(group, idLec):
    for index, row in lecture_has_studentgroup.iterrows():
        if row['idLecture'] == idLec:
            if row['idStudentGroup'] == group:
                return False
    return True          
    

def StudentGroupsBusy (groups, d, ts, list):
         for group in groups:
             for el in list or []:
                 if d== el['idDay']:
                     if ts== el['idTimeSlot']:
                         if checkGroup ( group, ObjectPerLecture(el['idLectureObject'])) == False:
                             return False
         return True
     
        



def classroomBlacklist(idClassroom, idDay, idTS):
    for index, rowCL in classroom_blacklist.iterrows():

        
        if idClassroom == rowCL['idClassroom'] :
            if idDay == rowCL['idDay']:
                if idTS == rowCL['idTimeSlot']:
                    return True
        
    return False
        
classroomBlacklist (1, 5,6)

def stdGroupsPerLecture (idLec):
    stdGroups= []
    for index, row in  lecture_has_studentgroup.iterrows():
        if idLec == row['idLecture']:
            idStdGroup = str(row['idStudentGroup'])
            stdGroups.append(idStdGroup)
    return stdGroups



def numParticipantsPerLecture (idLec):
            num = 0
            for index, row in  lecture_has_studentgroup.iterrows():
               if idLec == int(row['idLecture']):
                   num= num + int (row['numParticipants'])
            return num
         
            
        
def elementInList (list, idToCheck, d , ts, param):
    res= False
    for el in list or []:
        res = ElementBusy (idToCheck, el, d, ts, res, param)
        if res == True:
            return True
    return res


def ElementBusy (idToCheck, el, d, ts, res, param):
         result = res
         
                
         if int(el[param]) == int(idToCheck) :
             if int(el['idDay']) == int(d) :
                 if int(el['idTimeSlot']) == int(ts) :
                     result= True
         return result
     
        

def checkClassromIsEnough(idLec, idClassroom):
        numStudents=  numParticipantsPerLecture (idLec)
        for index, row in  classroom.iterrows():
            if idClassroom == row['idClassroom']:
                if numStudents >  row['Capacity']:
                    return False
                else:
                    return True
        return False
                
                


def testClass(list, idClass, ts , d):
    test= True
    for el in list or []:
            
            if el['idClassroom'] == idClass:
                 if el['idDay'] == d:
                    if el['idTimeSlot'] == ts:
                        return False
            
    return test                   



def SearchFreeClass(d,ts, list, idLec):   
    for index, row in classroom.iterrows():
        
        if testClass(list, row['idClassroom'], ts, d)== True:   
                if  classroomBlacklist(int(row['idClassroom']), d, ts) == False:
                    if checkClassromIsEnough(idLec, int(row['idClassroom'])):
                        return int(row['idClassroom'])
    return 0

            
def LecturerBusy(list, idLecturer, d ,ts):
    for el in list or []:
       if el['idDay']== d:
           if el['idTimeSlot']== ts:
               if el['idLecturer'] == idLecturer:
                   return True
              
    return False
            
    



        






