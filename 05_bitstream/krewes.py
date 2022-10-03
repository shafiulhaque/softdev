'''
Awesome Sharks :: Shafiul Haque, Ameer Alnasser
SoftDev pd08
K05 -- bitstream
2022-09-29
time spent: 0.5hrs
DISCO:
    * python/thonny's output has a certain character limit
    * file.readline() would read the line of code
    * there cannot exist two functions of same name
    * .find() returns the first index of the parameter
    * we can append dictionaries
QCC:
    * why can python not have two functions with same name?
    * how ensure randomness?
'''

import random as rng

#krewes = {1:['A', 'B', 'C'], 2:['D', 'E', 'F']}
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }
look="2$$$Daniel$$$Porky@@@2$$$Maya$$$Logan@@@7$$$Sam$$$Otto@@@2$$$Anthony$$$Bart@@@2$$$Aaron$$$munchy@@@7$$$Nada$$$Ray@@@7$$$Jeremy$$$Parky@@@8$$$Wilson$$$bear@@@2$$$Talia$$$Dname@@@8$$$Shreya$$$Bob@@@8$$$Kevin$$$Bob@@@8$$$Verit$$$Nibbles@@@8$$$Shinji$$$Will Smith@@@8$$$Brian$$$Duc@@@8$$$Donald$$$Klein@@@8$$$Sebastian$$$Deno@@@2$$$Ryan$$$<T>@@@8$$$Brian$$$Dolphin@@@8$$$Jeffery$$$Mathias@@@7$$$William$$$Steve@@@2$$$Julia$$$Poof@@@8$$$Aahan$$$Spikes@@@7$$$Gitae$$$Kwak@@@7$$$James$$$Steve@@@7$$$Lauren$$$wagyu@@@2$$$William$$$cs50 ddb@@@2$$$Samuel$$$Arnold@@@2$$$Anson$$$Faizem@@@7$$$David$$$Eugene@@@7$$$Samantha$$$Tim@@@7$$$Anna$$$Flippers@@@7$$$Karen$$$Grape@@@7$$$Mahir$$$Nemo@@@2$$$Andrew$$$potatoe@@@8$$$Gordon$$$cheems@@@8$$$Yat Long$$$Reginald@@@2$$$Vansh$$$Berry@@@7$$$Ian$$$hydro@@@8$$$Samson$$$Doggo@@@8$$$April$$$horanghae@@@2$$$Daniel$$$Kosha@@@7$$$Gabriel$$$Moony@@@8$$$Jusin$$$Alfred@@@2$$$Ziying$$$Pinky@@@2$$$Raven$$$Bobby@@@8$$$Ameer$$$turtleboi@@@7$$$Prattay$$$Winnie@@@8$$$Ryan$$$Luigi@@@2$$$Fang Min$$$Cat@@@7$$$Russell$$$Bob 3.0@@@8$$$Erica Li$$$Hugo@@@"

def find_devo(krewes):
    keys = list(krewes)
    index = rng.randint(0, len(keys)-1)
    key = keys[index]
    rando_value = rng.randint(0, len(krewes[key])-1)
    return str("Your random devo is "+str(krewes[key][rando_value][0]) + " of period " + str(key))+ ". Their ducky is "+str(krewes[key][rando_value][1])

def decipher(look):
    dict={2:[],7:[],8:[]}
    sha=look
    while len(sha)>1:
        key=int(sha[0:sha.find("$")])
        sha = sha[sha.find("$")+3:]
        name = sha[:sha.find("$")]
        sha = sha[sha.find("$")+3:]
        ducky = sha[:sha.find("@")]
        sha = sha[sha.find("@")+3:]
        dict[key].append([name, ducky])
    return dict

def decipher2():
    dict={2:[],7:[],8:[]}
    file1 = open("krewes.txt",'r')
    sha=str(file1.readline())

    while len(sha)>1:
        key=int(sha[0:sha.find("$")])
        sha = sha[sha.find("$")+3:]
        name = sha[:sha.find("$")]
        sha = sha[sha.find("$")+3:]
        ducky = sha[:sha.find("@")]
        sha = sha[sha.find("@")+3:]
        dict[key].append([name, ducky])
    return dict
def decipher(look):
    dict={2:[],7:[],8:[]}
    sha=look

    while len(sha)>1:
        key=int(sha[0:sha.find("$")])
        sha = sha[sha.find("$")+3:]
        name = sha[:sha.find("$")]
        sha = sha[sha.find("$")+3:]
        ducky = sha[:sha.find("@")]
        sha = sha[sha.find("@")+3:]
        dict[key].append([name, ducky])
    return dict


print( decipher2())
print (find_devo(decipher2()))
print (find_devo(decipher(look)))