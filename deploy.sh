#!/bin/bash
set -e


export ANSIBLE_REMOTE_TEMP=/tmp
ansible-playbook -i deploy/host deploy/main.yml

