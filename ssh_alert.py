#!/usr/bin/env python

import os
import time
import subprocess
import select
from pushb import send_pushbullet


def poll_logfile(filename):
    """
    Polls a logfile for sudo commands or ssh logins.
    """
    f = subprocess.Popen(["tail", "-F", "-n", "0", filename],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = select.poll()
    p.register(f.stdout)

    while True:
        if p.poll(1):
            process_log_entry(str(f.stdout.readline()))
        time.sleep(1)


def process_log_entry(logline):
    """
    Check a logline and see if it matches the content we care about.
    """
    send = False

    # If it's a local sudo exec
    if all(x in logline for x in ["sudo", "COMMAND"]):
        alert_type = "sudo"
        send = True

    # If it's an SSH login
    elif all(x in logline for x in ["ssh", "Accepted"]):
        alert_type = "ssh"
        send = True

    if send:
        send_pushbullet("ssh_alert from emby",
                        format_msg(alert_type, logline))


def format_msg(alert_type, logline):
    return '''ssh_alert from emby
    ---
    alert : {}
    ---
    {}
    '''.format(alert_type, logline)


# If this program was called directly (as opposed to imported)
if __name__ == "__main__":
    # poll the auth.log file
    poll_logfile("/var/log/auth.log")
