import wpilib
from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.crash import Crash

joystick = None
shouldRecord = False

def init():
    '''
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    '''

    global joystick

    joystick = Joystick(0)

    trigger = JoystickButton(joystick, Joystick.ButtonType.kTrigger)
    trigger.whenPressed(Crash())

def getJoyTurn():
    joyX = joystick.getX()
    joyZ = joystick.getZ()
    return (joyX if abs(joyX) > abs(joyZ) else joyZ)

def getJoySpeed():
    return joystick.getY()

def log():
    wpilib.SmartDashboard.putNumber('Speed Input', getJoySpeed())
    wpilib.SmartDashboard.putNumber('Rotate Input', getJoyTurn())