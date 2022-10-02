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
sortednumbers = sorted(numbers, key = float)
numberslength = int(len(sortednumbers))
if numberslength % 2 == 1: #checks if the length of numbers is odd
    print(sortednumbers[int((numberslength/2)-0.5)])
else:
    print((sortednumbers[int((numberslength/2)-1)]+sortednumbers[int(numberslength/2)])/2)
