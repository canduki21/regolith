import time
import board
import busio
import ephem
import adafruit_bno055
import RPi.GPIO as GPIO
import datetime

# === SETTINGS ===
LAT = 28.0614     # Your latitude
LON = -80.6233    # Your longitude
AZ_PINS = (17, 18)  # Azimuth motor control pins
EL_PINS = (22, 23)  # Elevation motor control pins
TOLERANCE_DEG = 2  # How precise alignment should be

# === SETUP BNO055 ===
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

# === SETUP GPIO ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(AZ_PINS + EL_PINS, GPIO.OUT)

def rotate_motor(pin1, pin2, direction='forward', duration=0.1):
    if direction == 'forward':
        GPIO.output(pin1, GPIO.HIGH)
        GPIO.output(pin2, GPIO.LOW)
    else:
        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)

# === SUN POSITION ===
def get_sun_position(lat, lon):
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)
    observer.date = datetime.datetime.utcnow()
    sun = ephem.Sun(observer)
    return float(sun.az), float(sun.alt)

# === ORIENTATION ===
def get_orientation():
    euler = sensor.euler  # (heading, roll, pitch)
    if euler and euler[0] is not None and euler[2] is not None:
        azimuth = euler[0]
        elevation = euler[2]
        return azimuth, elevation
    return None, None

# === ALIGN MOTOR TO SUN ===
def align_to_sun():
    sun_az, sun_el = get_sun_position(LAT, LON)
    print(f"Sun Position → Azimuth: {sun_az:.2f}°, Elevation: {sun_el:.2f}°")

    current_az, current_el = get_orientation()
    if current_az is None or current_el is None:
        print("Waiting for valid IMU data...")
        return

    print(f"Current Orientation → Azimuth: {current_az:.2f}°, Elevation: {current_el:.2f}°")

    # Adjust Azimuth
    if abs(current_az - sun_az) > TOLERANCE_DEG:
        if (current_az - sun_az) % 360 > 180:
            rotate_motor(*AZ_PINS, 'forward', 0.2)
            print("Rotating AZ forward")
        else:
            rotate_motor(*AZ_PINS, 'backward', 0.2)
            print("Rotating AZ backward")

    # Adjust Elevation
    if abs(current_el - sun_el) > TOLERANCE_DEG:
        if current_el < sun_el:
            rotate_motor(*EL_PINS, 'forward', 0.2)
            print("Tilting EL forward")
        else:
            rotate_motor(*EL_PINS, 'backward', 0.2)
            print("Tilting EL backward")

# === MAIN LOOP ===
try:
    while True:
        align_to_sun()
        time.sleep(10)  # Track every 10 seconds

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()
