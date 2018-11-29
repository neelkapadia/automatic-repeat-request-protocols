# CSC 573 - Internet Protocols Project 2

## Go-Back-N Automatic Repeat Request Protocol

Step 1: Install all required packages
```
pip install time
pip install signal
pip install socket
pip install inspect
pip install struct
pip install sys
pip install threading
pip install pickle
pip install random
```

Step 2: Run the server
```
python3 go-back-n-server.py <server-port> <server-buffer-file> <probability>

eg.
python3 go-back-n-server.py 20930 server-file.txt 0.05
```

Step 3: Run the client
```
neelkapadia$ python3 go-back-n-client.py <server-host-name> <server-port-number> <client-sending-file> <window-size> <MSS>

eg.
python3 go-back-n-client.py Neels-MacBook-Pro.local 20930 client-file.txt 1 500
```

Step 4: Observe the output of the client to get information on the time required to send, server info etc.