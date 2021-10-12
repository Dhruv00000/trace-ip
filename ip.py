# Importing the necessary functions from the module.
from socket import gethostbyname, gaierror

# Getting the user input.
host = input("Enter the website that you wannt to trace the ip of: ")

try:

    # Finding and printing the ip.
    print(f"The IP address is {gethostbyname(host)}")

# If the user enters an invalid domain, this message is printed out instead of the program crashing with an error.
except gaierror:

    print("Please enter a valid domain.")