so simple.

## port scanner as python
my environment
 - OS X
 - Python 3.6.4 with Pycharm

### Usage::

you can input target as ip
```bash

$ python main.py -t 192.168.5.1-192.168.5.10 -p 0-300


[+] scanning on 192.168.5.1
open ports [80, 110, 143] in 192.168.5.1
[+] scanning on 192.168.5.2
open ports [80, 110, 143] in 192.168.5.2
[+] scanning on 192.168.5.3
open ports [80, 110, 143] in 192.168.5.3
[+] scanning on 192.168.5.4
open ports [80, 110, 143] in 192.168.5.4
[+] scanning on 192.168.5.5
open ports [80, 110, 143] in 192.168.5.5

```
you can also input target as url
```bash

$ python main.py -t www.naver.com -p 0-300


www.naver.com: 125.209.222.141
[+] scanning on 125.209.222.141
open ports [80, 110, 143] in 125.209.222.141

```
