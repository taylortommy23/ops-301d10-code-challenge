#!/usr/bin/env/python3

import requests

# Prompt user for URL and HTTP method
destination_url = input("Enter the destination URL: ")
http_method = input("Select an HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Check if HTTP method is valid
valid_methods = ("GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS")
if http_method not in valid_methods:
    print(f"Invalid HTTP method: {http_method}")
    exit(1)

# Print request information
print(f"\nRequest information:")
print(f"URL: {destination_url}")
print(f"Method: {http_method}")

# Send request and handle response
try:
    if http_method == "GET":
        response = requests.get(destination_url)
    elif http_method == "POST":
        # Prompt user for data to send
        data = input("Enter data to send (JSON format): ")
        response = requests.post(destination_url, data=data)
    elif http_method == "PUT":
        # Prompt user for data to send
        data = input("Enter data to send (JSON format): ")
        response = requests.put(destination_url, data=data)
    elif http_method == "DELETE":
        response = requests.delete(destination_url)
    elif http_method == "HEAD":
        response = requests.head(destination_url)
    elif http_method == "PATCH":
        # Prompt user for data to send
        data = input("Enter data to send (JSON format): ")
        response = requests.patch(destination_url, data=data)
    elif http_method == "OPTIONS":
        response = requests.options(destination_url)

    # Print response status code
    print(f"\nResponse status code: {response.status_code}")

    # Translate and print response headers
    print("\nResponse headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

except Exception as e:
    print(f"\nError: {e}")
