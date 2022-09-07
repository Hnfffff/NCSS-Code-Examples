from random import *
import time
from os import system

def exit():
    end = input("would you like to end?")
    
def addition():
    addcorrect = 0
    addnumber1 = int(input("What is the first number of the first range?: "))
    system("cls")
    addnumber2 = int(input("What is the second number of the first range?: "))
    system("cls")
    addnumber3 = int(input("What is the first number of the second range?: "))
    system("cls")
    addnumber4 = int(input("What is the second number of the second range?: "))
    system("cls")
    addquestionnum = int(input("How many Questions?: "))
    system("cls")
    for i in range(addquestionnum):
        adda = randrange(addnumber1, addnumber2)
        addb = randrange(addnumber3, addnumber4)
        addanswer = adda+addb
        print(f"{adda}+{addb}")
        adduser = int(input("="))
        if adduser == addanswer:
            print("Correct!")
        else:
            print("Wrong!")
            addcorrect = addcorrect + 1
        time.sleep(0.5)
        system("cls")
    print(f"You got {addcorrect} wrong!")
    time.sleep(0.5)
    system("cls")
    main()
        
    

def subtraction():
    subcorrect = 0
    subnumber1 = int(input("What is the first number of the first range?: "))
    system("cls")
    subnumber2 = int(input("What is the second number of the first range?: "))
    system("cls")
    subnumber3 = int(input("What is the first number of the second range?: "))
    system("cls")
    subnumber4 = int(input("What is the second number of the second range?: "))
    system("cls")
    subquestionnum = int(input("How many Questions?: "))
    system("cls")
    for i in range(subquestionnum):
        suba = randrange(subnumber1, subnumber2)
        subb = randrange(subnumber3, subnumber4)
        subanswer = adda-addb
        print(f"{suba}-{subb}")
        subuser = int(input("="))
        if subuser == subanswer:
            print("Correct!")
        else:
            print("Wrong!")
            subcorrect = subcorrect + 1
        time.sleep(0.5)
        system("cls")
    print(f"You got {addcorrect} wrong!")
    time.sleep(0.5)
    system("cls")
    main()

def multiplacation():
    mutlicorrect = 0
    multinumber1 = int(input("What is the first number of the first range?: "))
    system("cls")
    multinumber2 = int(input("What is the second number of the first range?: "))
    system("cls")
    multinumber3 = int(input("What is the first number of the second range?: "))
    system("cls")
    multinumber4 = int(input("What is the second number of the second range?: "))
    system("cls")
    multiquestionnum = int(input("How many Questions?: "))
    system("cls")
    for i in range(multiquestionnum):
        multia = randrange(multinumber1, multinumber2)
        multib = randrange(multinumber3, multinumber4)
        multianswer = multia*multib
        print(f"{multia}*{multib}")
        multiuser = int(input("="))
        if multiuser == multianswer:
            print("Correct!")
        else:
            print("Wrong!")
            multicorrect = multicorrect + 1
        time.sleep(0.5)
        system("cls")
    print(f"You got {multicorrect} wrong!")
    time.sleep(0.5)
    system("cls")
    main()

def division():
    divcorrect = 0
    divnumber1 = int(input("What is the first number of the first range?: "))
    system("cls")
    divnumber2 = int(input("What is the second number of the first range?: "))
    system("cls")
    divnumber3 = int(input("What is the first number of the second range?: "))
    system("cls")
    divnumber4 = int(input("What is the second number of the second range?: "))
    system("cls")
    divquestionnum = int(input("How many Questions?: "))
    system("cls")
    for i in range(divquestionnum):
        diva = randrange(divnumber1, divnumber2)
        divb = randrange(divnumber3, divnumber4)
        divanswer = diva/divb
        print(f"{diva}÷{divb}")
        divuser = float(input("="))
        if divuser == divanswer:
            print("Correct!")
        else:
            print("Wrong!")
            divcorrect = divcorrect + 1
        time.sleep(0.5)
        system("cls")
    print(f"You got {divcorrect} wrong!")
    time.sleep(0.5)
    system("cls")
    main()

