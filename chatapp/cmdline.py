import cmd
import ipdb
import zmq
from config import config
from zmq.devices import ProcessDevice


class CLI(cmd.Cmd):

    context = zmq.Context()
    client_socket = context.socket(zmq.REQ)
    client_socket.connect("tcp://%s:%s" % (config['client_ip'], config['client_port']))

    def default(self, line):
        line = str(line)
        self.do_send(line)

    def do_send(self, line):
        self.client_socket.send_string(line)
        msg = self.client_socket.recv_string()
        print msg

    def do_receive(self, line):
        """
        Should be able to remove this.
        """
        self.client_socket.recv_string()

    def do_debug(self, line):
        ipdb.set_trace()

if __name__ == '__main__':

    queue_process = ProcessDevice(zmq.QUEUE, zmq.XREP, zmq.XREQ)
    queue_process.connect_out("tcp://%s:%s" % (config['server_ip'], config['server_port']))
    queue_process.bind_in("tcp://%s:%s" % (config['client_ip'], config['client_port']))
    queue_process.start()
    CLI().cmdloop(intro='Welcome to the shell, mortal.')

