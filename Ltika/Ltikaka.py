import RPi.GPIO as GPIO
import time

led_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin, True)
    time.sleep(1)
    GPIO.output(led_pin, False)
    time.sleep(1)

GPIO.cleanup()
