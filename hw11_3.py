#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:46:50 2016

@author: nalingadihoke
"""



import string
import operator 
import itertools

message = "TICRTIXC'FNCRWTGWCTICPQQBTIWCGBX'JBMCUWXCAYITGT'FCTICRTIXC'FNCWXCRWQCTICFQUC'CAYITGT'FCTICPQQBTIWC'FNCWXCTICVQQNCTFC'ICP'JC'ICWXCTICRTIXC'FNCD'NCTFC'ICP'JC'ICWXCTICPQQBTIWCMXIC'FNCMQYCRQYBNCI'MCUWXCI'AXCIQJUCQPCUWTFVCQPCUWXCZWMITGT'FCMXIC'FNCNQCMQYCUWTF CAMCXHGXBBXFUCPJTXFNCUW'UC'CAYITGT'FCRWXFCWXC'NLYIUICUWXCBMJXCRQYBNCNXITJXCQJCGB'TACUQCXHGXXNCQJCVQCDXMQFNC'CAYITGT'FCTFCUWXCUTVWUXFTFVC'FNCBQQIXFTFVCUWXCIUJTFVICTCNQCFQUCUWTF CUW'UCWXCRQYBNCDYUCWXCRQYBNCGB'TACUQCXHGXXN"


def substitution(message, sub_alpha):
    d = {} 
    m = list(string.ascii_uppercase)
    m.append("'")
    m.append(" ")
    for i in range (0, 28):
        d[m[i]] = sub_alpha[i] 
    message_list = list(message)
    for z in range (0, len(message)):
        message_list[z] = d[message_list[z]]
    answer = "".join(message_list)
    return answer
    
def read_scores( input_file ):
    d = { }
    for line in open( input_file ):
        line = line.rstrip( )
        gram,score = line.split( "," )
        d[ gram ] =  float(score)
    return d
        
def count_letters( message ):
    counts = { }
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ' ":
        counts[ c ] = 0
    for c in message:
        counts[ c ] += 1
    return counts

    
def score_string(message, scores):
    score = 0.0
    for i in range(0, len(message)):
        if len(message[i:i+3]) == 3:
            try:
                score += float(scores[message[i:i+3]])
            except:
                score -= 11.0
        else:
            break
    return score
    
    
def evaluate( candidate,message,scores ):
    x = substitution( message,candidate )
    return score_string( x,scores )
    
def step(current_solution, message, scores):
    current_temp = current_solution[:]
    for s in itertools.combinations(current_solution, 2):
        temp1 = current_temp[:]
        a,b = s
        m,n = temp1.index(a), temp1.index(b)
        temp1[m], temp1[n] = temp1[n], temp1[m]
        if evaluate(temp1, message, scores) > evaluate(current_temp, message, scores):
            current_temp = temp1
        else:
            temp1[m], temp1[n] = temp1[n], temp1[m]
    return current_temp
        
def find_secret(message):
    
    d1 = read_scores('1-scores.csv')
    sorted_d1 = sorted(d1.items(), key=operator.itemgetter(1))
   
    
    d2 = count_letters(message)
    sorted_d2 = sorted(d2.items(), key=operator.itemgetter(1))

    translation = {}


    for i in range(28):
        translation[sorted_d2[i][0]] = sorted_d1[i][0]

    

    sub_alpha_temp = sorted(translation.items(), key=operator.itemgetter(0))
    sub_alpha = []

    i = 0
    while i <28:
        temp = sub_alpha_temp[i][1]
        sub_alpha.append(temp)
        i += 1
    sub_alpha.append(sub_alpha[1])
    sub_alpha.append(sub_alpha[0])
    del sub_alpha[0]
    del sub_alpha[0]

    greedy_output = substitution(message, sub_alpha)
    
    d3l = read_scores("3-scores.csv")
    
    
    for i in range(50):
        if sub_alpha == step(sub_alpha, greedy_output, d3l):
            break
        else:
            sub_alpha = step(sub_alpha, greedy_output, d3l)
            
            
    return substitution(greedy_output, sub_alpha)
    
print (find_secret(message))