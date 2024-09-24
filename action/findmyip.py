import socket
from speech_.TTS import *

def ip():
    host = socket.gethostname()
    IPAddr = "Your Computer IP Address is:" + socket.gethostbyname(host)+"."
    TTS_en(IPAddr)
