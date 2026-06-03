from calculator import add, subtract, multiply, divide

def run():
    print("Simple Calculator (type 'exit' to quit)")

    while True:
        command = input("Enter operation (+, -, *, /): ")

        if command == "exit":
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if command == "+":
            print(add(a, b))
        elif command == "-":
            print(subtract(a, b))
        elif command == "*":
            print(multiply(a, b))
        elif command == "/":
            print(divide(a, b))
        else:
            print("Invalid operation")

if __name__ == "__main__":
    run()
