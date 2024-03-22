from machine import Pin
from time import sleep
import dht

sensor = dht.DHT22(Pin(15))
#sensor = dth.DTH11(Pin(15))

while True:
    try:
        sleep(2)
        sensor.measure()
        temp=sensor.temperature()
        hum = sensor.humidity()
        print( temp)
        print( hum)
    except OSError as e:
        print("Ni uspelo") 