import zmq
import sys


port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    message = socket.recv()
    print message
    output = '<OK got message: %s>', % message
    socket.send(output)

