#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz archive
        from the contents of the web_static folder
        of your AirBnB Clone repo,
        using the function do_pack.
"""
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['18.233.67.178', '34.234.201.151']
def do_pack():
    """ function that converts the content of webstatic into a .tgz
    """
    d = datetime.now()
    now = d.strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    local("tar -czcf versions/web_static_{}.tgz web_static".format(now))


def do_deploy(archive_path):
	""" distributes an archive to your web servers
	"""
	if path.exists(archive_path):	
		archive = archive_path.split('/')[1]
		a_path = "/tmp/{}".format(archive)
		folder = archive.split('.')[0]
		f_path = "/data/web_static/releases/{}/".format(folder)
		
		put(archive_path, a_path)
		run("mkdir -p {}".format(f_path))
		run("tar -xzf {} -C {}".format(a_path, f_path))
		run("rm {}".format(a_path))
		run("mv -f {}web_static/* {}".format(f_path, f_path))
		run("rm -rf {}web_static".format(f_path))
		run("rm -rf /data/web_static/current")
		run("ln -s {} /data/web_static/current".format(f_path))
		return True 
	return False
