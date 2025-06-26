import time
import board
import busio
import adafruit_bno055

# Set up I2C connection
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize BNO055 sensor
sensor = adafruit_bno055.BNO055_I2C(i2c)

print("BNO055 IMU Test")
print("---------------------")

while True:
    try:
        # Euler angles: (heading, roll, pitch)
        euler = sensor.euler
        temp = sensor.temperature

        if euler is not None:
            print(f"Heading: {euler[0]:.2f}°, Roll: {euler[1]:.2f}°, Pitch: {euler[2]:.2f}° | Temp: {temp}°C")
        else:
            print("Waiting for IMU data...")

        time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nExiting...")
        break
