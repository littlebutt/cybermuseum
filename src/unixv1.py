import random
import time
import hashlib
import os
import subprocess

from typing import Tuple


class UnixV1:

    def start(self) -> Tuple[int, str]:
        timestamp = time.time()
        md5 = hashlib.md5()
        md5.update(repr(timestamp).encode())
        instance_hash = md5.hexdigest()
        port = self.find_port()
        p = subprocess.Popen(['tmux', 'new', '-s', instance_hash, '-d'])
        p = subprocess.Popen(f'tmux send -t {instance_hash} "cd /home/www" Enter', shell=True)
        p = subprocess.Popen(['tmux', 'send', '-t', instance_hash, 'ttyd', '-p', '8089', 'bash', 'Enter'], stdout=subprocess.DEVNULL)
        print(f'port={port} instance_hash={instance_hash}')
        return port, instance_hash

    def find_port(self) -> int:
        cmd = "netstat -ntl | grep -v Active | grep -v Proto | awk '{print $4}' | awk -F: '{print $NF}'"
        procs = os.popen(cmd).read()
        port = random.randint(1024, 49151)
        if port in procs.split('\n'):
            return self.find_port()
        else:
            return port
