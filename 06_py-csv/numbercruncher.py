'''
Charles's Angels::Aleksandra Shifrina, Nakib Abedin, Ameer Alnasser
SoftDev pd08
K04 -- RNG + Dictionaries
2022-09-22
time spent: 0.5hrs
DISCO:
    *figured out that .keys() returns all keys of a dictionary  
    *figured out typecasting. ex: int(4.0)
    *figured out general solution for returning a random devo 
QCC:
    *will the final dictionary work with our code?
    *how do we ensure that the code will completely randomly chose a devo?
OPS Summary:
    1. gather all keys from dictionary in a list, keys
    2. pick a random index using length of list
    3. retrieve key from list
    4. generate a random element from list associated with key
    5. return random devo
'''

import csv

def filereader():
    file1 = open("occupations.csv",'r')
    file1.readline()
    sha= file1.readlines()
    sha = sha[:-1]
    dictionary = {}
    for e in sha:
        if e[1] == '"'
        dictionary.append(e[:e.find(
    return sha

print(filereader())