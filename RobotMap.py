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

# Button mapping for the joystick
buttons = {
    'brake'            : 1,
    'climb'            : 5,
    'drop'             : 3,
    'stopClimb'        : 4,
    'preciseDrive'     : 7,
    'resetRevolutions' : 5,
    'suckCube'         : 12,
    'retractCube'      : 11,
    'winchUp'          : 10,
    'winchDown'        : 9
}
buttons = dotdict(buttons)

# Drivetrain motor assignment
drivetrain = {
    'frontLeftMotor'  : 4,
    'frontRightMotor' : 3,
    'rearLeftMotor'   : 2,
    'rearRightMotor'  : 0
}
drivetrain = dotdict(drivetrain)

# Elevator motor assignment
elevator = {
    'motor' : 3,
    'pos0'  : 0,
    'pos1'  : 1,
    'pos2'  : 2,
    'pos3'  : 3,
    'pos4'  : 4
}
elevator = dotdict(elevator)

# Claw motor assignments
claw = {
    'leftMotor'  : 2,
    'rightMotor' : 1,
    'winchMotor' : 1
}
claw = dotdict(claw)

# Default parameters assignment
defaults = {
    'speedSensitivity'   : 1.5,
    'turningSensitivity' : 1.5
}
defaults = dotdict(defaults)