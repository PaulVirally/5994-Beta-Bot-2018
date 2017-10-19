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

drivetrain = {
    'frontLeftMotor'  : 0,
    'frontRightMotor' : 1,
    'rearLeftMotor'   : 2,
    'rearRightMotor'  : 3
}
drivetrain = dotdict(drivetrain)