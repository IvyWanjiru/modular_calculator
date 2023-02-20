import operators
import others
import trigonometry
operator=input("enter an operator: ")
if operator =="cube":
    num=eval(input("enter number: "))
    x=others.cube(num)
    print(x)
elif operator =="square":
    num = eval(input("enter number: "))
    x=others.square(num)
    print(x)
elif operator=="sine":
    angle=eval(input("Enter angle in degrees: "))
    sin_of_angle= trigonometry.get_sine(angle)
    print(sin_of_angle)


else:
    num1 = eval(input("enter the first number: "))
    num2= eval(input("enter the second number: "))
    

#x = others.cube(67)
#x=function.add(12,34)
#y=function.subtract(23,12)
#print(x)
#print(y)

#or

#from  operators import add

#x=add(45,67)
#print(x)

    if operator =="+":
        x=operator.add(num1,num2)  
        print(x)
    elif operators =="-":
        x=operators.subtract(num1,num2)
        print(x)
    elif operators =="/":
        x=operators.divide(num1,num2)
        print(x)
    elif operators =="*" or"x" or "X":
        x=operators.multiply(num1,num2)
        print(x)
    else:
        print("invalid operator")

