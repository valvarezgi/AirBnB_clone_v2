#!/usr/bin/python3
"""Distributes"""

import os
from fabric.operations import local, run, put, env
from datetime import datetime


env.hosts = ['34.75.76.240', '35.229.102.53']


def do_deploy(archive_path):
    """Deploys"""

    if not os.path.exists(archive_path):
        return False

    name = archive_path.split('/')[-1]

    tar = "/data/web_static/releases/{}".format(name.replace('.tgz', ''))

    put(archive_path, '/tmp')
    run('mkdir -p ' + tar)
    run('tar -xzf /tmp/{} -C {}'.format(name, tar))
    run('rm /tmp/{}'.format(name))
    run("mv {}/web_static/* {}".format(tar, tar))
    run("rm -rf {}/web_static".format(tar))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(tar))
