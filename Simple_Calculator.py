def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print("Select operation to perform")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

while True:
    choice=input("Enter Your choice(1,2,3,4) ? ")
    if choice in ('1','2','3','4'):
        num1=float(input("enter your first number"))
        num2=float(input("Enter your second number"))

        if choice == '1':
            print(num1,"+",num2, "=", add(num1,num2) )

        elif choice == '2':
            print(num1,"-",num2, "=", subtract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2, "=", multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2, "=", division(num1,num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Wrong choice, Please choose a valid option")

