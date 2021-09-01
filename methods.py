# def name(n):
#     print(n)
# name("John")

# def name(n):
#     return n
# print(name("John"))

# def square(s):
#     return s * s
# print(square(4))

# def your_name(fname):
#     return fname

# print("Input your First Name")
# fname = input("First Name:")
# print(f"Your firstname is:{your_name(fname)}")

from square import squares
from square import cubes
print(f"The square of 4 is: {squares(4)}")
print(f"The cube is: {cubes(4)}")

from square import area_triangle
print(f"The area of the triangle is: {print(area_triangle(4,5))}")