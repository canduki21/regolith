import RPi.GPIO as GPIO
import time

# Motor pins (change if needed)
ENA = 11
IN1 = 12
IN2 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def motor_forward(duration=2):
    print("Motor forward")
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    time.sleep(duration)
    stop_motor()

def motor_backward(duration=2):
    print("Motor backward")
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    time.sleep(duration)
    stop_motor()

def stop_motor():
    print("Motor stopped")
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

try:
    motor_forward(3)    # run forward for 3 seconds
    time.sleep(1)
    motor_backward(3)   # run backward for 3 seconds
    time.sleep(1)
finally:
    stop_motor()
    GPIO.cleanup()
