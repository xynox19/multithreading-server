#!/usr/bin/env python 
# Source Python Network Programming Cookbook,Second Edition -- Chapter - 1 

import socket 
import sys 
import json  # don't forget to import json

host = '127.0.0.1'

available_medicines = [
    "Paracetamol",
    "Lexapro",
    "Aspirin",
    "Insulin",
    "Eumovate",
    "Antihistamine"
]

def echo_client(port): 
    """ A simple echo client """ 
    # First connection for order
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = ('127.0.0.1', 9879)
    print("--------------------")
    print ("Connecting to %s port %s" % server_address) 
    sock.connect(server_address)

    order_med = input("Would you like to place an order? y or n: ")
    if order_med.strip().lower() in ["yes", "y"]:
        pharmacy_name = input("Enter Pharmacy Name: ")
        pharmacy_ID = input("Enter Pharmacy ID: ")

        print("\nAvailable Medicines:")
        for med in available_medicines:
            print(f" - {med}")
        print()

        medicine.lower() = input("Enter Medicine to Order: ")
        while not medicine:  # Ensure the user enters a valid medicine
            print("Error: Medicine cannot be empty.")
            medicine = input("Enter Medicine to Order: ")

        quantity_medicine = input("Enter Amount of Medicine to Order: ")
        while not quantity_medicine.isdigit():  # Ensure the user enters a valid number for quantity
            print("Error: Please enter a valid number for quantity.")
            quantity_medicine = input("Enter Amount of Medicine to Order: ")

        currency = input("Enter Currency (GBP, USD, INR, EUR): ")
        while currency not in ["GBP", "USD", "INR", "EUR"]:  # Ensure a valid currency
            print("Error: Invalid currency. Please enter GBP, USD, INR, or EUR.")
            currency = input("Enter Currency (GBP, USD, INR, EUR): ")

        order_data = {
            "pharmacy_name": pharmacy_name,
            "pharmacy_ID": pharmacy_ID,
            "medicine": medicine,
            "quantity_medicine": quantity_medicine,
            "currency": currency
        }

        # Send order data
        sock.sendall(json.dumps(order_data).encode('utf-8'))

        # Receive and handle order response
        data = sock.recv(1024)
        try:
            order_response = json.loads(data.decode("utf-8"))
            if "error" in order_response:
                print(f"Error: {order_response['error']}")
            else:
                print("\n--- Order Confirmation ---")
                print(f"Booking Number: {order_response['booking_number']}")
                print(f"Pharmacy ID: {order_response['pharmacy_ID']}")
                print(f"Medicine: {order_response['medicine']}")
                print(f"Quantity Supplied: {order_response['quantity_supplied']}")
                print(f"Total Cost: {order_response['cost']}")
        except json.JSONDecodeError:
            print("Received from Server:", data.decode("utf-8"))

        print ("Closing connection to the server") 
        sock.close()

    # Second connection for sending additional messages
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    message = input("Enter your comment: ")
    print(f"Sending to Server: {message} :")
    sock.sendall(message.encode('utf-8'))

    # Look for the response
    try:
        data = sock.recv(1024)
        if data:
            print("Received from Server:", data.decode("utf-8"))

    except socket.error as e:
        print(f"Socket error: {str(e)}")
    except Exception as e:
        print(f"Other exception: {str(e)}")
    finally:
        # Close the second connection
        print ("Closing connection to the server") 
        sock.close()
        exit()

if __name__ == '__main__': 
    port = 9879 
    while True:
        echo_client(port) 
