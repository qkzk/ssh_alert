# ssh alert


# Principle

send pushbullet notifications to your phone when someone logs in
your server

# Installation

1. clone this repo
2. Install the requirements

    ```bash
    $ pip install -r requirements.txt
    ```

3.  Create a file called `token` containing your
    [pushbullet API key](https://www.pushbullet.com/#settings/account).

4.  **Change the folders in the service file.**
5.  Then just copy the service to correct place

    ```bash
    $ cp ssh_alert.service /lib/systemd/system/
    $ sudo systemctl enable ssh_alert.service
    $ sudo systemctl start ssh_alert.service
    ```

6.  Check if it hasn't crashed

    ```bash
    $ systemctl status ssh_alert.service
    ```



Then ssh to your server (or sudo) and you should get a pushbullet notification


# Credits

* It uses the wonderfull package [pushbullet.py](https://github.com/rbrcsk/pushbullet.py)

* Inspiration (and part of code) comes from [ssh_alert](https://github.com/groovemonkey/sshalert)

* Check his videos : [tutorial linux](https://www.youtube.com/channel/UCvA_wgsX6eFAOXI8Rbg_WiQ)
