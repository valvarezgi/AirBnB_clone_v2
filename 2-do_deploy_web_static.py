#!/usr/bin/python3
"""Distributes an archive to the web servers"""
from datetime import datetime
from fabric.api import env, local, put, run
from os.path import exists

env.hosts = ['34.75.76.240', '35.229.102.53']


def do_pack():
    """"Makes a pack of directory on local"""

    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    final = 'versions/web_static_{}.tgz'.format(date)

    try:
        local('tar -czvf {} web_static'.format(final))
        return final
    except:
        return None


def do_deploy(archive_path):
        """Distributes files to web servers"""
        if not exists(archive_path):
            return False
        try:
            put(archive_path, '/tmp/')
            base = archive_path.split('/')[-1]
            extent = base.split('.')[0]
            release = '/data/web_static/releases/'
            curren = '/data/web_static/current'
            run('mkdir -p {}{}/'.format(release, extent))
            run('tar -xzf /tmp/{} -C {}{}/'.format(base, release, extent))
            run('rm /tmp/{}'.format(base))
            run('mv{1}{0}/web_static/*{1}{0}/'.format(extent, release))
            run('rm -rf {}{}/web_static'.format(release, extent))
            run('rm -rf {}'.format(curren))
            run('ln -fs {}{}/ {}'.format(release, extent, curren))
            return True
        except:
            return False
