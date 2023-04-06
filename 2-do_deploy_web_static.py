#!/usr/bin/python3
"""A fabric script to send an archive file to a remote server
and decompress it"""

from fabric.api import run, env, put
import os.path

env.hosts = ['18.207.234.171', '35.153.226.243']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """A function to deploy code and decompress it"""

    if not os.path.isfile(archive_path):
        return False
    compressed_file = archive_path.split("/")[-1]
    no_extension = compressed_file.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(no_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir - p {}".format(remote_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_file, remote_path))
        run("sudo rm /tmp/{}".format(compressed_file))
        run("sudo ln -sf {} {}".format(remote_path, sym_link))
        return True
    except Exception as e:
        return False
