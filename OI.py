from commands.Brake import Brake
from commands.LockStraight import LockStraight
from commands.ReverseDrive import ReverseDrive
from commands.Climb import Climb
from commands.HoldClimb import HoldClimb
from commands.StopClimb import StopClimb
from commands.Drop import Drop
from commands.PlayBack import PlayBack
# from commands.PreciseDriveWithJoystick import PreciseDriveWithJoystick
from commands.Record import Record
import wpilib
from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

import RobotMap

joystick = None

def init():
    '''
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    '''

    global joystick

    joystick = Joystick(0)

    brakeButton = JoystickButton(joystick, RobotMap.buttons.brake)
    brakeButton.whileHeld(Brake())

    lockStraightButton = JoystickButton(joystick, RobotMap.buttons.lockStraight)
    lockStraightButton.whileHeld(LockStraight())
    
    reverseDriveButton = JoystickButton(joystick, RobotMap.buttons.reverseDrive)
    reverseDriveButton.whileHeld(ReverseDrive())
    
    climbButton = JoystickButton(joystick, RobotMap.buttons.climb)
    climbButton.whileHeld(Climb())
    climbButton.whenReleased(HoldClimb())

    stopClimbButton = JoystickButton(joystick, RobotMap.buttons.stopClimb)
    stopClimbButton.whenPressed(StopClimb())

    dropButton = JoystickButton(joystick, RobotMap.buttons.drop)
    dropButton.whileHeld(Drop())

    # TODO:
    # preciseDriveButton = JoystickButton(joystick, RobotMap.buttons.preciseDrive)
    # preciseDriveButton.whileHeld(PreciseDriveWithJoystick())

    centerRecordButton = JoystickButton(joystick, RobotMap.buttons.recordCenterAuto)
    centerRecordButton.whenPressed(Record('center_auto.auto'))

    playCenterButton = JoystickButton(joystick, RobotMap.buttons.playCenterAuto)
    playCenterButton.whileHeld(PlayBack('center_auto.auto'))

def getJoyTurn():
    joyX = joystick.getX()
    joyZ = joystick.getZ()
    return (joyX if abs(joyX) > abs(joyZ) else joyZ)

def getJoySpeed():
    return joystick.getY()

def getSpeedSmoothing():
    return wpilib.SmartDashboard.getNumber('Speed Sensitivity', RobotMap.defaults.turningSensitivity)

def getTurnSmoothing():
    return wpilib.SmartDashboard.getNumber('Turning Sensitivity', RobotMap.defaults.turningSensitivity)

def log():
    wpilib.SmartDashboard.putNumber('Speed Input', getJoySpeed())
    wpilib.SmartDashboard.putNumber('Rotate Input', getJoyTurn())
    wpilib.SmartDashboard.putNumber('Speed Sensitivity', RobotMap.defaults.speedSensitivity)
    wpilib.SmartDashboard.putNumber('Turning Sensitivity', RobotMap.defaults.turningSensitivity)