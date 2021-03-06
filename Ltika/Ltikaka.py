import RPi.GPIO as GPIO
import time

led_pin = 2
time_sleep = 0.2
what_times = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(what_times):
    GPIO.output(led_pin,1)
    time.sleep(time_sleep)
    GPIO.output(led_pin,0)
    time.sleep(time_sleep)

GPIO.cleanup()
