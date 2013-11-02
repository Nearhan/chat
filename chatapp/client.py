import zmq
import sys
import time


PORT = '5556'
IP = sys.argv[1]
msg = sys.argv[2]

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://%s:%s" % (IP, PORT))

#send request
socket.send_string(msg)
time.sleep(1)
msg = socket.recv_string()
print(msg)
