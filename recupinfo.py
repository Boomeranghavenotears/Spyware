import socket
import os, platform
import requests
name = socket.gethostname()
os_name = os.name
cpu = os.cpu_count()
system = platform.system()
release = platform.release()
architechture = platform.architecture()
hostname = socket.gethostname()
ip = socket.gethostbyname_ex(hostname)
publicip = requests.get('https://api.ipify.org').text


print("Software informations:")
print("os: " + os_name)
print("System: ", system + " " + release)
print("Release: " + release)
print("Architecture: ", architechture)
print("PC user name: " + name)
print("IP adress: ", ip[2], "Router ip/Public IP: " + publicip)
print()
print("Hardware informations:")
print("CPU count: ", cpu)
input(" ")


