# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:30:09 2019

@author: Devlin
"""

class Student():
    def __init__(self, name, sex, marks, grade = False, ranked = False):
        self.name = name
        self.sex = sex
        self.marks = marks
        self.total_marks = sum(self.marks)
        self.grade = grade
        self.ranked = ranked
        
    def __str__(self):
        return '{}: {}%, Ranked {}'.format(self.name, self.grade*100, self.ranked)
    

        