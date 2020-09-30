#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

username = ""
password = ""

while username != "admin" or password != "12345":
    username = (input("Enter your username")).strip()
    password = (input("Enter your password")).strip()
    if username != "admin" or password != "12345":
        print("Access denied")
    elif username == "admin" and password == "12345":
        print("Access granted")
