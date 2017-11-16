#!/home/viherbos/anaconda2/bin/python

import socket as sk
import numpy as np
import json
from Queue import Queue
from pypetalo import config
from pypetalo import comms
from threading import Thread, Event


def main():

    # CONFIG // STOP

    COMMAND = {'command':"STOP",
                'arg1':"10",
                'arg2':"13"}

    sh_data = config.DATA(read=True)
    clt_queue = Queue()
    stopper = Event()

    thread_CLIENT = comms.SCK_client(sh_data,clt_queue,stopper)

    thread_CLIENT.start()
    clt_queue.put(json.dumps(COMMAND))
    stopper.set()
    thread_CLIENT.join()

if __name__ == "__main__":
    main()
