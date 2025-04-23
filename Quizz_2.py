#!/usr/bin/env python
# coding: utf-8

# worksshop 2
# Dr Andrew Tedder

# In[46]:


#Question one

import os
# first create an empty list list
my_list = []

#import our fasta file to work with
input_file = 'C:/Users/ALIEU CSAY/Downloads/workshop_data.fasta'

# 1. we open the file
# 2. isolate the headers 
# 3. append/add the headers to our empty list
# 4. print the list

with open(input_file, 'r') as file:
    for line in file:
        if line.startswith('>'):
            headers = line.lstrip('>')
            my_list.append(headers)
print(my_list)


# In[64]:


#Question two
# sorting ALphabetically and numbering the sorted list

#initiat the count 
count = 1 

# create a range from start of the list to the length of the list, with one step.
# sort the list with index of the range. 
# print the count and the sorted list. 

for x in range(0, len(my_list), 1):
    print(count, sorted(my_list)[x])
    count = count + 1
    
#print(sort_header)


# In[112]:


#Question Threee 

# create an empty dictionary
my_dict = {}

# 1. open the file. 
# 2. iterate through the lines. 
# 3. we use an if and else statement to get our headers and the sequence. 
# 4. attach both to a variable. 
# 5. add to a dictionary.
# 6. print your dictionary 

with open(input_file, 'r') as file:
    for lines in file:
        lines = lines.strip()
        if lines.startswith('>'):
            my_headers = lines
            
        else:
            my_seq = lines
            my_dict[my_headers] = my_seq

print(my_dict)


# In[92]:


# Question Four 

# create a function to hold our dictionary argument

def my_workshop(file):
    my_dict = {}
    '''Creating a dictionary for my fasta file, to hold headers as KEYS and sequences as VALUES......lets seeeee '''
    with open(input_file, 'r') as file:
        for lines in file:
            lines = lines.strip()
            if lines.startswith('>'):
                my_headers = lines   
            else:
                my_seq = lines
                my_dict[my_headers] = my_seq
    return my_dict

# we call the function and attach it to a varible 
# print the variable
A_seq = my_workshop(input_file)
print(A_seq)


# In[111]:


# printing values for only a perticular key in my_dict

my_dict['>AT1G04130.1_pop1_+_m']


# In[108]:


# Question Five

# 1. iterate through keys of the dectionary in the function to call/print values.

for keys in my_workshop(input_file).keys():
    print(my_workshop(input_file)[keys])


# In[ ]:




