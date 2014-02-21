#!/bin/bash
# adhoc_commands.sh

# Install nginx (EL first) and ensure that it is set to start at boot

# First we upload the repo file for nginx
ansible -i hosts -u root -m copy -a "src=nginx.repo dest=/etc/yum.repos.d/nginx.repo owner=root mode=0655" labserver

# Now let's install the package 
ansible -i hosts -u root -m yum -a "name=nginx state=present" labserver

# Last, enable the package to run at boot
anisible -i hosts -u root -m service -a "name=nginx enabled=yes"
