from blocks import *
from logInOut import *
from Play import *
from genre import *
from unfollow import *
from Settings import *
from NewMix import *

i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
p = 0

#NewMix Funcstinality
def recursiveEH6():

    global p

    try:
        Mix()

    except:
        p += 1
        print("#New Mix failures: ",p)
        recursiveEH6()
        

#Block Funcstinality
def recursiveEH5():

    global n

    try:
        block()

    except:
        n += 1
        print("#Block failures: ",n)
        recursiveEH5()

    else:
        recursiveEH6()

#Settings & recepiets Funcstinality
def recursiveEH4():

    global m

    try:
        Settings()

    except:
        m += 1
        print("#Settings failures: ",m)
        recursiveEH4()

    else:
        recursiveEH5()

#follow -unfollow functinality
def recursiveEH3():

    global l

    try:
        unfollow()

    except:
        l += 1
        print("#follow-button failures: ",l)
        recursiveEH3()

    else:
        recursiveEH4()


#Genre testing functinality
def recursiveEH2():

    global k
    
    try:
        testGenre()
                        
    except:
        k += 1
        print("#testGenre failures: ",k)
        recursiveEH2()

    else:
        recursiveEH3()

#play functinality
def recursiveEH1():

    global j

    try:
        play()
                

    except:
        j += 1
        print("#Play failures: ",j)
        recursiveEH1()

    else:
        recursiveEH2()

#Login-out functionality testing 
def recursiveEH():

    global i
    
    try:
        LogInOut()
        

    except:
        
        i += 1
        print("#Log(in-out) failures: ",i)
        recursiveEH()


    else:
        recursiveEH1()
    
                
recursiveEH()

print("number of test failures happend during func 1 testing is: ",i)
print("number of test failures happend during func 2 testing is: ",j)
print("number of test failures happend during func 3 testing is: ",k)
print("number of test failures happend during func 4 testing is: ",l)
print("number of test failures happend during func 5 testing is: ",m)
print("number of test failures happend during func 6 testing is: ",n)
print("number of test failures happend during func 7 testing is: ",p)