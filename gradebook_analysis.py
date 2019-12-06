# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 05:20:55 2019

@author: Devlin
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import gradebook_toolkit as kit
import table_gen3 as tg3

###############################################################################
def grade_analysis(file, form):
    kids = kit.sdnt_convert(file)
    with open(file) as file_obj:
        gradebook = json.load(file_obj)
    
    all_grades = [stdnt.grade*100 for stdnt in kids]
    boys_grades = [stdnt.grade*100 for stdnt in kids if stdnt.sex == 'Boy']
    girls_grades = [stdnt.grade*100 for stdnt in kids if stdnt.sex == 'Girl']
    grade_groups = [all_grades, boys_grades, girls_grades]
    class_data = [[], [], []]
    subj_titles = ['Count', 'Mean', 'Median', 'St Dev', 'Range', 'Pass Rate']
    group_titles = ['All', 'Boys', 'Girls']
    
    limit = kit.int_check("Lower Pass Boundry (1-99)>> ")
    
    for i in range(3):
        class_data[i].append(len(grade_groups[i]))
        class_data[i].append(kit.srt(np.mean(grade_groups[i])) + '%')
        class_data[i].append(str(np.median(grade_groups[i])) + '%')
        class_data[i].append(kit.srt(np.std(grade_groups[i])) + '%')
        class_data[i].append(kit.srt(max(grade_groups[i]) - min(grade_groups[i])) + '%')
        class_data[i].append((kit.srt(len([grade for grade in grade_groups[i] if grade > limit])/len(grade_groups[i])* 100)) + "%")
        
    atable = tg3.Table(subj_titles, group_titles, class_data)
    print(atable.table)
    
    all_assigned = gradebook['assignments']
    
    grades = {}    
    for assigned in all_assigned:
        dex = all_assigned.index(assigned)
        top_score = gradebook['possible_marks'][dex]
        grades[assigned] = [stdnt.marks[dex]/top_score * 100 for stdnt in kids]
    
    analysis = [[], [], [], []]
    for key in grades:
        analysis[0].append(kit.srt(max(grades[key])) + '%')
        analysis[2].append(kit.srt(min(grades[key])) + '%')
        analysis[1].append(kit.srt(np.mean(grades[key])) + '%')
        p = [g for g in grades[key] if g >= limit]
        pr = len(p)/len(grades[key])
        analysis[3].append(kit.srt(pr * 100) + "%")
        
    cats = ['Max Grade', 'Avg Grade', 'Min Grade', 'Pass Rate']    
    gtable = tg3.Table(all_assigned, cats, analysis)
    print(gtable.table)
            
    print('The Top Five: ')
    for i in range(1, 6):
        for stdnt in kids:
            if stdnt.ranked == i:
                print(stdnt)
                
    plt.figure(figsize = (8, 8))
    my_plot = sns.distplot(all_grades)
    line = my_plot.get_lines()[-1]
    x, y = line.get_data()
    mask = x > limit
    x, y = x[mask], y[mask]
    my_plot.fill_between(x, y1 = y, alpha = .5, facecolor = 'red')
    plt.title('Score Dictribution of {}'.format(form))
    plt.xlim(0, 100)
    plt.xlabel('Grades')
    plt.ylabel('Frequency')
    plt.show()
    
    sns.violinplot(data = grade_groups[1:])
    plt.title('Grade Distributions')
    plt.xlabel(' '.join(group_titles[1:]))
    plt.ylabel('Grades')
    plt.show()
    
    if 'Final Exam' in all_assigned:
        loc = all_assigned.index('Final Exam')
        top = gradebook['possible_marks'][loc]
        plt.figure(figsize = (8, 8))
        exam_marks = [stdnt.marks[loc] for stdnt in kids]
        plt.hist(exam_marks)
        plt.title('Final Exam Score Distribution')
        plt.ylabel('Count')
        plt.xlabel('Marks')
        plt.vlines(x = top, ymin = 0, ymax = 10)
        plt.show()
        
###############################################################################
def assignment_analysis(file):
    kids = kit.sdnt_convert(file)
    with open(file) as file_obj:
        gradebook = json.load(file_obj)
        
    print('Which assignment will you analyze?')
    print(*gradebook['assignments'], sep = '\n')
    
    subject = kit.pick_one(gradebook['assignments'], '\nWe will analyze... ')
        
    place = gradebook['assignments'].index(subject)
    out_of = gradebook['possible_marks'][place]
    s_marks = [k.marks[place] for k in kids]
    b_marks = [k.marks[place] for k in kids if k.sex == 'Boy']
    g_marks = [k.marks[place] for k in kids if k.sex == 'Girl']
    
    a_marks = [s_marks, b_marks, g_marks]
    
    data = []
    for cat in a_marks:
        percents = [(cat[l] / out_of) * 100 for l in range(len(cat))]
        m = round(np.mean(cat), 2)
        a = round(len([i for i in percents if i >= 90]), 2)
        b = round(len([i for i in percents if i >= 80 and i < 90]), 2)
        c = round(len([i for i in percents if i >= 70 and i < 80]), 2)
        d = round(len([i for i in percents if i >= 60 and i < 70]), 2)
        f = round(len([i for i in percents if i > 0 and i < 60]), 2)
        z = round(len([i for i in percents if i == 0]), 2)
        data.append([m, a, b, c, d, f, z])
        
    axis = ['All', 'Boys', 'Girls']
    ayis = ['Mean', '90 - 100', '80 - 89', '70 - 79', '60 - 69', '1 - 59', 'Zeros']
    
    atable = tg3.Table(ayis, axis, data)
    print(atable.table)
    
    plt.hist(s_marks)
    plt.title('{} Score Distribution'.format(subject))
    plt.xlabel('Scores')
    plt.ylabel('These Darn Kids')
    plt.show()
    
###############################################################################
def unit_compare(file):
    kids = kit.sdnt_convert(file)
    with open(file) as file_obj:
        gradebook = json.load(file_obj)
        
    comparing = []
    print('Which assignments will you compare? Type DONE to finish')
    print(*gradebook['assignments'], sep = '\n')
    while True:
        x = input('\n>> ')
        if x.lower() == 'done':
            break
        elif x not in gradebook['assignments'] or x in comparing:
            print('Not a valid assignment')
        elif x in gradebook['assignments'] and x not in comparing:
            comparing.append(x)
        else:
            print('Those conditions are mutually exclusive! I dunno how you did this....')
            
    ci = [gradebook['assignments'].index(a) for a in comparing]
    grades = [[(k.marks[a] / gradebook['possible_marks'][a]) * 100 for k in kids] for a in ci]
    means = [np.mean(a) for a in grades]
    diffs = [[kit.srt(e - means[l], 0) for e in grades[l]] for l in range(len(grades))]
    for group in diffs:
        for num in range(len(group)):
            v = group[num]
            if v[0] != '-' and v != '0.0':
                group[num] = '+' + v
                
    kid_diffs = [[int(float(group[r])) for group in diffs] for r in range(len(kids))]
    remarks = []
    for kid in kid_diffs:
        if sum([np.sign(u) for u in kid]) == -1 * len(kid):
            remarks.append('Needs Help')
        elif sum([i > 20 for i in kid]) == len(kid):
            remarks.append('Above Average')
        else:
            remarks.append('')
    
    diffs.append(remarks)
    comparing.append('Remarks')
    
    ctable = tg3.Table([k.name for k in kids], comparing, diffs)
    print(ctable.table)