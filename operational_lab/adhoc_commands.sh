#!/bin/bash
# adhoc_commands.sh

# Install nginx (EL first) and ensure that it is set to start at boot

# First we upload the repo file for nginx
ansible all -i hosts -u root -m copy -a "src=nginx.repo dest=/etc/yum.repos.d/nginx.repo owner=root mode=0655"

# Install the RPM GPG Key
ansible all -i hosts -u root -m rpm_key -a "key=http://nginx.org/keys/nginx_signing.key"

# Now let's install the package
ansible all -i hosts -u root -m yum -a "name=nginx state=present"

# Last, enable the package to run at boot
ansible all -i hosts -u root -m service -a "name=nginx enabled=yes"
