a,b = input("Enter two numbers sperated with space: ").split()
lst = ["+","-","/","*","%","**","//",">=","<=",">","<","!="]
for operator in lst:
    result = eval(a + operator + b)
    print(f"{a} {operator} {b} = {result}")