from pyniryo import *

# This template lets the user define his own process, but it handles connection,
# calibration, tool equipping, and makes the robot go to sleep at the end:

local_mode = False  # Or True
tool_used = ToolID.GRIPPER_1
# Set robot address
robot_ip_address_rpi = "x.x.x.x"
robot_ip_address_local = "127.0.0.1"

robot_ip_address = robot_ip_address_local if local_mode else robot_ip_address_rpi


def process(niryo_edu):
    # --- YOUR CODE --- #
    pass


if __name__ == '__main__':
    # Connect to robot
    robot = NiryoRobot(robot_ip_address)
    # Calibrate robot if the robot needs calibration
    robot.calibrate_auto()
    # Equip tool
    robot.update_tool()
    # Launching the main process
    process(robot)
    # Ending
    robot.go_to_sleep()
    # Releasing connection
    robot.close_connection()
