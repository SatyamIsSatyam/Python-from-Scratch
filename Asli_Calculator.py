print("Welcome to the calculation saga")
print("Choose your option")
print("1. +")
print("2. -")
print("3. *")
print("4. /")


def add():
    S = 0
    n = int(input("How many nums: "))
    for i in range(n):
        A=int(input(f"num{i+1}: "))
        S += A
    print("Sum of all is your required sum",S)
      
def sub():
    F = 0
    n = int(input("How many nums: "))
    for i in range(n):
        A=int(input(f"num{i+1}: "))
        if i==0:
            F += A
        else:
            F -= A
    print("Difference is your required diff",F)
def mul():
    M = 0
    n = int(input("How many nums: "))
    for i in range(n):
        A=int(input(f"num{i+1}: "))
        M *= A
    print("Multiplication is:",M)
def div():
    D = 0
    n = int(input("How many nums: "))
    for i in range(n):
        A=int(input(f"num{i+1}: "))
        if i == 0:
            D = A
        else:
            D /= A
    print("Division is: ",D)
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

      
      
      
