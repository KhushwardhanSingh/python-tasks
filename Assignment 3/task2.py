import math
num = int(input("Enter a number: "))
def calculate_square_root(num):
    if num < 0:
        return "Square root is not defined for negative numbers."
    return math.sqrt(num)
    
def calculate_logarithm(num):
    if num <= 0:
        return "Logarithm is not defined for non-positive numbers."
    return math.log(num)
   
def calculate_sine(num):
    return math.sin(num)

print("square root : ", calculate_square_root(num))
print("logarithm : ", calculate_logarithm(num))
print("sine : ", calculate_sine(num))
