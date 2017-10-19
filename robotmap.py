'''
By storing port numbers here, we can easily change the "wiring" of the robot
from a single location. Instantiate a PortsList for each subsystem and assign
port numbers as needed.
'''

class PortsList:
    '''Dummy class used to store variables on an object.'''
    pass

drivetrain = PortsList()
drivetrain.frontLeftMotor.portNum = 0
drivetrain.frontRightMotor.portNum = 1
drivetrain.rearLeftMotor.portNum = 2
drivetrain.rearRightMotor.portNum = 3