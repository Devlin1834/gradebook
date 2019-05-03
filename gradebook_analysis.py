# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 05:20:55 2019

@author: Devlin
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import gradebook_update
import table_gen2

def grade_analysis(file, form):
    kids = gradebook_update.grade_update(file)
    
    all_grades = [stdnt.grade*100 for stdnt in kids]
    boys_grades = [stdnt.grade*100 for stdnt in kids if stdnt.sex == 'Boy']
    girls_grades = [stdnt.grade*100 for stdnt in kids if stdnt.sex == 'Girl']
    grade_groups = [all_grades, boys_grades, girls_grades]
    class_data = [[], [], []]
    subj_titles = ['Mean', 'Median', 'St Dev', 'Range', 'Pass Rate']
    group_titles = ['All', 'Boys', 'Girls']
    
    for i in range(3):
        class_data[i].append(str(round(np.mean(grade_groups[i]), 2)))
        class_data[i].append(str(np.median(grade_groups[i])))
        class_data[i].append(str(round(np.std(grade_groups[i]), 2)))
        class_data[i].append(str(round(max(grade_groups[i]) - min(grade_groups[i]), 2)))
        class_data[i].append(str(round(len([grade for grade in grade_groups[i] if grade > 69.9]/len(grade_groups[i])), 2)))
        
    table_gen2.table_gen(row_names = subj_titles, col_names = group_titles, list_of_lists = class_data)
            
    print('The Top Five: ')
    for i in range(1, 6):
        for stdnt in kids:
            if stdnt.ranked == i:
                print(stdnt)
                
                
        
    plt.figure(figsize = (8, 8))
    sns.distplot(all_grades, rug = True)
    plt.title('Score Dictribution of {}'.format(form))
    plt.xlabel('Grades')
    plt.ylabel('Frequency')
    plt.show()
    
    sns.violinplot(data = grade_groups[1:])
    plt.title('Grade Distributions')
    plt.xlabel(' '.join(group_titles[1:]))
    plt.ylabel('Grades')
    plt.show()
                
    
    
    
    