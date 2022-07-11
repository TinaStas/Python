def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def new_calculation():
    num1=int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation: ")
        num2=int(input("What's the next number?: "))
        calculation_function=operations[operation_symbol]
        res=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {res}")
        question=input(f"Type \"y\" to coninue calculating with {res}, or type \"n\" to start a new calculation:\n")
        if question == 'n':
            should_continue=False
            new_calculation()
        else:
            first_number = res
