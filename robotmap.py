'''
By storing port numbers here, we can easily change the "wiring" of the robot
from a single location. Instantiate a PortsList for each subsystem and assign
port numbers as needed.
'''

class PortsList:
    '''Dummy class used to store variables on an object.'''
    pass

frontLeftMotor = PortsList()
frontLeftMotor.portNum = 0

rearLeftMotor = PortsList()
rearLeftMotor.portNum = 1

frontRightMotor = PortsList()
frontRightMotor.portNum = 2

rearRightMotor = PortsList()
rearRightMotor.portNum = 3
