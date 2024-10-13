# some basic computer knowledge: storing data, memory, arithmetic logic unit, input, output,... 

# scarlar ojects: int, float, string, bool, NoneType. using type() function to see the type of an object

print(type(1))
print(type(3.5))
print(type('hello'))
print(type(True))

# expressions: combine objects and operators to form expressions 
# <object> <operators> <objects>
# operators: + (sum) , - (difference) , * (product) , / (division) , % (remainder) , // (floor division) , ** (power)

print(1 + 1)
print(type(3 + 2))
print(11 % 3)
print((-43)//3)
print(type(4/5))
print(3**8)
print(float((4+2)*6-1)) # compress data type

# variables (computer science variables are different than math variables) 

x = 9
y = 6
xy = 67
print(x*y)
print(xy)

# rebind variables
x = x + 1
y = y - 1
print(x, y, x*y)

# swapping values between 2 variables
x = 1
y = 2
print('before swap:',x,y)
temp = x
x = y
y = temp 
print('after:',x,y)

