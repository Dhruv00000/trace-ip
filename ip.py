from socket import gethostbyname, gaierror

host = input("Enter the website that you wannt to trace the ip of: ")

try:

    print(f"The IP address is {gethostbyname(host)}")

# Handling invalid domains.
except gaierror:

    print("Please enter a valid domain.")