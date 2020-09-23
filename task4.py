#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math

print("Input side 1")
s1 = input()
s1 = int(s1)
print("Input side 2")
s2 = input()
s2 = int(s2)
hyp2 = math.pow(s1,2) + math.pow(s2,2)
hyp = math.sqrt(hyp2)

print("Hypotenuse = " ,end="")
print(hyp)
