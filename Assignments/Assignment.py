
def intro():
    #This try block is to handle the exception for Choose
    try:
        choose = int(input("Enter the choice of operation you want to do\n############################################# \n1.Add \n2.Sub \n3.Multiply \n4.Divide \n5.Remainder \n6.Power"))
        
        if choose in (1,2,3,4,5,6):
            #This try block is to handle the exception for values a and b
            try:
                a=float(input("Enter the first number: "))
                b=float(input("Enter the second number: "))
            except ValueError:
                print("Please Enter numerical values only")
                print("==================================\n")
                intro()
                
            if choose == 1:
                addition(a,b)
                
            elif choose == 2:
                substraction(a,b)
                
            elif choose == 3:
                multiplication(a,b)
                
            elif choose == 4:
                division(a,b)
                
            elif choose == 5:
                percentile(a,b)
                    
            elif choose == 6:
                power(a,b)
            
            calculate_again()        
                
        else:
            print("\nPlease Choose the values that are listed only")
            print("______________________________________________\n")
            calculate_again()
            
    except ValueError:
        print("\nPlease Choose the values that are listed only")
        print("______________________________________________\n")
        intro()
                
def calculate_again():
    proceed = input("\nTo continue enter any key else N for discontinue")
    if proceed.upper()=="N":
        print("Thanks for using")
            
    else:
        intro()
    

def addition(value1,value2):
    add = value1+value2
    print(add)
    
def substraction(value1,value2):
    sub = value1-value2
    print(sub)
    

def multiplication(value1,value2):
    mul = value1*value2
    print(mul)

def division(value1,value2):
    try:
        div = value1/value2
        print(div)
        
    except ZeroDivisionError:
        print("Zero division is not possible")  

def percentile(value1,value2):
    try:
        percent = value1%value2
        print(percent)
        
    except ZeroDivisionError:
        print("Denominator cannot be Zero")

def power(value1,value2):
    pow = value1**value2
    print(pow)

if __name__=="__main__":
    print("Welcome to console python calculator")
    print("------------------------------------\n")
    intro()