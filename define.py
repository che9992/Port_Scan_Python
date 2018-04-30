import socket

def define_targets(args):
    ip_r = []
    if args[0] in ['0','1','2','3','4','5','6','7','8','9']:
        line = args.find('-')
        if line != -1:
            s = args[:line]
            ip_r.append(s.split('.')[0]+'.'+s.split('.')[1]+'.'+s.split('.')[2]+'.')
            ip_r.append(s.split('.')[3])
            s = args[line+1:]
            ip_r.append(s.split('.')[3])
        else:
            ip_r.append(args.split('.')[0]+'.'+args.split('.')[1]+'.'+args.split('.')[2]+'.')
            ip_r.append(args.split('.')[3])
            ip_r.append(args.split('.')[3])
    else:
        s = socket.gethostbyname(args)
        print(args +': ' +s)
        ip_r.append(s.split('.')[0] + '.' + s.split('.')[1] + '.' + s.split('.')[2] + '.')
        ip_r.append(s.split('.')[3])
        ip_r.append(s.split('.')[3])

    return ip_r


def define_range(args):
    ports = []
    line = args.find('-')
    if line != -1:
        ports.append(int(args[:line]))
        ports.append(int(args[line+1:]))
    else:
        ports.append(int(args))
        ports.append(int(args))
    return ports