#This is a program to calculate the area of the following shapes: Triangle,
#circle, square, rectangle, trapezoid, rhombus, parallelogram and elipse.t

from math import * #imports a special library to use pi

#our functions are written at the top of the program
def circle(radiusc):
    print("Your circle's area is", pi * radiusc ** 2)

def square(sidesq):
    print("Your square has an area of:",sidesq*sidesq)

def triangle(baset, heightt):
    print("your triangle has an area of:",baset/2*heightt)

def rectangle(widthr, heightr):
    print("your rectangle has an area of:",widthr*heightr)

def trapezoid(toptr, bottomtr, heighttr):
    print("your trapezoid has an area of:",(toptr+bottomtr)/2*(heighttr))

def rhombus(diagonal1, diagonal2):
    print("your rhombus has an area of:",(diagonal1*diagonal2)/2)

def parallelogram(basep, heightp):
    print("your parrallelogram has an area of:",basep*height)

def elipse(axis1, axis2):



#main function is the main menu  of the program
def main():
    print("Welcome to my area calculator")
    end = "no"
    while end != "yes": #conditional loop to keep the program running until user exits
        print("please choose a shape to calculate the area for:") #triple quotes allow us to write on many lines
        print("""1 for circle
2 for square
3 for triangle
4 for rectangle
5 for trapezoid
6 for rhombus
7 for parallelogram
8 for elipse""")
        # choice for decisions below
        choice = int(input("Choice: "))
        if choice == 1:
            radiusc = int(input("what is your circle radius? "))
            circle(radiusc)
        elif choice == 2:
            sidesq = int(input("What is the length of your side: "))
            square(sidesq)
        elif choice == 3:
            baset = int(input("what is your base size? "))
            heightt = int(input("What is your height size? "))
            triangle(baset, heightt)
        elif choice == 4:
             widthr = int(input("what is your width size? "))
             heightr = int(input("what is your height size? "))
             rectangle(widthr, heightr)
        elif choice == 5:
            toptr = int(input("what is your top number? "))
            bottomtr = int(input("what is your bottom number? "))
            heighttr = int(input("what is your height? "))
            trapezoid(toptr, bottomtr, heighttr)
        elif choice == 6:
            diagonal1 = int(input("what is your first diagonal number? "))
            diagonal2 = int(input("what is your second diagonal number? "))
            rhombus(diagonal1, diagonal2)
        elif choice == 7:
            basep = int(input("what is your base size? "))
            heightp = int(input("what is your height size? "))
            parallelogram(basep, heightp)
        elif choice == 8:
            print("elipse")
        else:
            print("Invalid choice")

        end = input("Do you wish to end? ").lower()
    print("Thanks for using my program")

main()
            
                          

