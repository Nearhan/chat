import cmd
import zmq
from communicator import Communicator


class WorkerConfig(object):

    context = zmq.Context()



class CLI(cmd.Cmd):

    def do_start(self, line):
        pass


    def do_goodbye(self, line):
        pass


    def do_send_message(self, line):
        pass


if __name__ == '__main__':

    CLI().cmdloop(intro='Welcome to the shell, mortal.')

