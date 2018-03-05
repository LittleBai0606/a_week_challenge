from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/LittleBai0606/a_week_challenge.git"

env.user = 'root'
env.password = 'admin123BZP'

env.hosts = ['120.78.167.243']

env.port = '22'

def deploy():
    source_folder = '/home/baicai/sites/baicaicoder.online/django_blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py makemigrations &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('start gunicorn-baicaicoder.online')
    sudo('service nginx reload')
