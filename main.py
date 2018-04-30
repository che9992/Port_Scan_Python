from threading import Thread
import define
import socket,argparse

counting_open = []
threads = []


W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
P = '\033[35m'  # purple
BOLD = '\033[1m'  # bold
THIN = '\033[1m'  # normal


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-target',
                        '-t',
                        type=str,
                        required = True,
                        help='ex) 0.0.0.0-0.0.0.50 or url ')

    parser.add_argument('-port',
                        '-p',
                        type=str,
                        required = True,
                        help='start port - finish port.')


    return parser


def port_check(target,port):
    s = socket.socket()
    s.settimeout(1)
    #socket.AF_INET, socket.SOCK_STREAM
    result = s.connect_ex((target, port))
    if result == 0:
        counting_open.append(port)
        s.close()
    else:
        s.close()

def scan(targets,ports):
    for t in range(int(targets[1]),int(targets[2])+1):

        if (ports[1]+1 - ports[0]) >=100:
            alot = True
        else:
            alot = False

        target = targets[0]+str(t)
        print(R + '[+] ' + 'scanning on ' + str(target) + W)

        for i in range(ports[0], ports[1]+1):
            t = Thread(target=port_check, args=(target,i))
            threads.append(t)

            if alot:
                if len(threads) >= 100:
                    for i in threads:
                        i.start()
                    for x in threads:
                        x.join()
                    threads.clear()

            elif alot == False:
                if len(threads) == (ports[1]+1 - ports[0]):
                    for i in threads:
                        i.start()
                    for x in threads:
                        x.join()
                    threads.clear()

        print('open ports {} in {}'.format(counting_open, target))
        counting_open.clear()


if __name__ == '__main__':
    print(R + '* * * * * * * * * * * * * * * * * *')
    print('* * * * * * Port Scanning * * * * *')
    print('* * * * *  Author: che9992  * * * *')
    print('* * * * * * * * * * * * * * * * * *'+W)

    args = argument_parser().parse_args()


targets = define.define_targets(args.target)
ports = define.define_range(args.port)
scan(targets,ports)