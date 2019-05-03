# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:22:19 2019

@author: Devlin
"""

import json

def int_check(string):
    while True:
        try:
            some_number = int(input(string))
        except ValueError:
            print('This needs to be a number')
        else:
            break
    
    return some_number
    

def assignment_add(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
   
    assignment_name = input('Assignment Name >> ')
    assignment_points = int_check('Marks Possible >> ')
        
    gradebook['assignments'].append(assignment_name)
    gradebook['possible_marks'].append(assignment_points)
    
    print('\nType DONE when finished')
    graded = ['assignments', 'possible_marks']
    while True:
        this_student = input('Student Name >> ')
        if this_student not in graded and this_student in gradebook.keys():
            marks = int_check('Marks >> ')
            gradebook[this_student][2].append(marks)
            graded.append(this_student)
        elif this_student.lower() == 'done':
            break
        else:
            print('Try a differen student')
    
    for i in gradebook.keys():
        if i not in graded:
            gradebook[i][2].append(0)
            
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)
        
def single_edit(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
    while True:
        student = input('Select a student to edit >> ')
        if student in gradebook.keys():
            break
        else:
            print('Not a student in this class')
    
    for assignment in gradebook['assignments']:
        print(assignment)
        
    while True:    
        assignment = input('Pick an assignment to edit >> ')
        if assignment in gradebook['assignments']:
            break
        else:
            print('Thats not a valid assignment')
    
    current_marks = gradebook[student][2][gradebook['assignments'].index(assignment)]
    print('{} got a {} on {}'.format(student, current_marks, assignment))
    new_marks = int_check('But {} should have gotten >> '.format(student))
    gradebook[student][2][gradebook['assignments'].index(assignment)] = new_marks
    
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)
        
def remove_student(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
    
    untouchables = ['assignments', 'possible_marks']
    for i in gradebook.keys():
        if i not in untouchables:
            print(i)
        
    while True:
        student = input('Select a student to remove >> ')
        if student in gradebook.keys() and student not in untouchables:
            break
        else:
            print('Not a student in this class')
    
    verify = input('Are you sure >> ')
    if verify.lower() == 'y':
        del gradebook[student]
    else:
        pass
    
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)

def newcomer(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
    genders = ['Boy', 'Girl']
    while True:
        new_student = input('Select a student to remove >> ')
        newcomer_sex = input('Boy or Girl >> ')
        if newcomer_sex not in genders:
            print('Try again')
        else:
            print(new_student + ' is a ' + newcomer_sex)
            check = input('Is this right? \n >> ')
            if 'y' in check.lower():
                gradebook[new_student] = [new_student, newcomer_sex, []]
                break
    
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)
    
