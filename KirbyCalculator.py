#Name:Trevon Harris
#Purpose:Project
#Date:4/24/2018


def options():
    print("Please enter a choice (1. Multiply 2. Divide 3. Substraction 4. Addition 5. Show 6.Quit")




def add(x,y,file):
    total = x + y
    xy = (str(x)+"+"+str(y)+"="+str(total)+"\n")
    file.write(xy)
    return total

def sub(x,y,file):
    total = x - y
    xy = (str(x)+"-"+str(y)+"="+str(total)+"\n")
    file.write(xy)
    return total

def divide(x,y,file):
    total = x / y
    xy = (str(x)+"+"+str(y)+"="+str(total)+"\n")
    file.write(xy)
    return total

def multiply(x,y,file):
    total = x * y
    xy = (str(x)+"+"+str(y)+"="+str(total)+"\n")
    file.write(xy)
    return total

def show(file):
    file = open("myResult.txt file","r")
    print("Your calculation history:\n")
    for info in file:
        print(info)
def kirby():
    print("Have a nice day! <(^.^)> Poyo!")

def main():
    file = open("myResult.txt file","w")
    print("Kirby's handy dandy calculator!")
    options()
    userchoice = ""
    while userchoice != "6":
        userchoice = input("What would you like to do: ")
        if userchoice == "4":
            x = int(input("Please enter a number:"))
            y = int(input("Please enter a number:"))
            print(add(x,y,file))
        elif userchoice == "3":
            x = int(input("Please enter a number:"))
            y = int(input("Please enter a number:"))
            print(sub(x,y,file))
        elif userchoice == "2":
            x = int(input("Please enter a number:"))
            y = int(input("Please enter a number:"))
            print(divide(x,y,file))
        elif userchoice == "1":
            x = int(input("Please enter a number:"))
            y = int(input("Please enter a number:"))
            print(multiply(x,y,file))
        elif userchoice == "5":
            file.close()
            show(file)
            file = open("myResult.txt file","w")
        elif userchoice == "6":
            file.close()
            print("Closing calculator\n")
            kirby()
        else:
            print("Enter a valid command!")
main()

    
