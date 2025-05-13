    #!/usr/bin/env python
    # Python Network Programming Cookbook,Second Edition -- Chapter - 1
    
    
import socket
import sys
import json
import random
    
host = '127.0.0.1'
port = 9879
data_payload = 2048
backlog = 5
    
#medicine prices, name and how much in stock
medicine_details={
    "Paracetamol":{"price": 5.00, "stock":1110},
    "Lexapro":{"price": 10.00, "stock":9},
    "Aspirin":{"price": 6.00, "stock":1500},
    "Insulin":{"price": 100.00, "stock":240},
    "Eumovate":{"price": 20.00, "stock":50},
    "Antihistamine":{"price": 3.70, "stock":110}
}

#currency exchange based on Pound Sterling
currency_rates={
    "GBP":1,
    "USD":1.29,
    "EUR":1.18,
    "INR":110.71
}

def order(order_data):
    try:
        #ordering system
        pharmacy_name = order_data["pharmacy_name"]
        pharmacy_ID = order_data["pharmacy_ID"]
        medicine = order_data["medicine"]
        requested_boxes = int(order_data["quantity_medicine"])
        currency = order_data["currency"]

        # Validate medicine
        if medicine not in medicine_details:
            return {"error": "Medicine not available"}

        # Check stock availability
        available_boxes = medicine_details[medicine]["stock"]
        supplied_boxes = min(requested_boxes, available_boxes)

        # Update stock
        medicine_details[medicine]["stock"] -= supplied_boxes

        # Calculate cost
        price_per_box = medicine_details[medicine]["price"]
        total_cost_gbp = price_per_box * supplied_boxes
        total_cost = total_cost_gbp * currency_rates.get(currency, 1)

        # Generate booking number
        booking_number = random.randint(100000, 999999)

        # Response
        return {
            "booking_number": booking_number,
            "pharmacy_ID": pharmacy_ID,
            "medicine": medicine,
            "quantity_supplied": supplied_boxes,
            "cost": f"{total_cost:.2f} {currency}"
        }
    except Exception as e:
        return {"error": f"Failed to process:{str(e)}"}
    
    
def echo_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    #print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(('127.0.0.1', 9879))#

    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog) 
    while True: 
        print ("Waiting to receive message from client")
        client, address = sock.accept() 
        data = client.recv(data_payload).decode('utf-8')
        print("Message Received from client: ",data)
        if data:
            try:
                # Try to load as JSON order
                request = json.loads(data)
                response = order(request)
                response_data = json.dumps(response)
            except json.JSONDecodeError:
                # Treat as plain message
                response_data = f"Echo from server: {data}"
            print("Data to Send to Client: %s" % response_data)
            client.send(response_data.encode('utf-8'))
            #end connection here
            print("sent %s bytes back to %s" % (response_data, address))
        client.close()
        
 
    
if __name__ == '__main__':
    #given_args = parser.parse_args() 
    port =9879
    echo_server(9879)
  

