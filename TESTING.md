# Midterm Testing Documentation

Use this file as a checklist while completing the required demonstrations. Replace the blank areas with your actual test results after running the programs.

## Part 1: Socket Connection

### Test 1 - Successful connection and message exchange
- Start `server.py`.
- Start `client.py`.
- Send a test message from the client.
- Confirm the server receives it.
- Confirm the client receives the server response.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 2 - Server receiving a message
- Server output shows the client's message.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 3 - Client receiving a response
- Client output shows the server response.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 4 - Server not running
- Stop the server.
- Run the client.
- Confirm that the connection-refused error is handled without a traceback.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 5 - Clean disconnection
- Confirm the client closes its socket.
- Confirm the server closes the client connection and server socket.
- Screenshot: ______________________________
- Date/time: ______________________________

## Part 2: Port Scanner

Only scan the authorized targets listed in the assignment: `127.0.0.1`, `localhost`, and `scanme.nmap.org`.

### Test 6 - Common localhost ports
Example:
```text
python port_scanner.py 127.0.0.1 21 443
```
Record the open and closed ports shown by your own computer.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 7 - Custom localhost range
Example:
```text
python port_scanner.py 127.0.0.1 5000 5010
```
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 8 - Authorized scanme.nmap.org test
Use a limited range as directed by your instructor.
Example:
```text
python port_scanner.py scanme.nmap.org 20 25
```
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 9 - Invalid port number
Example:
```text
python port_scanner.py 127.0.0.1 0 10
```
Confirm that the program reports the invalid port instead of attempting the scan.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 10 - Invalid port range
Example:
```text
python port_scanner.py 127.0.0.1 5000 4000
```
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 11 - Unauthorized target
Example:
```text
python port_scanner.py example.com 80 80
```
Confirm that the program rejects the target before scanning.
- Screenshot: ______________________________
- Date/time: ______________________________

### Test 12 - Different range sizes
Run a small range and a larger range on localhost and record the completion time printed by the scanner.
- Small range: ______________________________
- Larger range: _____________________________
- Screenshots: ______________________________
- Date/time: ______________________________

## Screenshot Requirements

Keep the terminal clock/date visible when possible. Screenshots should clearly show:
- The command that was executed.
- The program output.
- The target and port range.
- The date/time when the test was performed.

Do not claim a test passed until you have actually run it.
