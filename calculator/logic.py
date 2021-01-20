from arts import logo, calculation

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
    calculation(str(num1))

    for symbols in operations:
        print(symbols)

    operation_symbol = input("Pick an operation: ")
    calculation(f"{str(num1)} {operation_symbol}")
    num2 = float(input("What's the seconnd number?: "))
    calculation(f"{str(num1)} {operation_symbol} {str(num2)}")

    answer = operations[operation_symbol](num1, num2)
    calculation(f"{str(num1)} {operation_symbol} {str(num2)}", str(answer))

    #calculation(f"{num1} {operation_symbol} {num2} = {answer}")


    should_continue = True

    while should_continue:
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation.: ").lower() == 'y':

            result = answer
            
            operation_symbol = input("Pick an operation: ")
            
            calculation(f"{str(answer)} {operation_symbol}")
            num3 = float(input("What's the next number?. "))
            calculation(f"{str(num1)} {operation_symbol} {str(num3)}")
            answer = operations[operation_symbol](result, num3)
            calculation(f"{str(result)} {operation_symbol} {str(num3)}", str(answer))
        else:
            calculator()

        
calculator()
