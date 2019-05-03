# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 13:54:44 2019

@author: Devlin
"""

import json
import csv

def gradebook_reset():
    one_a = list(csv.reader(open("C:\\Users\\Devlin\\Documents\\1a.csv")))
    two_a = list(csv.reader(open("C:\\Users\\Devlin\\Documents\\2a.csv")))
    two_b = list(csv.reader(open("C:\\Users\\Devlin\\Documents\\2b.csv")))

    students_1A = {'assignments': [],
                   'possible_marks': []}
    students_2A = {'assignments': [],
                   'possible_marks': []}
    students_2B = {'assignments': [],
                   'possible_marks': []}

    for i in one_a:
        students_1A[i[0]] = [i[0], i[1], []]
    
    for i in two_a:
        students_2A[i[0]] = [i[0], i[1], []]
    
    for i in two_b:
        students_2B[i[0]] = [i[0], i[1], []]
    
    print('Running this will rewrite your JSONs!')
    while True:
        password = 'padme is my main ho'
        attempt = input('Proceding past here requires password verification >> ')
        if attempt == password:    
            print('Ok fine whatever\nRewriting JSONs....')
            json_names = ['GradeBook1A.json', 'GradeBook2A.json', 'GradeBook2B.json']
            json_dicts = [students_1A, students_2A, students_2B]
            for i in range(3):
                with open("C:\\Users\\Devlin\\Documents\\" + json_names[i], 'w') as file_obj:
                    json.dump(json_dicts[i], file_obj)
            break
        else:
            print('Exiting now')
            break