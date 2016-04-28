#!/usr/bin/python
# coding: utf-8

# In[274]:

import string
from collections import defaultdict
import random
import re
import numpy as np
from statistics import *
import math
import sys


def roundoff(value):
    if( (value < 1.0) and (value > 0.998) ):
        return 1.0
    else:
        return value
        




def get_length(inputt):
    words = [ w for w in inputt.split(' ') if w != ""]
    m = mean(map(len, words))
    s = stdev(map(len, words))
    return math.floor(random.gauss(m, s))
    


def count_ocurrance_two(inputt):
    ocurrancies = defaultdict(lambda: 0)
    
    last_char_read = None
    
    for ch in inputt:
        if (last_char_read != None):
            ocurrancies[last_char_read +  ch] += 1
        
        last_char_read = ch
    
    return ocurrancies
            


# In[310]:

def create_fequencies_two(inputt):
    occurences = count_ocurrance_two(inputt)
    freq = defaultdict(lambda: 0)
    
    regular_occurance = { key:value for key, value in occurences.items() if key[1] != ' ' }
    word_ending_occurances = { key:value for key, value in occurences.items() if key[1] == ' ' }
    
    if(len(occurences) > 0):
        
        for k , v in regular_occurance.items():
            freq[k] = v / float( sum([value for key, value in regular_occurance.items() if key[0] == k[0]]))
        
        for k , v in word_ending_occurances.items():
            freq[k] = v / float( sum([value for key, value in word_ending_occurances.items()]))
    
    return freq
        
        
           
         


# In[311]:

def execute_two(freq):
    last_key = None
    cum_value = 0.0
    
    for key in sorted({k for k in  freq.keys() if k[1] != ' ' }):
        if((last_key != None) and (last_key[0] != key[0])):
            cum_value = 0.0
        cum_value += freq[key]
        cum_value = roundoff(cum_value) 
        freq[key] = cum_value
        last_key = key
    
    cum_value = 0.0
    
    for key in sorted({k for k in  freq.keys() if k[1] == ' ' }):
        cum_value += freq[key]
        cum_value = roundoff(cum_value) 
        freq[key] = cum_value
    
    return freq
    
    
        

    


# ## Three Letter Functions

# In[312]:

def count_ocurrance_three(inputt):
    occurances = defaultdict(lambda: 0)
    
    last_char = None
    next_2_last = None
    
    for ch in inputt:
        if ((last_char != None) and (next_2_last != None)):
            occurances[next_2_last + last_char + ch] += 1
        
        next_2_last = last_char
        last_char = ch
    
    return {key:value for key , value in occurances.items() if key[1] != ' '}


# In[313]:

def create_fequencies_three(inputt):
    occurences =  count_ocurrance_three(inputt)
    
    freq = defaultdict(lambda: 0)
    
    regular_occurance = { key:value for key, value in occurences.items() if key[2] != ' ' }
    word_ending_occurances = { key:value for key, value in occurences.items() if key[2] == ' ' }
    
    if(len(occurences) > 0):
        
        for k , v in regular_occurance.items():
            freq[k] = v / float( sum([value for key, value in regular_occurance.items() if (key[0] == k[0]) and (key[1] == k[1])]))
        
        for k , v in word_ending_occurances.items():
            freq[k] = v / float( sum([value for key, value in word_ending_occurances.items() if k[0] == key[0]]))
    
    return freq
    
    
    


# In[314]:

def execute_three(freq):
    last_key = None
    cum_value = 0.0
    
    for key in sorted({k for k in freq.keys() if k[2] != ' '}):
        if (last_key != None) and (last_key[0] != key[0]  or last_key[1] != key[1]):
            cum_value = 0.0
        
        cum_value += freq[key]
        
        cum_value = roundoff(cum_value)
        
        freq[key] = cum_value
        last_key = key
    
    last_key = None
    cum_value = 0.0
    
    for key in sorted({k for k in freq.keys() if k[2] == ' '}):
        if (last_key != None) and (last_key[0] != key[0]):
            cum_value = 0.0
        
        cum_value += freq[key]
        
        cum_value = roundoff(cum_value)
        
        freq[key] = cum_value
        last_key = key
    
    return freq
    
    


# ## Random Number Gen
# 

# In[315]:


# In[317]:

def get_starting_letter(pair_cum_prob):
    rand = random.random()
    
    return sorted( [ key for key, value in pair_cum_prob.items() if key[0] == " " and key[1] != " " and value >= rand])[0][1]
    
    


# In[318]:

def get_next_letter(first_letter, second_letter, trip_cum_prob, pair_cum_prob):
    rand = random.random()
    trip_list = sorted([key for key, value in trip_cum_prob.items() if key[0] == first_letter and key[1] == second_letter and key[2] != ' ' and value >= rand])
    if(len(trip_list)):
        return trip_list[0][2]
    
    pair_list = sorted([key for key, value in pair_cum_prob.items() if key[1] == second_letter and key[0] != ' ' and value >= rand])
    if(len(pair_list)):
        return pair_list[0][1]
   
    return get_starting_letter(pair_cum_prob)
        


# In[319]:

def get_last_letter(current_last, sec_to_last, trip_cum_prob, pair_cum_prob ):
    rand = random.random()
    
    trip_list = sorted([key for key, value in trip_cum_prob.items() if key[0] == current_last  and key[2] == ' ' and value >= rand])
    if(len(trip_list)):
        return trip_list[0][1]
    
    valid_letters = {k[0] for k in trip_cum_prob.keys() if k[2] == ' '}
    pair_list = sorted([key for key, value in pair_cum_prob.items() if (key[0] == current_last) and (key[1] in valid_letters) and (value >= rand)])
    if(len(pair_list)):
        new_last = pair_list[0][1]
        return new_last + get_last_letter(new_last, sec_to_last, trip_cum_prob, pair_cum_prob)

    return get_next_letter(current_last, sec_to_last, trip_cum_prob, pair_cum_prob)
    


# In[320]:

def generate_name(inputt, trip_cum_prob, pair_cum_prob):
    name = " " + get_starting_letter( pair_cum_prob)
    
    for i in range(get_length(inputt) -2):
        name += get_next_letter(name[-2], name[-1], trip_cum_prob, pair_cum_prob)
        
    name += get_last_letter(name[-1], name[-2], trip_cum_prob, pair_cum_prob)
    return name.strip().capitalize()
    

def main(argv):
    file_path = argv[1]
    name_file = open(file_path, "r")
    
    line =  name_file.readline()
    
    name_file.close()
    
    line = re.sub(r'[^a-zA-Z\s=]','', line).replace('\n', ' ').replace("'", " ").replace('\xa0','').lower()
    
    line = line.split()

    line = [l for l in line if len(l) > 2]
    line = ' '  + ' '.join(line) + ' '
   

    trip_cum_prob = execute_three(create_fequencies_three(line))

    pair_cum_prob = execute_two(create_fequencies_two(line))

    for i in range(50):
        print(generate_name(line, trip_cum_prob, pair_cum_prob))



if __name__ == "__main__":
   main(sys.argv)
