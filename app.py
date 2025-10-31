# print("hello world")
# #primitive
# a = 30
# print(type(a))

# b = "50"
# print(type(b))

# c = True
# print(type(c))

# #non-primitive
# d = 2+3j
# print(type(d))

# e = (23,18,43)
# print(type(e))

# f = [23,18,43]
# print(type(f))

# j = {23,60,86}
# print(type(j))

# h = {id : '23'}
# print(type(h))

# l = [23,18,43] #tuples are not mutable
# print(l[0])

# f = [23,18,43]
# f[2] = 34
# print(f) 

def app():
    a = 20
    b = 30
    return print(a+b)
app()


age = 20
age = int(input("Enter your age: "))
if(age >= 18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")

temperature = 32
temperature = int(input("Enter the temperature: "))
if(temperature == 32):
    print("room temperature")
elif(temperature <= 32):
    print("It's hot")
else:
    print("it's cold")






