#!/usr/bin/env python3
import  sys
import subprocess
import os.path
import shutil

action = sys.argv[1]

kds_path = os.getenv("APPDATA") + "/Microsoft/Windows/Start Menu/Programs/Startup/kds"

def is_installed():
    # TODO: add checker code
    return(os.path.exists(kds_path))

def install():
    # TODO: add install code
    print("Installing...")
    shutil.copytree(".", kds_path)
    print("Installation finished.")

def uninstall():
    # TODO: add uninstall code
    print("Uninstalling...")
    shutil.rmtree(kds_path)

def update():
    # TODO: add update code
    print("Updating...")
    subprocess.call(["git", "pull"])

def run():
    # TODO: add run code
    subprocess.call(["\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://coinpot.co/mine/bitcoincore/?ref=9AB12F01235C"])

if action == "--install":
    if is_installed():
        update()
        run()
    else:
        install()
elif (action == "--uninstall") & is_installed():
    uninstall()
else:
    run()

