import machine
import time

led_pin = machine.Pin(15, machine.Pin.OUT)

for i in range(5):
    led_pin.on()
    time.sleep(0.5)
    led_pin.off()
    time.sleep(0.5)
    
led_pin.off()
