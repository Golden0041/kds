#!/usr/bin/env python3
import subprocess
import os.path

def is_installed():
    # TODO: add checker code
    return(os.path.exists(os.getenv("APPDATA") + "/Microsoft/Windows/Start Menu/Programs/Startup/kds"))

def install():
    # TODO: add install code
    print("Installing...")

def uninstall():
    # TODO: add uninstall code
    print("Uninstalling...")

def update():
    # TODO: add update code
    subprocess.call(["git", "pull"])

def run():
    # TODO: add run code
    subprocess.call(["\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://coinpot.co/mine/bitcoincore/?ref=9AB12F01235C"])

if is_installed():
    update()
    run()
else:
    install()


# subprocess.call(["wget/bin/wget", "--no-check-certificate" "ScriptFile"])
# %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup