# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:51:09 2019

@author: Devlin
"""

import gradebook_edit
import gradebook_update
import gradebook_analysis
import gradebook_create

json_names = ['GradeBook1A.json', 'GradeBook2A.json', 'GradeBook2B.jon']
classes = {0: '1A Maths', 1: '2A Maths', 2: '2B ICT'}
operations = {0: 'Quit',
              1: 'Input marks for an assignment',
              2: 'Change a mark for a student',
              3: 'View a student\'s grade and class rank',
              4: 'Generate a class SBA',
              5: 'View class statistics'}

def class_select():
    print('Which class is this for?')
    for key in classes:
        print(str(key) + ": " + classes[key])
        
    while True:
        try:
            choice = int(input('The number of your choice >> '))
        except ValueError:
            print('Pick the number of the class')
        else:
            if choice not in classes.keys():
                print('Try again')
            else:
                break

    return choice

if __name__ == '__main__':
    
    subject = class_select()
    
    editing = classes[subject]
    grading = "C:\\Users\\Devlin\\Documents\\" + json_names[subject]
    
    print('\nWELCOME\n...to the {} GradeBook!'.format(editing))    
    
    while True:
        print('\nWe can do these operations')
        for key in operations:
            print(str(key) + ': ' + operations[key])
        action = gradebook_edit.int_check("\nWhich one do you need to do >> ")
        if action == 1:
            gradebook_edit.assignment_add(grading)
        elif action == 2:
            gradebook_edit.single_edit(grading)
        elif action == 3:
            gradebook_update.grade_check(grading)
        elif action == 4:
            gradebook_update.SBA(grading)
            break
        elif action == 5:
            gradebook_analysis.grade_analysis(grading, editing)
            break
        elif action == 12345:
            print('\nADMIN ACCESS GRANTED')
            admin_choice = input('>> ')
            if admin_choice == '**remove':
                gradebook_edit.remove_student(grading)
            elif admin_choice == '**reset':
                gradebook_create.gradebook_reset()
            elif admin_choice == '**newcomer':
                gradebook_edit.newcomer(grading)
            else:
                print('Goodbye')
                break
        else:
            print('Goodbye')
            break