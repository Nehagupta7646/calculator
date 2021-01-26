
def calc():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplicatin")
        print("4. Division")
        print("5. Power of Num1 to Num2")
        print("6. Square Root")
        print("7. CubeRoot")
        print("8. Exit")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            n1 = float(input("Enter no1: "))
            n2 = float(input("Enter no2: "))
            res = n1 + n2
            res = float(res)
            print(f"The addition of {n1} and {n2} is {res}")
        elif opt == 2:
            n1 = float(input("Enter no1: "))
            n2 = float(input("Enter no2: "))
            res = n1 - n2
            res = float(res)
            print(f"The subtraction of {n1} and {n2} is {res} ")
        elif opt == 3:
            n1 = float(input("Enter no1: "))
            n2 = float(input("Enter no2: "))
            res = n1 * n2
            res = float(res)
            print(f"The multiply of {n1} and {n2} is {res}")
        elif opt == 4:
            n1 = float(input("Enter no1: "))
            n2 = float(input("Enter no2: "))
            res = n1 / n2
            res = float(res)
            print(f"The division {n1} and {n2} is {res} ")
        elif opt == 5:
            n1 = float(input("Enter no1: "))
            n2 = float(input("Enter no2: "))
            res = n1 ** n2
            res = float(res)
            print(f"The power of {n1} on {n2} is {res} ")
        elif opt == 6:
            n1 = float(input("Enter no1: "))
            res = (n1 ** (1/2))
            res = float(res)
            print(f"The squareRoot of {n1} is {res} ")
        elif opt == 7:
            n1 = float(input("Enter no1: "))
            res = (n1 ** (1/3))
            res = float(res)
            print(f"The cuberoot of {n1} is {res} ")
        elif opt == 8:
            print("Thank you for using my CalCulator.") 
            break
        else:
            print("Please Enter valid key!..")
        ch = input("press E to Exit and C key to continue: ")
        if ch in 'Ee':
            print("Thank you for using my CalCulator.")
            exit()
        elif ch in 'Cc':
            continue

print("************ You have some option to perform Arithmatic operations ********************")     
calc()