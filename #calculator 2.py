#addition
def add(x, y): 
    return x + y

# subtraction 
def subtract(x, y):
    return x - y

#multiplication 
def multiply(x, y):
    return  x * y 

#division
def divide(x, y):
    return x / y 

print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    #take input from user 
    choice = input ("enter choice (1/2/3/4): ")

    #check if choice is one of the four functions
    if choice in ('1', '2', '3', '4'):
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))

        if choice =='1':
            print(a, "+", b, "=", add(a,b))
        elif choice =='2':
            print(a, "-", b, "=", subtract(a,b))
        elif choice =='3':
            print(a, "*", b, "=", multiply(a,b))
        elif choice =='4':
            print(a, "/", b, "=", divide(a,blue))

        #check if user wants another operation 
        #break the while loop if answer is no
        next_calculation = input ("let's do next calculation? (yes/no): ")
        if next_calcutaion == "no":
            break

    else:
            print("invalid input")
    

    


