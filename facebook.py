#!/usr/bin/env python3
"""Facebook

Control access to Facebook with a simple on and off switch

Usage:
    facebook COMMAND

Commands:
    block  Blocks all facebook hosts
    allow  Allows facebook traffic
"""
from tempfile import mkstemp
from docopt import docopt
from shutil import move
import os
from os import remove

fb_hosts = [
    'www.facebook.com', 'facebook.com', 'www.messenger.com', 'messenger.com'
]


def remove_facebook_hosts():
    hosts_path = '/etc/hosts'
    fh, temp_hosts = mkstemp()

    with open(hosts_path) as old, open(fh, 'w') as new:
        for line in old:
            if not any(fb in line for fb in fb_hosts):
                new.write(line)
    remove(hosts_path)
    move(temp_hosts, hosts_path)
    os.chmod(hosts_path, 0o644)


def add_facebook_hosts():
    with open('/etc/hosts', 'a') as host:
        for fb in fb_hosts:
            host.write('{}      {}\n'.format('0.0.0.0', fb))


if __name__ == "__main__":
    args = docopt(__doc__, options_first=True)

    if args['COMMAND'] == 'allow':
        remove_facebook_hosts()
    elif args['COMMAND'] == 'block':
        remove_facebook_hosts()
        add_facebook_hosts()
