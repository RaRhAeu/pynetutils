#!/usr/bin/env python3
import sys
import argparse
from pynetutils import TCPClient, TCPServer


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", action="store_true")
    parser.add_argument("-e", "--execute")
    parser.add_argument("-c", "--command")
    parser.add_argument("-u", "--upload")
    parser.add_argument("-t", "--host", default="0.0.0.0")
    parser.add_argument("-p", "--port", default=80, type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    host = args.host
    port = args.port
    execute = args.execute
    command = args.command
    upload = args.upload
    if args.listen:
        TCPServer.server_loop(host, port, upload, execute, command)
    else:
        TCPClient.sender(host, port)
    sys.exit(0)





if __name__ == '__main__':
    main()
