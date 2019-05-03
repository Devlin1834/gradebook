# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:01:55 2019

@author: Devlin
"""

import json
import os
import student_class
import table_gen2

def sba_rank(data):
    data_dict = {}
    rank = 1
    for point in sorted(data, reverse = True):
        if point not in data_dict.keys():
            data_dict[point] = rank
            rank += 1
        
    return [data_dict[i] for i in data]


def grade_update(file):
    with open(file) as file_obj:
        gradebook = json.load(file_obj)
        
    untouchables = ['assignments', 'possible_marks']
    students_raw = [gradebook[key] for key in gradebook if key not in untouchables]
    all_students = [student_class.Student(*i) for i in students_raw]
    
    total_points_offered = sum(gradebook['possible_marks'])
    for stdnt in all_students:
        stdnt.grade = round(stdnt.total_marks/total_points_offered, 2)
    
    grades = [stdnt.grade for stdnt in all_students]
    rankings = sba_rank(grades)
    
    for i in range(len(all_students)):
        all_students[i].ranked = rankings[i]
    
    with open(file, 'w') as file_obj:
        json.dump(gradebook, file_obj)

    return all_students

def grade_check(file_name):
    kids = grade_update(file_name)
    names = [stdnt.name for stdnt in kids]
    print('\nGrade Check')
    while True:
        to_see = input('Student Name >> ')
        if to_see in names:
            index = names.index(to_see)
            break
        else:
            print('thats not a student')
    
    print(kids[index])
    input('Done?')
    os.system('cls')
    
def SBA(file_name):
    kids = grade_update(file_name)
    names = [stdnt.name for stdnt in kids]
    final_grades = [str(round(stdnt.grade*100, 2)) for stdnt in kids]
    term_grade = [str(round(float(i)/2, 2)) for i in final_grades]
    test_grade = [str(round(.4*float(i), 2)) for i in term_grade]
    classwork = [str(round(.2*float(i), 2)) for i in term_grade]
    ranks = [str(stdnt.ranked) for stdnt in kids]
    columns = ['Test 1', 'Project Work', 'Test 2', 'Group Work', 'Term Total', 'Final Exam', 'Final Grade', 'Ranks']
    sba_data = [test_grade, classwork, classwork, classwork, term_grade, term_grade, final_grades, ranks]
    print('\n---All Students---')
    table_gen2.table_gen(row_names = names, col_names = columns, list_of_lists = sba_data)
    
    bnames = [stdnt.name for stdnt in kids if stdnt.sex == 'Boy']
    bfinal_grades = [str(round(stdnt.grade*100, 2)) for stdnt in kids if stdnt.sex == 'Boy']
    bterm_grade = [str(round(float(i)/2, 2)) for i in bfinal_grades]
    btest_grade = [str(round(.4*float(i), 2)) for i in bterm_grade]
    bclasswork = [str(round(.2*float(i), 2)) for i in bterm_grade]
    branks = [str(stdnt.ranked) for stdnt in kids if stdnt.sex == 'Boy']
    bsba_data = [btest_grade, bclasswork, bclasswork, bclasswork, bterm_grade, bterm_grade, bfinal_grades, branks]
    print('\n---   Boys   ---')
    table_gen2.table_gen(row_names = bnames, col_names = columns, list_of_lists = bsba_data)
    
    gnames = [stdnt.name for stdnt in kids if stdnt.sex == 'Girl']
    gfinal_grades = [str(round(stdnt.grade*100, 2)) for stdnt in kids if stdnt.sex == 'Girl']
    gterm_grade = [str(round(float(i)/2, 2)) for i in gfinal_grades]
    gtest_grade = [str(round(.4*float(i), 2)) for i in gterm_grade]
    gclasswork = [str(round(.2*float(i), 2)) for i in gterm_grade]
    granks = [str(stdnt.ranked) for stdnt in kids if stdnt.sex == 'Girl']
    gsba_data = [gtest_grade, gclasswork, gclasswork, gclasswork, gterm_grade, gterm_grade, gfinal_grades, granks]
    print('\n---   Girls   ---')
    table_gen2.table_gen(row_names = gnames, col_names = columns, list_of_lists = gsba_data)
    
    