from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_ports = []


def prepare_args():
    """ prepare arguments

        return:
            args()
    """
    parser = ArgumentParser(
        description="Python Based Fast Port Scanner",
        usage="%(prog)s 192.168.1.2",
        epilog="Example - %(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.2"
    )

    parser.add_argument(
        metavar="IPv4",
        dest="ip",
        help="host to scan"
    )

    parser.add_argument(
        "-s",
        "--start",
        dest="start",
        metavar="",
        type=int,
        help="Starting port",
        default=1
    )

    parser.add_argument(
        "-e",
        "--end",
        dest="end",
        metavar="",
        type=int,
        help="ending port",
        default=65535
    )

    parser.add_argument(
        "-t",
        "--threads",
        dest="threads",
        metavar="",
        type=int,
        help="threads to use",
        default=500
    )

    parser.add_argument(
        "-V",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="verbose output"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 3.0",
        help="Displays version"
    )

    args = parser.parse_args()

    if args.start < 1 or args.end > 65535:
        parser.error("Port range must be between 1 and 65535")

    if args.start > args.end:
        parser.error("Starting port cannot be greater than ending port")

    if args.threads <= 0:
        parser.error("Threads must be greater than 0")

    return args


def prepare_ports(start: int, end: int):
    """generator functions for ports

        arguments:
            start(int) - starting port
            end(int) - ending ports
    """
    for port in range(start, end + 1):
        yield port


def scan_port():
    """
    scan ports
    """
    while True:
        s = None

        try:
            port = next(ports)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            s.connect((arguments.ip, port))
            open_ports.append(port)

            if arguments.verbose:
                print(f"\r{sorted(open_ports)}", end="")

        except (ConnectionRefusedError, socket.timeout):
            continue

        except StopIteration:
            break

        except OSError:
            continue

        finally:
            if s is not None:
                s.close()


def prepare_threads(threads: int):
    '''
    create , start, join threads
        arguments:
            threads(int) - number of threads to use
    '''

    thread_list = []

    for _ in range(threads):
        thread_list.append(Thread(target=scan_port))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    arguments = prepare_args()

    ports = prepare_ports(arguments.start, arguments.end)

    start_time = time()

    prepare_threads(arguments.threads)

    end_time = time()

    if arguments.verbose:
        print()

    print(f"Open Ports Found - {sorted(open_ports)}")
    print(f"Time Taken - {round(end_time - start_time, 2)}")
