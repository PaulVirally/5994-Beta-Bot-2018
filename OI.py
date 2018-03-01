from commands.Brake import Brake
from commands.ResetRevolutions import ResetRevolutions
from commands.PreciseDriveWithJoystick import PreciseDriveWithJoystick
from commands.Climb import Climb
from commands.Drop import Drop
from commands.StopClimb import StopClimb
from commands.RetractCube import RetractCube
from commands.SuckCube import SuckCube
from commands.WinchDown import WinchDown
from commands.WinchUp import WinchUp
from subsystems import Drivetrain
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

    # resetRevolutionsButton = JoystickButton(joystick, RobotMap.buttons.resetRevolutions)
    # resetRevolutionsButton.whenPressed(ResetRevolutions())

    preciseDriveButton = JoystickButton(joystick, RobotMap.buttons.preciseDrive)
    preciseDriveButton.whileHeld(PreciseDriveWithJoystick())

    # climbButton = JoystickButton(joystick, RobotMap.buttons.climb)
    # climbButton.whileHeld(Climb())

    # dropButton = JoystickButton(joystick, RobotMap.buttons.drop)
    # dropButton.whileHeld(Drop())

    # stopClimbButton = JoystickButton(joystick, RobotMap.buttons.stopClimb)
    # stopClimbButton.whileHeld(StopClimb())

    # suckCubeButton = JoystickButton(joystick, RobotMap.buttons.suckCube)
    # suckCubeButton.whileHeld(SuckCube())

    retractCubeButton = JoystickButton(joystick, RobotMap.buttons.retractCube)
    retractCubeButton.whileHeld(RetractCube())

    retractCubeButton2 = JoystickButton(joystick, RobotMap.buttons.retractCube2)
    retractCubeButton2.whileHeld(RetractCube())

    winchUpButton = JoystickButton(joystick, RobotMap.buttons.winchUp)
    winchUpButton.whileHeld(WinchUp())

    winchDownButton = JoystickButton(joystick, RobotMap.buttons.winchDown)
    winchDownButton.whileHeld(WinchDown())

def getJoyTurn():
    joyX = joystick.getRawAxis(0)
    t = joystick.getRawAxis(5) # 3
    joyZ = joystick.getRawAxis(4) # 2

    if abs(t) < abs(joyZ):
        return (joyX if abs(joyX) > abs(joyZ) else joyZ)
    return joyX

def getJoySpeed():
    return joystick.getRawAxis(1)

def getJoyElevatorSpeed():
    t = joystick.getRawAxis(5) # 3
    joyZ = joystick.getRawAxis(4) # 2

    if abs(t) > abs(joyZ):
        return t
    return 0

def rumble():
    joystick.setRumble(Joystick.RumbleType.kLeftRumble, 1)
    joystick.setRumble(Joystick.RumbleType.kRightRumble, 1)

def stopRumble():
    joystick.setRumble(Joystick.RumbleType.kLeftRumble, 0)
    joystick.setRumble(Joystick.RumbleType.kRightRumble, 0)

def getClawSpeeds():
    l = joystick.getRawAxis(2) # 4
    r = joystick.getRawAxis(3) # 5
    return ((l*2)-1, (r*2)-1)
    # return ((l+1)/2, (r+1)/2)

def getSpeedSmoothing():
    return wpilib.SmartDashboard.getNumber('Speed Sensitivity', RobotMap.defaults.speedSensitivity)

def getTurnSmoothing():
    return wpilib.SmartDashboard.getNumber('Turning Sensitivity', RobotMap.defaults.turningSensitivity)

def log():
    wpilib.SmartDashboard.putNumber('Speed Input', getJoySpeed())
    wpilib.SmartDashboard.putNumber('Rotate Input', getJoyTurn())