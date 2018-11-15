import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
try:
    GPIO.output(18, GPIO.LOW)
    time.sleep(5);
    GPIO.output(18, GPIO.HIGH)
    GPIO.cleanup()
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
