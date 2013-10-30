import multiprocessing
import logging
import zmq


class Communicator(multiprocessing.Process):

    multiprocessing.log_to_stderr(logging.DEBUG)

    def run(self):
        try:
            name = multiprocessing.current_process().name
            print('PROCESS ID ' + name + ' is a Communicator class')

        except:
            print('oh shit something happened')

    def __init__(self):  # TODO does this take a Queue

        self.daemon = True
        self.context = zmq.Context()
