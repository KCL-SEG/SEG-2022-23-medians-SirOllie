"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
numberslength = int(len(numbers))
if numberslength % 2 == 1: #checks if the length of numbers is odd
    print(numbers[int((numberslength/2)-0.5)])
else:
    print((numbers[int((numberslength/2)-1)]+numbers[int(numberslength/2)])/2)
