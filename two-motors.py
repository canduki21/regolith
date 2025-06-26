import RPi.GPIO as GPIO
import time

# Motor 1 pins (Azimuth motor)
ENA1 = 11
IN1_1 = 12
IN2_1 = 13

# Motor 2 pins (Elevation motor)
ENA2 = 24
IN1_2 = 25
IN2_2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup([ENA1, IN1_1, IN2_1, ENA2, IN1_2, IN2_2], GPIO.OUT)

def motor1_forward(duration=2):
    print("Motor 1 forward")
    GPIO.output(ENA1, GPIO.HIGH)
    GPIO.output(IN1_1, GPIO.HIGH)
    GPIO.output(IN2_1, GPIO.LOW)
    time.sleep(duration)
    stop_motor1()

def motor1_backward(duration=2):
    print("Motor 1 backward")
    GPIO.output(ENA1, GPIO.HIGH)
    GPIO.output(IN1_1, GPIO.LOW)
    GPIO.output(IN2_1, GPIO.HIGH)
    time.sleep(duration)
    stop_motor1()

def stop_motor1():
    print("Motor 1 stopped")
    GPIO.output(ENA1, GPIO.LOW)
    GPIO.output(IN1_1, GPIO.LOW)
    GPIO.output(IN2_1, GPIO.LOW)

def motor2_forward(duration=2):
    print("Motor 2 forward")
    GPIO.output(ENA2, GPIO.HIGH)
    GPIO.output(IN1_2, GPIO.HIGH)
    GPIO.output(IN2_2, GPIO.LOW)
    time.sleep(duration)
    stop_motor2()

def motor2_backward(duration=2):
    print("Motor 2 backward")
    GPIO.output(ENA2, GPIO.HIGH)
    GPIO.output(IN1_2, GPIO.LOW)
    GPIO.output(IN2_2, GPIO.HIGH)
    time.sleep(duration)
    stop_motor2()

def stop_motor2():
    print("Motor 2 stopped")
    GPIO.output(ENA2, GPIO.LOW)
    GPIO.output(IN1_2, GPIO.LOW)
    GPIO.output(IN2_2, GPIO.LOW)

try:
    motor1_forward(3)
    time.sleep(1)
    motor1_backward(3)
    time.sleep(1)
    motor2_forward(3)
    time.sleep(1)
    motor2_backward(3)
finally:
    stop_motor1()
    stop_motor2()
    GPIO.cleanup()
