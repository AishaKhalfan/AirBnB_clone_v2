#!/usr/bin/python3
"""a script to send an archive file to a remote server
and decompress it"""

from fabric.api import run, env, put
import os.path
from fabric import Connection

env.hosts = ['18.207.234.171', '35.153.226.243']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'

def do_deploy(archive_path):
    """a function to deploy code and decompress it"""
    
    if not os.path.isfile(archive_path):
        return False
    compressed_file = archive_path.split("/")[-1]
    no_extension = compressed_file.split(".")[0]
    
    for host in env.hosts:
        with Connection(host) as c:
            try:
                remote_path = "/data/web_static/releases/{}".format(no_extension)
                sym_link = "/data/web_static/current"
                c.put(archive_path, "/tmp/")
                c.run("sudo mkdir - p {}".format(remote_path))
                c.run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file, remote_path))
                c.run("sudo rm /tmp/{}".format(compressed_file))
                c.run("sudo ln -sf {} {}".format(remote_path, sym_link))
                return True
            except Exception as e:
                return False
