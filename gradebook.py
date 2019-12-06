# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:51:09 2019

@author: Devlin
"""

import os
import gradebook_edit as ged
import gradebook_analysis as gan
import gradebook_toolkit as kit
import gradebook_admin as gad

###############################################################################
json_names = ['GradeBook1A.json', 'GradeBook1B.json', 'GradeBook2A.json', 'GradeBook2B.json']

classes = {0: '1A Maths', 1: '1B Maths', 2: '2A Maths', 3: '2B ICT'}

operations = {0: 'Quit',
              1: 'Input marks for an assignment',
              2: 'Input attendance for day',
              3: 'Change a mark for a student',
              4: 'View a student\'s grade and class rank',
              5: 'Generate a class SBA',
              6: 'View class statistics',
              7: 'Analyze an assignment',
              8: 'Compare assignments'}

actions = {1: ged.assignment_add,
           2: ged.attendance_count,
           3: ged.single_edit,
           4: ged.grade_check,
           5: ged.SBA,
           7: gan.assignment_analysis,
           8: gan.unit_compare}

admin = {'**remove': gad.remove_student,
         '**newcomer': gad.newcomer,
         '**reset': gad.gradebook_reset,
         '**debug': gad.check_raw}

###############################################################################

print('Which class is this for?')
kit.pretty_dict(classes)
        
subject = kit.pick_one(classes.keys(), 'The number of your choice >> ', ic = True)
editing = classes[subject]
grading = "C:\\Users\\Devlin\\Documents\\" + json_names[subject]

###############################################################################
os.system('cls')   
print('WELCOME\n...to the {} GradeBook!'.format(editing))    
    
while True:
    print('\nWe can do these operations')
    kit.pretty_dict(operations)
    
    ## OPERATIONS #############################################################
    action = kit.int_check("\nWhich one do you need to do >> ")
    if action in [i for i in range(1, len(operations)) if i != 6]:
        actions[action](grading)
    elif action == 6:
        gan.grade_analysis(grading, editing)
    
    ## ADMIN ##################################################################
    elif action == 12345:
        print('\nADMIN ACCESS GRANTED')
        admin_choice = input('>> ')
        if admin_choice in admin.keys():
            admin[admin_choice](grading)
        else:
            print('Goodbye')
            break
    
    ## GOODBYE ################################################################
    else:
        print('Goodbye')
        break