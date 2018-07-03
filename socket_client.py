#!/home/viherbos/anaconda2/bin/python

import socket as sk
import numpy as np
import json
from Queue import Queue
from pypetalo import config
from pypetalo import comms
from threading import Thread, Event
import argparse
import pysftp
import os


if __name__ == "__main__":

    host = "158.42.105.105"
    password = "pi31416"
    username = "petalo"

    parser = argparse.ArgumentParser(description='PETALO remote control client.')
    parser.add_argument("-a", "--acquire", action="store_true",
                        help="Acquire Data for N seconds")
    parser.add_argument("-s", "--stop", action="store_true",
                        help="Stop Acquisition")
    parser.add_argument("-c", "--calibration", action="store_true",
                        help="Calibration routine for QDC & TDC")
    parser.add_argument("-f", "--cfilter", action="store_true",
                        help="Coincidence Filter")
    parser.add_argument("-w", "--raw", action="store_true",
                        help="Raw Single Extraction")
    parser.add_argument("-t", "--temperature", action="store_true",
                        help="Temperature in ASICs")
    parser.add_argument("-r", "--restart", action="store_true",
                        help="Restart RUNs counter")
    parser.add_argument("-g", "--getsftp", action="store_true",
                        help="Gets files through sftp")
    parser.add_argument("-d", "--dcsource", action="store_true",
                        help="Turn DC source ON/OFF and control Peltier")


    parser.add_argument('arg1', metavar='N', nargs='?', help='')
    parser.add_argument('arg2', metavar='N', nargs='?', help='')

    args = parser.parse_args()

    sh_data = config.DATA(read=True)
    clt_queue   = Queue()
    clt_queue_2 = Queue()

    stopper = Event()
    thread_CLIENT  = comms.SCK_client(sh_data,
                                     clt_queue,
                                     stopper,int(sh_data.data['client_port']))
    thread_CLIENT2 = comms.SCK_client(sh_data,
                                     clt_queue_2,
                                     stopper,int(sh_data.data['client_port2']))

    thread_CLIENT.start()
    thread_CLIENT2.start()


    if args.acquire:
        # ACQUIRE COMMAND: arg1=seconds arg2=data/my_data
        COMMAND = {'command':"ACQUIRE",
                    'arg1':''.join(args.arg1),
                    'arg2':''.join(args.arg2)}
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
    elif args.cfilter:
        # COINCIDENCE FILTER COMMAND: arg1=i_data/my_data arg2=o_data/my_data
        COMMAND = {'command':"C_FILTER",
                    'arg1':''.join(args.arg1),
                    'arg2':''.join(args.arg2)}
        clt_queue.put(json.dumps(COMMAND))
    elif args.raw:
        # RAW EXTRACTION COMMAND: arg1=i_data/my_data arg2=o_data/my_data
        COMMAND = {'command':"RAW_FILTER",
                    'arg1':''.join(args.arg1),
                    'arg2':''.join(args.arg2)}
        clt_queue.put(json.dumps(COMMAND))
    elif args.temperature:
        COMMAND = {'command':"TEMP",
                    'arg1':"88",
                    'arg2':"88"}
        clt_queue.put(json.dumps(COMMAND))
    elif args.restart:
        COMMAND = {'command':"RESTART",
                    'arg1':"88",
                    'arg2':"88"}
        clt_queue.put(json.dumps(COMMAND))
    elif args.getsftp:
        file_name = ''.join(args.arg1)
        actual_path = os.getcwd()
        os.chdir("/home/viherbos/DAQ_DATA")
        with pysftp.Connection(host, username=username, password=password) as sftp:
            sftp.chdir(sh_data.data['data_path'])
            filenames = sftp.listdir()
            for i in filenames:
                if (i.find(file_name)!=-1) and (i.find(".hdf")!=-1):
                    sftp.get(i)
        os.chdir(actual_path)

    elif args.dcsource:
        # Turn ON/OFF DC source
        COMMAND = {'command':"DC",
                    'arg1':''.join(args.arg1),
                    'arg2':''.join(args.arg2)}
        clt_queue_2.put(json.dumps(COMMAND))

    stopper.set()
    thread_CLIENT.join()
    thread_CLIENT2.join()
