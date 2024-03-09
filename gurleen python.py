def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "error!"
    return x/y
def calculator():
    history=[]

    while True:
        print("function:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.view history")
        print("6.Exit")

        choice = input ("Enter choice:1,2,3,4,5,6")


        if choice in ('1','2','3','4',):        
            num1=float(input("enter first number:"))
            num2=float(input("enter second number"))
            if choice == '1':
               result = add(num1,num2)
               print("Result:", result)
               history.append((num1,'+',num2 ,'=', result))

            elif choice == '2':
               result = add(num1,num2)
               print("Result:", result)
               history.append((num1,'+',num2 ,'=', result))

            elif choice == '3':
               result = add(num1,num2)
               print("Result:", result)
               history.append((num1,'+',num2, '=', result))

            elif choice == '4':
               result = add(num1,num2)
               print("Result:", result)
               history.append((num1,'+',num2, '=', result))

        
        elif choice == '5':
            if not history:
                print("history is empty")
            else:
                print("calculation history:")
                for entry in history:
                    print(entry)
        elif choice == '6':
            print("Exiting calculator. Goodbye!")
            break

            
        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculator()