a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

operation = input("Choose Operation: ")

if (b == 0):
    print(" 0 Naver be divisible")

match operation: 
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid Operation")    