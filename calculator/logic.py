from arts import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbols in operations:
        print(symbols)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the seconnd number?: "))

    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")


    should_continue = True

    while should_continue:
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation.: ").lower() == 'y':

            result = answer
            
            operation_symbol = input("Pick an operation: ")
            num3 = float(input("What's the next number?. "))
            answer = operations[operation_symbol](result, num3)
            print(f"{result} {operation_symbol} {num3} = {answer}")
        else:
            calculator()

        
calculator()
