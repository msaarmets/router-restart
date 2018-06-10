# router-restart

A simple GUI python application to restart wifi-routers without leaving your couch.

It connects to the router via wifi, using Selenium and Chrome/Firefox WebDrivers with headless options enabled.
The application logs in and issues the reboot command.

It's quite specific and works only if you have Thomson and DIR wifi-routers. Most likely it's not gonna work for you unless you modify the code.

You can use "RouterRestart.spec" to create .exe using [PyInstaller](https://pyinstaller.readthedocs.io/en/v3.3.1/index.html):

`pyinstaller RouterRestart.spec -F -y --name RouterRestart`

To install dependencies use:

`pip install -r requirements.txt`

![screenshot](screenshots/py_restart.JPG)
