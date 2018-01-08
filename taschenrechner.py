#Den Code von dem Taschenrechner in Scratch findet ihr hier: http://bit.ly/2AGXiG9 
#oder zum Download: http://bit.ly/2s8MvDm

import time
while True:
    print("\n")
    num1=input("1. Zahl: ")
    ra=input("Rechenart: ")
    num2=input("2. Zahl: ")

    num1=int(num1)
    num2=int(num2)

    if ra == "+":
        print("Das Ergebnis lautet: ", num1+num2)
    elif ra == "-":
        print("Das Ergebnis lautet: ", num1-num2)
    elif ra == "*":
        print("Das Ergebnis lautet: ", num1*num2)
    elif ra == "/":
        print("Das Ergebnis lautet: ", num1/num2)
