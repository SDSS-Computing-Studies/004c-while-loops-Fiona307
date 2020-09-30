##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""

username = ""
password = ""
count = 0

while username != "admin" or password != "12345":
    username = input("Enter your username")
    password = input("Enter your password")
    count = count + 1
    if username != "admin" or password != "12345":
        print("Access denied")
    if count == 3:
        break
    elif username == "admin" and password == "12345":
        print("Access granted")