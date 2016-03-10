from __future__ import with_statement
from fabric.api import *
import os

def stop():
    local('docker-compose -f docker-compose.yml -f docker-compose.production.yml -p metrics stop')

def up():
    if not os.environ.get('PRE_CREATE_DB'):
        raise "PRE_CREATE_DB must be set"
    if not os.environ.get('GF_SECURITY_ADMIN_USER'):
        raise "GF_SECURITY_ADMIN_USER must be set"
    if not os.environ.get('GF_SECURITY_ADMIN_PASSWORD'):
        raise "GF_SECURITY_ADMIN_PASSWORD must be set"

    local('docker-compose -f docker-compose.yml -f docker-compose.production.yml -p metrics up -d')
