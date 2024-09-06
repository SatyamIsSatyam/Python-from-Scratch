print("Welcome to the calculation saga")
print("Choose your option")
print("1. +")
print("2. -")
print("3. *")
print("4. /")


def add():
    A=int(input("num1:"))
    B=int(input("num2:"))
    S= A+B
    print("A+B is your required sum",S)
      
def sub():
    A=int(input("num1:"))
    B=int(input("num2:"))
    F= A-B
    print("A-B is your required sum",F)

def mul():
    A=int(input("num1:"))
    B=int(input("num2:"))
    M= A*B
    print("A*B is your required sum",M)

def div():
    A=int(input("num1:"))
    B=int(input("num2:"))
    D=A/B
    print("A/B is your required sum",D)

calc=int(input("-->>"))



if calc== 1:
    add()
elif calc== 2:
    sub()
elif calc== 3:
    mul()
elif calc== 4:
    div()
else:
    print("Incorrect option")

      
      
      
