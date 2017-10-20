'''
By storing port numbers here, we can easily change the "wiring" of the robot
from a single location. Instantiate a PortsList for each subsystem and assign
port numbers as needed.
'''

# Pretty neat trick https://stackoverflow.com/a/23689767/6026013
class dotdict(dict):
    '''dot.notation access to dictionary attributes'''
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

buttons = {
    'brake'            : 1,
    'lockStraight'     : 2,
    'reverseDrive'     : 5,
    'climb'            : 6,
    'stopClimb'        : 4,
    'drop'             : 8,
    'preciseDrive'     : 7,
    'recordCenterAuto' : 11,
    'recordLeftAuto'   : 10
}
buttons = dotdict(drivetrain)

drivetrain = {
    'frontLeftMotor'  : 0,
    'frontRightMotor' : 1,
    'rearLeftMotor'   : 2,
    'rearRightMotor'  : 3
}
drivetrain = dotdict(drivetrain)