#!/usr/bin/env python3
"""
Write a Fabric script that generates a .tgz archive
        from the contents of the web_static folder
        of your AirBnB Clone repo,
        using the function do_pack.
"""
from datetime import datetime
from fabric import task

@task
def do_pack():
    """ function that converts the content of webstatic into a .tgz
    """
    d = datetime.now()
    now = d.strftime("%Y&m%d%H%M%S")

    c.run("mkdir -p versions")
    c.run("tar -czcf versions/web_static_{} web_static".format(now))
