from fabric import task

@task
def local_echo(c):
    c.run('echo "Hello, world!"', echo=True)
