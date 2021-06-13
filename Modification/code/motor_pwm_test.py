import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 57)
dc = 9
p.ChangeDutyCycle(dc)
p.start(0)
try:
    while 1:
        for i in range(9):
            dc = 9
            p.ChangeDutyCycle(dc)
            time.sleep(0.03)
        dc = 7
        p.ChangeDutyCycle(dc)
        print(dc)
        time.sleep(0.03)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
print('program exit')

