#!/usr/bin/env python3

import socket
import time
import board
import neopixel

HOST = '192.168.1.201'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

pixelCount = 500
pixels = neopixel.NeoPixel(board.D21, pixelCount, brightness=1, auto_write=False, pixel_order=neopixel.GRB)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            stringdata = data.decode('utf-8')

            if stringdata.startswith("ALLON"):
                print ("ALLON")
                pixels.fill([255, 255, 255])
                pixels.show()

            if stringdata.startswith("ALLOFF"):
                print("ALLOFF")
                pixels.fill([0, 0, 0])
                pixels.show()

            if stringdata.startswith("ON "):
                print("ON")
                stringIndex = stringdata.replace("ON ","")
                
                pixels.fill([0, 0, 0])
                pixels[int(stringIndex)] = [255,255,255]
                pixels.show()

            
            if not data:
                break
            conn.sendall(data)
