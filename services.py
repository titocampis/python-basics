import platform
from subprocess import run, PIPE
from unittest import TestCase

class Server:
    def __init__(self, name, ips):
        self.name = name
        self.ips = ips

def pingto(timeout, ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    cmd = ('ping',param,'1', '-w', str(timeout), str(ip))
    res = run(cmd, stdout=PIPE, stderr=PIPE)
    return (res.returncode==0, res.stderr)

