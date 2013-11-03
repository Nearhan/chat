import cmd
import sys
import zmq
from chatapp.communicator import create_queue
from config import config
from multiprocessing import Process


class CLI(cmd.Cmd):

    def do_start(self, line):
        pass

    def do_goodbye(self, line):
        pass

    def do_send(self, line):
        self.socket.send_string(line)

    def do_kill(self, line):
        # kill the zmq process
        pass

    def __init__(self, socket):
        self.socket = socket


if __name__ == '__main__':

    context = zmq.Context()
    # initialize queue
    queue_process = Process(target=create_queue, name='main_queue', args=(context,))
    queue_process.start()
    # TODO get pid for killing the queue process
    client_socket = context.socket(zmq.REQ)
    client_socket.connect("tcp://%s:%s") \
        % config['server_ip'], config['server_port']

    CLI(client_socket).cmdloop(intro='Welcome to the shell, mortal.')

