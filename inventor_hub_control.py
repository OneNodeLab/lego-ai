from pybricks.tools import StopWatch
from pybricks.hubs import InventorHub
from pybricks.parameters import Port
from pybricks.pupdevices import Motor
import urandom

# Connect to the Inventor Hub
hub = InventorHub()

# Initialize the motor on port A
motor = Motor(Port.A)

# Function to perform the motor sequence
def motor_sequence():
    while True:
        # Go to the initial position at 180 degrees
        motor.run_target(500, 180)
        # Wait for 2 seconds
        stopwatch = StopWatch()
        while stopwatch.time() < 2000:
            pass

        # Turn clockwise a random angle between 30 and 90 degrees
        angle_cw = urandom.randint(30, 90)
        motor.run_angle(500, angle_cw)
        # Wait for 2 seconds
        stopwatch = StopWatch()
        while stopwatch.time() < 2000:
            pass

        # Turn counterclockwise a random angle between 30 and 90 degrees
        angle_ccw = urandom.randint(30, 90)
        motor.run_angle(500, -angle_ccw)
        # Wait for 2 seconds
        stopwatch = StopWatch()
        while stopwatch.time() < 2000:
            pass

# Start the motor sequence
motor_sequence()
