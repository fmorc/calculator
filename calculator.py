from art import logo

print(logo)


def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def substract(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divides two numbers"""
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What is the first number? "))

    another_number = True
    while another_number:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation from the type above: ")
        operation_function = operations[operation_symbol]

        num2 = float(input("What is the second number? "))

        answer = operation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        another_number = input("Do you wish to continue? y/n: ")
        if another_number == 'n':
            another_number = False
            calculator()
        else:
            num1 = answer


calculator()