
"""
Simple command-line calculator.
Supports: +, -, *, /, %, ** (power), // (floor division)
Handles errors (division by zero, invalid input).
Enter 'exit' to quit.
"""

def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    if op == "%":
        if b == 0:
            raise ZeroDivisionError("Modulo by zero")
        return a % b
    if op == "":
        return a ** b
    if op == "//":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a // b
    raise ValueError("Unsupported operator")

def main():
    print("Simple Calculator. Supported ops: + - * / % ** //")
    while True:
        expr = input("Enter expression (e.g. 2 + 3) or 'exit': ").strip()
        if not expr:
            continue
        if expr.lower() in ("exit", "quit"):
            print("Goodbye.")
            break
        # naive parse: split by spaces
        parts = expr.split()
        try:
            if len(parts) == 3:
                a = float(parts[0])
                op = parts[1]
                b = float(parts[2])
                res = calculate(a, b, op)
                # if result is whole number show as int
                if isinstance(res, float) and res.is_integer():
                    res = int(res)
                print("Result:", res)
            else:
                print("Please enter in format: number operator number (e.g. 3 * 4)")
        except ZeroDivisionError as e:
            print("Error:", e)
        except ValueError as e:
            print("Error:", e)
        except Exception:
            print("Invalid input or unsupported operation.")

if __name__ == "__main__":
    main()