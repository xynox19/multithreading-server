# Multithreading TCP Server

This project is a simple multithreaded TCP server and client implemented in C++. It demonstrates basic socket programming using the BSD sockets API and includes threading support to handle multiple clients concurrently.

## Features

- Multithreaded TCP server using POSIX threads (`pthread`)
- Handles multiple client connections simultaneously
- Simple TCP client for testing the server
- Basic send/receive communication
- Clean, minimal codebase for learning or extension

## File Structure

- `tcp-server.cc`: The main multithreaded server implementation.
- `tcp-client.cc`: A client that connects to the server for communication.
- `Makefile`: For building both server and client with a single command.

## Build Instructions

Make sure you have a C++ compiler (like `g++`) and `make` installed.

This will compile: 
tcp-server (from tcp-server.cc) 
tcp-client (from tcp-client.cc) 

## Run Instructions

Please ensure you start the server first before you run the client. Start the server and ensure both the server and client model run on the same port you have chosen.

### Start the Server

```bash
./tcp-server <PORT>
./tcp-server 8080
```


## How It Works
The server listens on a specified port.

For each incoming client connection, it spawns a new thread using pthread.

Each client can send messages to the server.

The server can echo or handle the messages based on the implemented logic.

All communication happens via standard TCP sockets.

## Dependencies
POSIX-compatible system (Linux/macOS)

g++ (for compiling C++ code)

pthread library (typically included by default)

