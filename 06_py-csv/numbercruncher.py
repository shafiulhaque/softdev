'''
Awesome Sharks :: Shafiul Haque, Ameer Alnasser
SoftDev pd08
K06 -- Divine your Destiny
2022-10-02
time spent: 0.5hrs
DISCO:
    *figured out how to go through each element in a dictionary 
    *figured out typecasting between string and integer values
    *figured out general solution for returning a random occupation
QCC:
    *what happens if a key in a dictionary wants to hold two different values?
    *is there a built in function to weigh different values randomly?
HOW THIS SCRIPT WORKS:
    1. open the csv file and read it in as a txt
    2. read the occupations and values into a dictionary
    3. go through each occupation and mulitiply the percentage value by 10
    4. put the occupation in a list as many times as the percentage value multiplied by 10
    5. choose a random value between the range of the list
    6. use the value to return occupation and percentage
'''

import csv
import random as rng

def filereader():
    file1 = open("occupations.csv",'r')
    file1.readline()
    sha= file1.readlines()
    sha = sha[:-1]
    dictionary = {}
    for e in sha:
        if e[0] == '"':
            dictionary[e[1:e.find('",')]] = float(e[e.find('",')+2:len(e)-1])
        else:
            dictionary[e[0:e.find(',')]] = float(e[e.find(',')+1:len(e)-1])
    return dictionary

def occupation(dic):
    occlist = []
    for key in dic:
        number = int((dic[key])*10)
        for x in range(number):
            occlist.append(key)
    index = rng.randint(0, len(occlist)-1)
    return "Your randomly selected occupation is " + occlist[index] + " with a " + str(dic[occlist[index]]) + "% chance."
        
print(occupation(filereader()))