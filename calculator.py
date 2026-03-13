import math

num1=int(input("enter number 1"))
num2= int(input("enter number 1"))
operator= input("enter the operator")

if operator== '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator== '/':
    if(num1>num2):    print(num1/num2)
    else:
        print('can not possible')

elif operator== '**':
    print(num1**num2)
elif operator =='%':
    print(num1% num2)
elif operator =='sqrt':
    print(math.sqrt(num1+num2))
else:
    print("enter correct operator")