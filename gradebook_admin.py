# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:42:25 2019

@author: Devlin
"""

import json
import csv
import gradebook_toolkit as kit

###############################################################################
def gradebook_reset(file_name):
    c = file_name[-7:-5]
    print('Running this will reset your gradebook to empty!')
    password = 'padme is my main ho'
    attempt = input('Proceding past here requires password verification >> ')        
    if attempt == password:    
        print('Rewriting JSON....')
        register = list(csv.reader(open("C:\\Users\\Devlin\\Documents\\{}.csv".format(c))))       
        book = {'assignments': [],
                'possible_marks': []}       
        
        for s in register:
            book[s[0]] = [s[0], s[1], [], []]
            
        with open(file_name, 'w') as file:
            json.dump(book, file)   
            
    else:
        print('Exiting now')

###############################################################################
def check_raw(file_name):
     with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
     for key in gradebook:
        print('--- Next Student ---------------------------------------------')
        print(key)
        print(gradebook[key])

###############################################################################        
def remove_student(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
    
    untouchables = ['assignments', 'possible_marks']
    names = [key for key in gradebook.keys() if key not in untouchables]
    print(*names, sep = '\n')
        
    while True:
        student = input('Select a student to remove >> ')
        if student in gradebook.keys() and student not in untouchables:
            break
        else:
            print('Not a student in this class')
            sir_you_tried = kit.name_attempt(gradebook, student)
            if len(sir_you_tried) > 0:
                print('Maybe you mean...')
                print(*sir_you_tried, sep = '\n')
    
    verify = input('Are you sure >> ')
    if 'y' in verify.lower():
        del gradebook[student]
    else:
        pass
    
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)

###############################################################################
def newcomer(file_name):
    with open(file_name) as file_obj:
        gradebook = json.load(file_obj)
        
    genders = ['Boy', 'Girl']
    while True:
        new_student = input('Newcomer Name >> ')
        newcomer_sex = input('Boy or Girl >> ')
        if newcomer_sex not in genders:
            print('Try again')
        else:
            print(new_student + ' is a ' + newcomer_sex)
            check = input('Is this right? \n >> ')
            if 'y' in check.lower():
                x = len(gradebook['assignments'])
                gradebook[new_student] = [new_student, newcomer_sex, [0 for i in range(x)], []]
                break
    
    with open(file_name, 'w') as file_obj:
        json.dump(gradebook, file_obj)
 