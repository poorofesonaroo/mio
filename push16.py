import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin=16
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(9)
pwm.ChangeDutyCycle(9)
time.sleep(2)
pwm.ChangeDutyCycle(3)
time.sleep(0.1)
pwm.stop()
GPIO.cleanup()
