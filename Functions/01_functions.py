def avg(a, b, c):
    d = (a + b + c)/3
    print(d)

avg(1, 2, 3)

#if we want to print something to calling function we need to return it.
def greet(name):
    return f"Hello, {name}..!"

print(greet("Komal"))