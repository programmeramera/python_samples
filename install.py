import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", "-U", package, "--user"])

def upgrade(package):
    subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", package])

upgrade("pip")
install("pygame")
