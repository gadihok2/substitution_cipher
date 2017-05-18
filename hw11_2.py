#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:44:22 2016

@author: nalingadihoke
"""

import string 
import operator 


#function to map alphabet to its floating point value in the score column 

def read_scores( input_file ):
   d = { }
   for line in open( input_file ):
       line = line.rstrip( )
       gram,score = line.split( "," )
       d[ gram ] =  float(score)
   return d
   
#function to count the frequencies in the encoded message 

def count_letters( message ):
    counts = { }
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ' ":
        counts[ c ] = 0
    for c in message:
        counts[ c ] += 1
    return counts
    
#decrypt the message using above two functions 

#ascending order of frequency of letter in alphabet 
d1 = read_scores('1-scores.csv')
sorted_d1 = sorted(d1.items(), key=operator.itemgetter(1))

#ascending order of frequency of letter in substitution alphabet 
sample = "TICRTIXC'FNCRWTGWCTICPQQBTIWCGBX'JBMCUWXCAYITGT'FCTICRTIXC'FNCWXCRWQCTICFQUC'CAYITGT'FCTICPQQBTIWC'FNCWXCTICVQQNCTFC'ICP'JC'ICWXCTICRTIXC'FNCD'NCTFC'ICP'JC'ICWXCTICPQQBTIWCMXIC'FNCMQYCRQYBNCI'MCUWXCI'AXCIQJUCQPCUWTFVCQPCUWXCZWMITGT'FCMXIC'FNCNQCMQYCUWTF CAMCXHGXBBXFUCPJTXFNCUW'UC'CAYITGT'FCRWXFCWXC'NLYIUICUWXCBMJXCRQYBNCNXITJXCQJCGB'TACUQCXHGXXNCQJCVQCDXMQFNC'CAYITGT'FCTFCUWXCUTVWUXFTFVC'FNCBQQIXFTFVCUWXCIUJTFVICTCNQCFQUCUWTF CUW'UCWXCRQYBNCDYUCWXCRQYBNCGB'TACUQCXHGXXN"
d2 = count_letters(sample)
sorted_d2 = sorted(d2.items(), key=operator.itemgetter(1))

translation = {}

i = 27
while i>-1:
    translation[sorted_d2[i][0]] = sorted_d1[i][0]
    i -= 1 
    

sub_alpha_temp = sorted(translation.items(), key=operator.itemgetter(1))
sub_alpha = []

i = 0
while i <28:
    temp = sub_alpha_temp[i][0]
    sub_alpha.append(temp)
    i += 1
sub_alpha.append(sub_alpha[1])
sub_alpha.append(sub_alpha[0])
del sub_alpha[0]
del sub_alpha[0]

def substitution(message, sub_alpha):
    #create empty dictionary 
    d = {}
    #list of uppercase alphabet 
    m = list(string.ascii_uppercase)
    m.append("'")
    m.append(" ")
    #update dictionary according to substitution alphabet
    for i in range (0,28):
        d[sub_alpha[i]] = m[i]
    #go over string and encode/decode it by first making it a list 
    message_list = list(message)
    answer_list = []
    for z in range (0, len(message)):
        temp = d[message_list[z]]
        answer_list.append(temp)
    answer = "".join(answer_list)
    return answer

greedy_output = substitution(sample, sub_alpha)

#print (greedy_output, d1, d2, sorted_d1)
print(translation)