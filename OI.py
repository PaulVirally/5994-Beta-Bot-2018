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

    resetRevolutionsButton = JoystickButton(joystick, RobotMap.buttons.resetRevolutions)
    resetRevolutionsButton.whenPressed(ResetRevolutions())

    preciseDriveButton = JoystickButton(joystick, RobotMap.buttons.preciseDrive)
    preciseDriveButton.whileHeld(PreciseDriveWithJoystick())

    climbButton = JoystickButton(joystick, RobotMap.buttons.climb)
    climbButton.whileHeld(Climb())

    dropButton = JoystickButton(joystick, RobotMap.buttons.drop)
    dropButton.whileHeld(Drop())

    stopClimbButton = JoystickButton(joystick, RobotMap.buttons.stopClimb)
    stopClimbButton.whileHeld(StopClimb())

    suckCubeButton = JoystickButton(joystick, RobotMap.buttons.suckCube)
    suckCubeButton.whileHeld(SuckCube())

    retractCubeButton = JoystickButton(joystick, RobotMap.buttons.retractCube)
    retractCubeButton.whileHeld(RetractCube())

    winchUpButton = JoystickButton(joystick, RobotMap.buttons.winchUp)
    winchUpButton.whileHeld(WinchUp())

    winchDownButton = JoystickButton(joystick, RobotMap.buttons.winchDown)
    winchDownButton.whileHeld(WinchDown())

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