def timestables():
    timescorrect = 0
    timesnumber1 = int(input("What timestables do you want to do?: "))
    system("cls")
    timesquestionnum = int(input("How many Questions?: "))
    system("cls")
    for i in range(timesquestionnum):
        timesa = timesnumber1
        timesb = randrange(1,13)
        timesanswer = timesa*timesb
        print(f"{timesa}*{timesb}")
        timesuser = int(input("="))
        if timesuser == timesanswer:
            print("Correct!")
        else:
            print("Wrong!")
            timescorrect = timescorrect + 1
        time.sleep(0.5)
        system("cls")
    print(f"You got {timescorrect} wrong!")
    time.sleep(0.5)
    system("cls")
    main()

def mixed():
    mixcorrect = 0
    mixnumber1 = int(input("What is the first number of the first range?: "))
    system("cls")
    mixnumber2 = int(input("What is the second number of the first range?: "))
    system("cls")
    mixnumber3 = int(input("What is the first number of the second range?: "))
    system("cls")
    mixnumber4 = int(input("What is the second number of the second range?: "))
    system("cls")
    mixquestionnum = int(input("How many Questions?: "))
    system("cls")
    for i in range(mixquestionnum):
        symbol = randrange(1,5)
        if symbol == 1:
            mixa = randrange(mixnumber1, mixnumber2)
            mixb = randrange(mixnumber3, mixnumber4)
            mixanswer = mixa/mixb
            print(f"{mixa}÷{mixb}")
            mixuser = float(input("="))
            if mixuser == mixanswer:
                print("Correct!")
            else:
                print("Wrong!")
                mixcorrect = mixcorrect + 1
            time.sleep(0.5)
            system("cls")
        if symbol == 2:
            mixa = randrange(mixnumber1, mixnumber2)
            mixb = randrange(mixnumber3, mixnumber4)
            mixanswer = mixa*mixb
            print(f"{mixa}x{mixb}")
            mixuser = int(input("="))
            if mixuser == mixanswer:
                print("Correct!")
            else:
                print("Wrong!")
                mixcorrect = mixcorrect + 1
            time.sleep(0.5)
            system("cls")
        if symbol == 3:
            mixa = randrange(mixnumber1, mixnumber2)
            mixb = randrange(mixnumber3, mixnumber4)
            mixanswer = mixa+mixb
            print(f"{mixa}+{mixb}")
            mixuser = int(input("="))
            if mixuser == mixanswer:
                print("Correct!")
            else:
                print("Wrong!")
                mixcorrect = mixcorrect + 1
            time.sleep(0.5)
            system("cls")
        if symbol == 4:
            mixa = randrange(mixnumber1, mixnumber2)
            mixb = randrange(mixnumber3, mixnumber4)
            mixanswer = mixa-mixb
            print(f"{mixa}-{mixb}")
            mixuser = int(input("="))
            if mixuser == mixanswer:
                print("Correct!")
            else:
                print("Wrong!")
                mixcorrect = mixcorrect + 1
            time.sleep(0.5)
            system("cls")
    print(f"You got {mixcorrect} wrong!")
    time.sleep(0.5)
    system("cls")
    main()
def main():
    userinput = int(input(""")What do you want to do?
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Timestables
6) Mix
:"""))
    if userinput == 1:
        system("cls")
        addition()
    elif userinput == 2:
        system("cls")
        subtraction()
    elif userinput == 3:
        system("cls")
        multiplacation()
    elif userinput == 4:
        system("cls")
        division()
    elif userinput == 5:
        system("cls")
        timestables()
    elif userinput == 6:
        system("cls")
        mixed()
    else:
        print("Invalid option!")
        system("cls")
        main()
main()
    

