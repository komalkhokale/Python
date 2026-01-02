def add(a, b): #parameters  #Positional Arguments
    return a + b

# c = add(2, 4) #Arguments
# print(c)

#Default Arguments
def add(a, b, plus=2):
    return a + b + plus

c = add(2, 4)
print(c)


#Keyword Arguments
c1 = add(b=3, a=4)
print(c1)   