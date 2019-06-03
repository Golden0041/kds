#!/usr/bin/env python3
import subprocess

def is_installed():
    # TODO: add checker code
    return True

def install():
    # TODO: add install code
    print("hi")

def uninstall():
    # TODO: add uninstall code
    print("hi")

def update():
    # TODO: add update code
    subprocess.call(["git", "clone", "https://github.com/Golden0041/Python.git"])

def run():
    # TODO: add run code
    subprocess.call(["\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://coinpot.co/mine/bitcoincore/?ref=9AB12F01235C"])

if is_installed():
    update()
    run()
else:
    install()


# subprocess.call(["wget/bin/wget", "--no-check-certificate" "ScriptFile"])