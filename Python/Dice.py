import random as r
import os
import sys

rolls = []

class dice:
    def __init__(self,sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = r.randrange(1,self.sides+1)

def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False



def main():
    print("Welcome to my dice roller!")
    choice = input("""What would you like to do?:
1. D4
2. D6
3. D8
4. D10
5. D12
6. D20
7. Any sided Dice
8. See previous roll
""")
    if checkInt(choice) == True:
        os.system('cls')
        choice = int(choice)
        if choice == 1:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                number = int(number)
                for x in range(number):
                    d4 = dice(4)
                    d4.roll()
                    print(d4.value)
                    rolls.append(d4.value)
                repeat = input("Would you like to go again? (y/n): ")
                if repeat == "y":
                    os.system('cls')
                    main()
                else:
                    sys.exit()
            else:
                print("ERROR")
                os.system('cls')
                main()

        if choice == 2:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                number = int(number)
                for x in range(number):
                    d6 = dice(6)
                    d6.roll()
                    print(d6.value)
                    rolls.append(d6.value)
                repeat = input("Would you like to go again? (y/n): ")
                if repeat == "y":
                    os.system('cls')
                    main()
                else:
                    sys.exit()
            else:
                print("ERROR")
                os.system('cls')
                main()
                
        if choice == 3:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                number = int(number)
                for x in range(number):
                    d8 = dice(8)
                    d8.roll()
                    print(d8.value)
                    rolls.append(d8.value)
                repeat = input("Would you like to go again? (y/n): ")
                if repeat == "y":
                    os.system('cls')
                    main()
                else:
                    sys.exit()
            else:
                print("ERROR")
                os.system('cls')
                main()

        if choice == 4:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                number = int(number)
                for x in range(number):
                    d10 = dice(10)
                    d10.roll()
                    print(d10.value)
                    rolls.append(d10.value)
                repeat = input("Would you like to go again? (y/n): ")
                if repeat == "y":
                    os.system('cls')
                    main()
                else:
                    sys.exit()
            else:
                print("ERROR")
                os.system('cls')
                main()
                
        if choice == 5:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                number = int(number)
                for x in range(number):
                    d12 = dice(12)
                    d12.roll()
                    print(d12.value)
                    rolls.append(d12.value)
                repeat = input("Would you like to go again? (y/n): ")
                if repeat == "y":
                    os.system('cls')
                    main()
                else:
                    sys.exit()
            else:
                print("ERROR")
                os.system('cls')
                main()

        if choice == 6:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                number = int(number)
                for x in range(number):
                    d20 = dice(20)
                    d20.roll()
                    print(d20.value)
                    rolls.append(d20.value)
                repeat = input("Would you like to go again? (y/n): ")
                if repeat == "y":
                    os.system('cls')
                    main()
                else:
                    sys.exit()
            else:
                print("ERROR")
                os.system('cls')
                main()

        if choice ==7:
            rolls.clear()
            number = input("How many times would you like to roll the dice?: ")
            if checkInt(number) == True:
                os.system('cls')
                number2 = input("How many sides are on the dice?: ")
                if checkInt(number2) == True:
                    number = int(number)
                    number2 = int(number2)
                    for x in range(number):
                        dr = dice(number2)
                        dr.roll()
                        print(dr.value)
                        rolls.append(dr.value)
                    repeat = input("Would you like to go again? (y/n): ")
                    if repeat == "y":
                        os.system('cls')
                        main()
                    else:
                        sys.exit()
                else:
                    print("ERROR")
                    os.system('cls')
                    main()
            else:
                print("ERROR")
                os.system('cls')
                main()

        elif choice == 8: 
            for i in rolls:
                print(i)
            repeat = input("Would you like to go again? (y/n): ")
            if repeat == "y":
                os.system('cls')
                main()
            else:
                sys.exit()

        else:
            print("Answer not found!")
            main()
    else:
        print("ERROR")
        os.system("cls")
        main()

main()
                   


