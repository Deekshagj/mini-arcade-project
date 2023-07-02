import random 
x = "y"
while x == "y": 
    no = random.randint(1,6) 
    if no == 1: 
        print(" _____") 
        print("|     |") 
        print("|     |")
        print("|  0  |")
        print("|     |") 
        print("|_____|") 
    if no == 2: 
        print(" _____") 
        print("|     |") 
        print("| 0   |") 
        print("|   0 |") 
        print("|_____|") 
    if no == 3: 
        print(" _____") 
        print("|0    |") 
        print("|     |")
        print("|  0  |")
        print("|     |") 
        print("|____0|") 
    if no == 4: 
        print(" _____") 
        print("|0   0|") 
        print("|     |")
        print("|     |")
        print("|0___0|") 
    if no == 5: 
        print(" _____") 
        print("|0   0|") 
        print("|     |")
        print("|  0  |")
        print("|     |") 
        print("|0___0|")  
    if no == 6: 
        print(" _____") 
        print("|0   0|") 
        print("|     |")
        print("|0   0|")
        print("|     |") 
        print("|0___0|")           
    x=input("press y to roll again and n to exit:") 
    print("\n")


