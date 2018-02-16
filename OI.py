from commands.Brake import Brake
from commands.SetGyroAngle import SetGyroAngle
from commands.AutoTest import AutoTest
from commands.ResetRevolutions import ResetRevolutions
from commands.PreciseDriveWithJoystick import PreciseDriveWithJoystick
from commands.Record import Record
from commands.PlayBack import PlayBack
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

    setGyro45Button = JoystickButton(joystick, RobotMap.buttons.setGyro45)
    setGyro45Button.whenPressed(SetGyroAngle(90))

    # setDistance100 = JoystickButton(joystick, 10)
    # setDistance100.whenPressed(SetDistance(100))

    autoTestButton = JoystickButton(joystick, 12)
    autoTestButton.whenPressed(AutoTest())

    # lockStraightButton = JoystickButton(joystick, RobotMap.buttons.lockStraight)
    # lockStraightButton.whileHeld(LockStraight())
    
    # reverseDriveButton = JoystickButton(joystick, RobotMap.buttons.reverseDrive)
    # reverseDriveButton.whileHeld(ReverseDrive())
    
    # climbButton = JoystickButton(joystick, RobotMap.buttons.climb)
    # climbButton.whileHeld(Climb())
    # climbButton.whenReleased(HoldClimb())

    # stopClimbButton = JoystickButton(joystick, RobotMap.buttons.stopClimb)
    # stopClimbButton.whenPressed(StopClimb())

    # dropButton = JoystickButton(joystick, RobotMap.buttons.drop)
    # dropButton.whileHeld(Drop())

    resetRevolutionsButton = JoystickButton(joystick, RobotMap.buttons.resetRevolutions)
    resetRevolutionsButton.whenPressed(ResetRevolutions())

    preciseDriveButton = JoystickButton(joystick, RobotMap.buttons.preciseDrive)
    preciseDriveButton.whileHeld(PreciseDriveWithJoystick())

    centerRecordButton = JoystickButton(joystick, RobotMap.buttons.recordCenterAuto)
    centerRecordButton.whenPressed(Record('/home/lvuser/center_auto.auto'))

    playCenterButton = JoystickButton(joystick, RobotMap.buttons.playCenterAuto)
    playCenterButton.whileHeld(PlayBack('/home/lvuser/center_auto.auto'))

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