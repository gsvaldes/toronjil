from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, put
from fabric.contrib.console import confirm

code_dir = '/home/django/toronjil'

def update_remote():
    with cd(code_dir):
        run('git pull origin master')

def create_remote_test_file():
    with cd(code_dir):
        run('touch hello.txt')

def move_local_settings():
    with cd(code_dir):
        put('toronjil/local_settings.py', 'toronjil')

def move_nginx_config():
    with cd('/etc/nginx/'):
        put('nginx', 'sites-available/toronjil')

def move_upstart_config():
    with cd('/etc/'):
        put('upstart', 'init/toronjil.conf')
        


