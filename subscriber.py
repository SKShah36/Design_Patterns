import zmq
import argparse

parser = argparse.ArgumentParser('ZMQ Publisher')
parser.add_argument('addresses', nargs='+',
                                        help='IP addresses you want to receive messages from in the format ip:port')
parser.add_argument('-topic', help='The topic to publish', required=True)

args = parser.parse_args()

print(args.addresses)

context = zmq.Context()
socket = context.socket(zmq.SUB)

for address in args.addresses[1:]:
    socket.connect("tcp://{}".format(address))

socket.setsockopt_string(zmq.SUBSCRIBE, "")
while True:
    string = socket.recv_string()
    print(string)