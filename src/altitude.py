import time
import socket

CARBON_SERVER = 'localhost'
CARBON_PORT = 2003
    
def handleAltitude(dataArray):
    altitude = dataArray[3]
    print(f"Altitude (m): {altitude}")
    message = f'bmp.altitude {altitude} {int(time.time())}\n'
    print(message)
    encodedMessage = bytes(message, 'utf-8')
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    sock.sendall(encodedMessage)
    sock.close()
