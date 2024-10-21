# string
a = 'me' # variables
b = 'you'
c = a + b # adding strings
d = a + ' ' + b # adding string variables but with another string
silly = a * 3 # multiply string x3 times
print(a, b)
print(c)
print(d)
print(silly)

# slicing to get 1 character in a string
# strings are immutable so it can't be modified. e.g: s[0] = 'b' will give an error

print(a[0], a[1])
print(b[0], b[1], b[2])
print(c[3])
print(a[-1], a[-2]) # -1: e  -2: m

# slicing to get substring
# [start:stop:step]
# start -> (stop - 1)
# step cannot be 0
# default step = 1 so if [start:stop] then it will still work but step = 1
# [::-1] to use the reversed string and when printing, it starts at the first position from the string's right
# [-1] = [len(<stringname>)-1]
# if step < 0 then end must be > than start or it will not return anything

print(silly[3:6]) # start at 3, end at (6-1)=5 , step = 1
print(silly[3:6:2]) # ee
print(d[::-1]) # print the reversed string of d but not changing the original string
print(d[6:2:-2]) # uy

# modifying strings to string
g = 'healrlowwwoerl'
print(g)
g = g[0:2] + 'l' + g[5:7] + g[9:11] + g[12:len(g)] + 'd'
print(g)

# print() function
print(True,'2a',3,4.4) # just print :)

# input() function
inp = input("write something: ")
print(5*inp)
num = int(input("write a number: "))
print('you just wrote the number',num,'!')

# F-strings
# Notice: Available starting with Python 3.6
num = 3000
fraction = 1/3
print(num*fraction,'is',fraction*100,'% of',num)
print(num*fraction,'is',str(fraction*100)+'% of',num)
print(f'{num*fraction} is {fraction*100}% of {num}')  # this is called f-string

# comparison operators
# i > j
# i >= j
# i < j
# i <= j
# i == j : equality test
# i != j : inequality test
print(2 < 3)
print(5 >= 4)
print(6==0)
print(8!=4,end='\n\n')

# logical operators on bool
# not a: return True if a is False and False if a is True
# a and b: True if both are True
# a or b: True if either or both are True
print(not (2<3))
print((9>8) and (5<4))
print((7==11) or (12>10))

#branching in python
# type 1:
# if <condition>:
#   <code>
#   <code>
#   ...
# the rest of the code
# Do code withtin if block when condition is True
# type 2:
# if <condition>:
#   <code>
#   <code>
#   ...
# else:
#   <code>
#   <code>
#   ...
# the rest of the code
# Do code withtin if block when condition is True or code within else block when condition is False
# type 3:
# if <condition>:
#   <code>
#   <code>
#   ...
# elif <condition>:
#   <code>
#   <code>
#   ...
# else:
#   <code>
#   <code>
#   ...
# <condition> has a value of True or False
# indentation matters in Python
