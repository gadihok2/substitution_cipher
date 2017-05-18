#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:43:07 2016

@author: nalingadihoke
"""

import string 


message1 = "This semester saw me work on papers concerning my main research topic. Having analyzed my own topic and having written a paper arguing the exact opposite of what my stance on the India-Pakistan-Kashmir issue is, I have arrived at a thesis for my final paper. I want my fourth paper to argue in favor of the relatively new foreign policy the current Indian government has taken since coming to power in, with emphasis on the hardened stand taken against Pakistan. To bolster my main argument, my paper will discuss why this new policy is the correct way to move forward in terms of curbing terrorism and, how it will play in India's favor to keep invoking sanctions on Pakistan on economic fronts and to globally make them out as the instigator in the Kashmir conflict by increasing diplomatic efforts with the UN and other countries. My thesis will occupy the two stasis of definition and cause/effect. In order to explain and elaborate on the new foreign policy adopted by India, I will first need to talk about its aspects, its roots and how it came to be, in my paper, all of which justify my classification of the thesis under stasis of definition."
message = message1.replace(".", "").replace(",", "").replace("/", " ").replace("-", " ").upper()
def substitution(message, sub_alpha):
    #create empty dictionary 
    d = {}
    #list of uppercase alphabet 
    m = list(string.ascii_uppercase)
    m.append("'")
    m.append(" ")
    #update dictionary according to substitution alphabet
    for i in range (0, 28):
        d[m[i]] = sub_alpha[i]
    #go over string and encode/decode it by first making it a list 
    message_list = list(message)
    for z in range (0, len(message)):
        message_list[z] = d[message_list[z]]
    answer = "".join(message_list)
    return answer
    
key1 =  " 'ZYXWVUSQRTOPNMHLGAFDEIKTCB"
key = list(key1)
print(substitution(message, key))