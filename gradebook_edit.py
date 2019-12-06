# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:22:19 2019

@author: Devlin
"""

import os
import json
import numpy as np
import table_gen3 as tg3
import gradebook_toolkit as kit
    
###############################################################################
def assignment_add(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
   
    assignment_name = input('Assignment Name >> ')
    assignment_points = kit.int_check('Marks Possible >> ')
        
    gradebook['assignments'].append(assignment_name)
    gradebook['possible_marks'].append(assignment_points)
    
    print('\nType DONE when finished')
    graded = ['assignments', 'possible_marks']
    while True:
        this_student = input('Student Name >> ')
        if this_student not in graded and this_student in gradebook.keys():
            marks = kit.int_check('Marks >> ')
            gradebook[this_student][2].append(marks)
            graded.append(this_student)
        elif this_student.lower() == 'done':
            break
        else:
            print('Try a different student')
            sir_you_tried = kit.name_attempt(gradebook, this_student)
            if len(sir_you_tried) > 0:
                print('Maybe you mean...')
                print(*sir_you_tried, sep = '\n')
            
    for i in gradebook.keys():
        if i not in graded:
            gradebook[i][2].append(0)
            
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)

###############################################################################        
def single_edit(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
    while True:
        student = input('Select a student to edit >> ')
        if student in gradebook.keys():
            break
        else:
            print('Not a student in this class')
            sir_you_tried = kit.name_attempt(gradebook, student)
            if len(sir_you_tried) > 0:
                print('Maybe you mean...')
                print(*sir_you_tried, sep = '\n')
    
    print(*gradebook['assignments'], sep = '\n')    
    assignment = kit.pick_one(gradebook['assignments'], 'Pick an assignment to edit >> ')
    
    current_marks = gradebook[student][2][gradebook['assignments'].index(assignment)]
    print('{} got a {} on {}'.format(student, current_marks, assignment))
    new_marks = kit.int_check('But {} should have gotten >> '.format(student))
    gradebook[student][2][gradebook['assignments'].index(assignment)] = new_marks
    
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)

###############################################################################
def attendance_count(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
    print('\nType DONE when finished')
    untouchables = ['assignments', 'possible_marks']
    while True:
        this_student = input('Student Name >> ')
        if this_student not in untouchables and this_student in gradebook.keys():
            marks = kit.int_check('Attendance >> ')
            gradebook[this_student][3].append(marks)
            untouchables.append(this_student)
        elif this_student.lower() == 'done':
            break
        else:
            print('Try a different student')
            
    for i in gradebook.keys():
        if i not in untouchables:
            gradebook[i][3].append(0)
            
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj) 

###############################################################################
def grade_check(file_name):
    kids = kit.sdnt_convert(file_name)
    names = [stdnt.name for stdnt in kids]
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
    print('\nGrade Check')
    while True:
        to_see = input('Student Name >> ')
        if to_see in names:
            index = names.index(to_see)
            break
        elif to_see.lower() == 'check':
            print(*names, sep = '\n')
        else:
            print("That's not a student")
            sir_you_tried = kit.name_attempt(gradebook, to_see)
            if len(sir_you_tried) > 0:
                print('Maybe you mean...')
                print(*sir_you_tried, sep = '\n')
            
    subject = kids[index]  
    work = gradebook['assignments']
    cats = ['Marks', 'Class Avg', 'Position']
    
    print(subject)
    
    all_marks = [[k.marks[i] for k in kids] for i in range(len(work))]        
    class_avg = [round(np.mean(m), 2) for m in all_marks]
    bars = [kit.comp_bar(subject.marks[a], all_marks[a]) for a in range(len(work))]
    final = [subject.marks, class_avg, bars] 
    mtable = tg3.Table(work, cats, final)
    print(mtable.table)
    
    input('Done?')
    os.system('cls')

###############################################################################    
def SBA(file_name):
    kids = kit.sdnt_convert(file_name)
    
    for x in ['Boy', 'Girl']:
        names = [stdnt.name for stdnt in kids if stdnt.sex == x]
        final_grades = [round(stdnt.grade*100, 1) for stdnt in kids if stdnt.sex == x]
        term_grade = [round(i / 2, 1) for i in final_grades]
        test_grade = [round(.4 * i, 1) for i in term_grade]
        classwork = [round(.2 * i, 1) for i in term_grade]
        ranks = [stdnt.ranked for stdnt in kids if stdnt.sex == x]
        columns = ['Test 1', 'Project Work', 'Test 2', 'Group Work', 'Term Total', 'Final Exam', 'Final Grade', 'Ranks']
        sba_data = [test_grade, classwork, classwork, classwork, term_grade, term_grade, final_grades, ranks]
        print('\n--- {}s ---'.format(x))
        sba = tg3.Table(names, columns, sba_data)
        print(sba.table)