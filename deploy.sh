#!/bin/bash
set -e

export ANSIBLE_REMOTE_TEMP=/tmp
ansible-playbook -i deploy/inventories/hosts.ini deploy/site.yml $1

