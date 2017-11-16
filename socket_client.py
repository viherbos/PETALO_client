#!/home/viherbos/anaconda2/bin/python

import socket as sk
import numpy as np
import json
from Queue import Queue
from pypetalo import config
from pypetalo import comms
from threading import Thread, Event


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PETALO remote control client.')
    parser.add_argument("-a", "--acquire", action="store_true",
                        help="Acquire Data for N seconds")
    parser.add_argument("-s", "--stop", action="store_true",
                        help="Stop Acquisition")
    parser.add_argument("-c", "--calibration", action="store_true",
                        help="Calibration routine for QDC & TDC")
    parser.add_argument('arg1', metavar='N', nargs='?', help='')
    parser.add_argument('arg2', metavar='N', nargs='?', help='')

    args = parser.parse_args()

    sh_data = config.DATA(read=True)
    clt_queue = Queue()
    stopper = Event()
    thread_CLIENT = comms.SCK_client(sh_data,clt_queue,stopper)
    thread_CLIENT.start()


    if args.acquire:
        COMMAND = {'command':"ACQUIRE",
                    'arg1':''.join(args.arg1),
                    'arg2':"88"}
        clt_queue.put(json.dumps(COMMAND))
    elif args.stop:
        COMMAND = {'command':"STOP",
                    'arg1':"88",
                    'arg2':"88"}
        clt_queue.put(json.dumps(COMMAND))
    elif args.calibration:
        COMMAND = {'command':"CONFIG",
                    'arg1':"88",
                    'arg2':"88"}
        clt_queue.put(json.dumps(COMMAND))


    stopper.set()
    thread_CLIENT.join()
