import RPi.GPIO as GPIO
import time

led_pin = 2
time_sleep = 0.02
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    GPIO.output(led_pin,1)
    time.sleep(time_sleep)
    GPIO.output(led_pin,0)
    time.sleep(time_sleep)

GPIO.cleanup()
