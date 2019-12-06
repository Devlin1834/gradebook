# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:42:23 2019

@author: Devlin
"""

import json

###############################################################################
class Student():
    def __init__(self, name, sex, marks, attendance, grade = False, ranked = False):
        self.name = name
        self.sex = sex
        self.marks = marks
        self.total_marks = sum(self.marks)
        self.attendance = attendance
        #self.a_rate = round(len([d for d in self.attendance if d != 0])/len(self.attendance), 2)
        self.grade = grade
        self.ranked = ranked
        
    def __str__(self):
        if len(self.attendance) > 0:
            return '{}: {}%, Ranked {} - Attendance {}%'.format(self.name, self.grade*100, self.ranked, self.a_rate*100)
        else:
            return '{}: {}%, Ranked {}'.format(self.name, self.grade*100, self.ranked)

###############################################################################
def sba_rank(data):
    data_dict = {}
    rank = 1
    for point in sorted(data, reverse = True):
        if point not in data_dict.keys():
            data_dict[point] = rank
            rank += 1
        
    return [data_dict[i] for i in data]

###############################################################################
def comp_bar(n, array):
    s = sorted(array)
    i = s.index(n)
    p = round(20 * i / len(s))
    r = ['=' for i in range(20)]
    r[p] = 'H'
    
    return ''.join(r)

###############################################################################
def name_attempt(book, attempt):
    untouchables = ['assignments', 'possible_marks']
    names = [key for key in book.keys() if key not in untouchables]
    seps = [x.find(' ') for x in names]
    first = [names[i][:seps[i]] for i in range(len(names))]
    last = [names[i][seps[i] + 1:] for i in range(len(names))]
    
    a_sep = attempt.find(' ')
    a_first = attempt[:a_sep]
    a_last = attempt[a_sep + 1:]
    
    f_match = [first.index(n) for n in first if n == a_first]
    l_match = [last.index(n) for n in last if n == a_last]
    matches = []
    for m in f_match:
        matches.append(names[m])
    for m in l_match:
        if names[m] not in matches:
            matches.append(names[m])
        
    return matches

###############################################################################
def int_check(string):
    while True:
        try:
            some_number = int(input(string))
        except ValueError:
            print('This needs to be a number')
        else:
            return some_number

###############################################################################
def sdnt_convert(file):
    with open(file) as file_obj:
        gradebook = json.load(file_obj)
        
    untouchables = ['assignments', 'possible_marks']
    students_raw = [gradebook[key] for key in gradebook if key not in untouchables]
    all_students = [Student(*i) for i in students_raw]
    
    total_points_offered = sum(gradebook['possible_marks'])
    for stdnt in all_students:
        stdnt.grade = round(stdnt.total_marks/total_points_offered, 2)
    
    grades = [stdnt.grade for stdnt in all_students]
    rankings = sba_rank(grades)
    
    for i in range(len(all_students)):
        all_students[i].ranked = rankings[i]
    
    with open(file, 'w') as file_obj:
        json.dump(gradebook, file_obj)
    
    all_students.sort(key = lambda x: x.name)
    return all_students

###############################################################################
def pick_one(choices, text, wrong = "That's not a valid choice", ic = False):
    
    while True:
        if ic:
            p = int_check(text)
        else:
            p = input(text)
            
        if p in choices:
            return p
        else:
            print(wrong)

###############################################################################
def srt(digit, n = 2):
    return str(round(digit, n))

###############################################################################
def pretty_dict(dic):
    for key in dic:
        print(str(key) + ": " + dic[key])