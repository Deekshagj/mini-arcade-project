import random
def flip():
    print("Toss a coin")
if __name__=="__main__": 
    while True:
        result=0
        computer=random.randint(1,2)
        choice=int(input("Enter your choice\n1.Head\n2.Tails\n3.Exit\n"))
        if computer==1:
            result=1
        elif computer==2:
            result=2
            
        if choice==result:
            print('\t',"Congo!! You won",'\n')
        elif choice == 3:
            exit()    
        else:
            print('\t',"Sorry! You lost",'\n')
        

print("Thank You for playing!")
