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
# imported csv to read file, rng in the later function

def filereader():
    file1 = open("occupations.csv",'r')
    file1.readline()
    sha= file1.readlines() #skip first line bc it just has the headings, which aren't necessary
    sha = sha[:-1]
    dictionary = {} #make dictionary
    for e in sha: #two cases, if a string has " " remove it after the quotes are finished, if a string is ' ' remove it after the , is done
        if e[0] == '"':
            dictionary[e[1:e.find('",')]] = float(e[e.find('",')+2:len(e)-1])
        else:
            dictionary[e[0:e.find(',')]] = float(e[e.find(',')+1:len(e)-1])
    return dictionary

def occupation(dic):
    occlist = [] #make a list that should be filled with 998 values depending on the percentage chance of the occupation
    for key in dic: # go through each occupation
        number = int((dic[key])*10) #multiply by 10 to get a int value
        for x in range(number):
            occlist.append(key) #add the value to the occlist
    index = rng.randint(0, len(occlist)-1) #generate a random value that would be an index in the occlist
    return "Your randomly selected occupation is " + occlist[index] + " with a " + str(dic[occlist[index]]) + "% chance." #return occupation and chance
        
print(occupation(filereader()))