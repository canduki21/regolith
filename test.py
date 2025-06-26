import time
import board
import busio
import adafruit_bno055

# Create UART connection (uses GPIO14=TXD, GPIO15=RXD)
uart = busio.UART(board.TX, board.RX, baudrate=115200)

# Initialize BNO055 over UART
sensor = adafruit_bno055.BNO055_UART(uart)

print("BNO055 IMU Test over UART")
print("-------------------------")

while True:
    try:
        euler = sensor.euler  # (heading, roll, pitch)
        temp = sensor.temperature

        if euler:
            print(f"Heading: {euler[0]:.2f}°, Roll: {euler[1]:.2f}°, Pitch: {euler[2]:.2f}° | Temp: {temp}°C")
        else:
            print("Waiting for data...")
        time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nExiting...")
        break
