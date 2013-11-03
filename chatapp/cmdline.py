import cmd
import sys
import zmq
from config import config
from multiprocessing import Process
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
        pass

    def do_receive(self, line):
        """
        Should be able to remove this.
        """
        self.client_socket.recv_string()
        pass

    def do_debug(self, line):
        import pdb
        pdb.set_trace()


#class ClientSocketPoller(Process):
#
#    def run(self):
#        context = zmq.Context()
#        polled_socket = context.socket(zmq.REQ)
#        polled_socket.connect("tcp://%s:%s" % (config['client_ip'], config['client_port']))
#        poller = zmq.Poller()
#        poller.register(polled_socket, zmq.POLLIN)
#
#        continue_status = True
#        while continue_status:
#            socks = dict(poller.poll())
#            if polled_socket in socks and socks['polled_socket'] == zmq.POLLIN:
#                msg = polled_socket.recv()
#                print msg

if __name__ == '__main__':

    queue_process = ProcessDevice(zmq.QUEUE, zmq.XREP, zmq.XREQ)
    queue_process.connect_out("tcp://%s:%s" % (config['server_ip'], config['server_port']))
    queue_process.bind_in("tcp://%s:%s" % (config['client_ip'], config['client_port']))
    queue_process.start()
    #poll_process = ClientSocketPoller()
    #poll_process.start()
    CLI().cmdloop(intro='Welcome to the shell, mortal.')

