import zmq
import argparse
import csv
import random
import time

# Parse arguments
parser = argparse.ArgumentParser('ZMQ Publisher')
parser.add_argument('-port', default=random.randint(10000, 40000), help='The port to bind your process to', type=int)
parser.add_argument('-topic', help='The topic to publish', required=True)
parser.add_argument('-rate', '--pub_rate', help='The publishing rate (in secs)', type=float, default=1)
parser.add_argument('-fp', '--file_path', default='combo.csv')
args = parser.parse_args()

topic = args.topic.lower()


def read_csv(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for index, top in enumerate(next(csv_reader)):
            ltop = top.lower()
            if topic in ltop:
                print(topic, ltop)
                break

        lst = []
        for row in csv_reader:
            lst.append('{}_{}_{}'.format(top, row[0], row[index]))

    return lst


msgs = read_csv(args.file_path)

context = zmq.Context()
socket = context.socket(zmq.PUB)

socket.bind("tcp://*:{}".format(args.port))
# socket.connect("tcp://127.0.0.1:{}".format(args.port))

while True:
    for msg in msgs:
        socket.send_string(msg)
        time.sleep(args.pub_rate)

