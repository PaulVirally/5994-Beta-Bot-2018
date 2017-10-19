import wpilib
from wpilib.command.subsystem import Subsystem

from commands.smoothfollowjoystick import SmoothFollowJoystick
import robotmap

class Drivetrain(Subsystem):
    '''
    This is the drivetrain subsystem
    '''

    def __init__(self):
        '''Instantiates the drivetrain object.'''

        super().__init__('Drivetrain')

        self.drivetrain = wpilib.RobotDrive(robotmap.drivetrain.frontLeftMotor, robotmap.drivetrain.rearLeftMotor,
                                            robotmap.drivetrain.frontRightMotor, robotmap.drivetrain.rearRightMotor)


    def drive(self, moveValue, rotateValue):
        '''Arcade drive'''
        self.drivetrain.arcadeDrive(moveValue, rotateValue)

    def stop(self):
        self.drivetrain.stopMotor()

    def initDefaultCommand(self):
        self.setDefaultCommand(SmoothFollowJoystick())