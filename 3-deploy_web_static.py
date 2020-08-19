#!/usr/bin/python3
"""Auto deploys"""


import os
from fabric.operations import local, run, put, env
from datetime import datetime


env.hosts = ['34.75.76.240', '35.229.102.53']


def do_pack():
    """C0mpress"""
    filename = 'web_static_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.tgz'
    try:
        if not os.path.isdir('versions'):
            local('mkdir versions')

        return local('tar -cvzf versions/{} web_static'.format(filename))
    except Exception:
        return None


def do_deploy(archive_path):
    """Deplys"""

    if not os.path.exists(archive_path):
        return False

    name = archive_path.split('/')[-1]

    untar = "/data/web_static/releases/{}".format(name.replace('.tgz', ''))

    put(archive_path, '/tmp')
    run('mkdir -p ' + untar)
    run('tar -xzf /tmp/{} -C {}'.format(name, untar))
    run('rm /tmp/{}'.format(name))
    run("mv {}/web_static/* {}".format(untar, untar))
    run("rm -rf {}/web_static".format(untar))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(untar))
    return True


def deploy():
    """Call deploy"""
    p = do_pack()
    if not p:
        return False
    return do_deploy(p)
