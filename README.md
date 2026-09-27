# Cybersecurity Midterm Project

This repository contains my Python programming assignments for the cybersecurity midterm examination.

## Project Overview

The project includes:

1. A client-server TCP socket connection.
2. A Python TCP port scanner restricted to the targets authorized by the assignment.
3. Testing documentation and an AI assistance record.

## Repository Structure

```text
cybersecurity-midterm/
├── socket_connection/
│   ├── server.py
│   └── client.py
├── port_scanner/
│   └── port_scanner.py
├── AI_ASSISTANCE.md
├── TESTING.md
└── README.md
```

## Part 1: Socket Connection

The socket project uses two Python programs. The server creates a TCP socket, binds it to the local host and port 5000, listens for a connection, receives a message, and sends a response. The client connects to the server, sends a message, receives the response, and closes its connection.

Python's `socket` module provides the low-level networking interface used for this project. The normal TCP server sequence includes creating a socket, binding, listening, and accepting a connection, while the client uses a socket and connects to the server. citeturn0search1

### Run the server

```text
cd socket_connection
python server.py
```

### Run the client

Open a second terminal in the same folder:

```text
python client.py
```

## Part 2: Port Scanner

The port scanner performs TCP connection checks over a user-specified inclusive port range.

For this assignment, the program intentionally restricts targets to:

- `127.0.0.1`
- `localhost`
- `scanme.nmap.org`

The scanner includes input validation, socket timeouts, error handling, and a small delay between connection attempts.

### Example localhost scan

```text
cd port_scanner
python port_scanner.py 127.0.0.1 21 443
```

### Example custom range

```text
python port_scanner.py 127.0.0.1 5000 5010
```

### Authorized scanme.nmap.org example

Use only a limited range as required by the course:

```text
python port_scanner.py scanme.nmap.org 20 25
```

Do not scan other systems without explicit authorization.

## Error Handling

The programs handle common errors including:
- The client attempting to connect while the server is stopped.
- Invalid port numbers.
- A reversed port range.
- An unauthorized target.
- Host resolution and connection errors.
- Socket timeouts.

## Testing

See [TESTING.md](TESTING.md) for the required test cases and screenshot checklist.

Screenshots should be added only after the tests have actually been performed. Keep timestamps visible when possible.

## AI Assistance

See [AI_ASSISTANCE.md](AI_ASSISTANCE.md). This record should contain the actual AI tools and prompts used during development, along with the changes made after receiving assistance.

## Security and Ethical Considerations

Port scanning can identify services listening on a host. Because scanning systems without permission can be unauthorized, this project uses an allowlist containing only the targets specified by the course assignment. The scanner also uses timeouts and a small delay between attempts rather than aggressive scanning.

## Course Submission

Before submitting, verify that:
- Both Python programs are uploaded.
- Both programs have been tested locally.
- Successful and unsuccessful socket tests are documented.
- Port scanner tests are documented.
- Required screenshots include timestamps.
- The written reflection is based on my actual development and testing experience.
- Any AI assistance is documented accurately.
