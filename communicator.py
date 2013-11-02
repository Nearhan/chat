import multiprocessing
import logging
import zmq


class QueueDevice():

    def create_queue(self):
        context = zmq.Context()
        frontend = context.socket(zmq.XREP)
        frontend.connect("tcp://50.17.152.74:5000")  # listen to server
        backend = context.socket(zmq.XREQ)
        backend.bind("tcp://127.0.0.1:6000")  # listen locally
        zmq.device(zmq.QUEUE, frontend, backend)



class ClientWorker(multiprocessing.Process):

    multiprocessing.log_to_stderr(logging.DEBUG)

    def run(self):
        try:
            dev = QueueDevice()
            dev.create_queue()
        except:
            print('oh shit something happened')

    def __init__(self):
        #self.daemon = False
        self.name = multiprocessing.current_process().name

