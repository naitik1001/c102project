#this is a program to make a simple calculator
#this function adds two numbers
def add(x,y):
    return x+y
#this function subtracts two numbers
def subtract(x,y):
    return x-y
#this function multiply two numbers
def multiply(x,y):
    return x*y
#this function divides two numbers
def divide(x,y):
    return x/y
print("Welcome to the calculator")
print("please seect the operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
#this is an infinietly running loop
while True:
    #this choice will acceoth the user's choice
    choice = input("please enter your choice")
    if choice in ('1','2','3','4'):
        number1 = float(input("please enter the first number"))
        number2 = float(input("please enter the second number"))
        if choice =='1':
            
            print(number1,"+",number2, "=" ,add(number1,number2))
        elif choice=='2':
            print(number1,"-",number2,"=",subtract(number1,number2))
        elif choice =='3':
            print(number1,"x",number2,"=",multiply(number1,number2))
        elif choice =='4':
            print(number1,"/",number2,"=",divide(number1,number2))
        next_calculation = input("do you want to do next calculation?if yes type yes or if no type no")
        if next_calculation=="no":
            print("Thanks for using the calculator")
            #it will break the while loop if the answer is no
            break
    else:
        print("invalid input")