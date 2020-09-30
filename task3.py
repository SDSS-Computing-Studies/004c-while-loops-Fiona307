#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

number = ""
x = x
while x % 1 != 0 or x % 2 != 0:
    number = (input("Enter a number")).strip()
    x = float(number)
    if x % 1 != 0 or x % 2 != 0:
        print("That is not an even integer")
    else:
        print("That is an enven integer")