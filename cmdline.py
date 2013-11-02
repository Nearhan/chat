import cmd
import zmq
from communicator import ClientWorker


QUEUE_DEVICE_ADDRESS = 'tcp://127.0.0.1'
CLIENT_PORT = '6000'
PID = None


class CLI(cmd.Cmd):

    def do_start(self, line):
        pass

    def do_goodbye(self, line):
        pass

    def do_send_message(self, line):
        pass

    def do_kill(self, line):
        # kill the zmq process
        pass

    #def do_bind(self, line):
    #    self.context = zmq.Context()
    #    self.socket = self.context.socket(zmq.REQ)
    #    self.socket.bind("tcp://127.0.0.1:%s" % CLIENT_PORT)

    def do_client(self, line):
        client = ClientWorker()
        client.start()


if __name__ == '__main__':

    # worker = ClientWorker()
    # device = QueueDevice()
    CLI().cmdloop(intro='Welcome to the shell, mortal.')

