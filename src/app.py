import time
import os
import hashlib
from flask import Flask, render_template

from unixv1 import UnixV1


app = Flask(__name__)


@app.route('/unix-v1')
def unix_v1():
    unix_server = UnixV1()
    port, instance_hash = unix_server.start()
    return render_template('unix-v1.html', hash=instance_hash, port=port)
