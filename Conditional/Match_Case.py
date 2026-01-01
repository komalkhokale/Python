a = int(input("Enter a number: "))

match(a):
    case 122:
        print("The value is 122")
    case 6:
        print("The value is 6")
    case 3: 
        print("The value is 3")
    case _:
        print("Better luck next time")