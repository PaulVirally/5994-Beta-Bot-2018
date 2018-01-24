import wpilib
import ctre
from wpilib.command.subsystem import Subsystem

from commands.SmoothFollowJoystick import SmoothFollowJoystick
import RobotMap
import subsystems

class Drivetrain(Subsystem):
    '''
    This is the drivetrain subsystem
    '''

    def __init__(self):
        '''Instantiates the drivetrain object.'''

        super().__init__('Drivetrain')

        self.frontLeftMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.frontLeftMotor)
        self.frontRightMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.frontRightMotor)
        self.rearLeftMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.rearLeftMotor)
        self.rearRightMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.rearRightMotor)

        self.drivetrain = wpilib.RobotDrive(self.frontLeftMotor, self.rearLeftMotor,
                                            self.frontRightMotor, self.rearRightMotor)
                                            
        self.drivetrain.setInvertedMotor(RobotMap.drivetrain.frontLeftMotor, True)
        self.drivetrain.setInvertedMotor(RobotMap.drivetrain.rearLeftMotor, False)
        self.drivetrain.setInvertedMotor(RobotMap.drivetrain.frontRightMotor, True)
        self.drivetrain.setInvertedMotor(RobotMap.drivetrain.rearRightMotor, False)

        self.lastMoveValue = 0
        self.lastRotateValue = 0

        self.gyro = wpilib.ADXRS450_Gyro()

    def drive(self, moveValue, rotateValue):
        '''Arcade drive'''
        self.drivetrain.arcadeDrive(moveValue, rotateValue)
        self.lastMoveValue = moveValue
        self.lastRotateValue = rotateValue

    def stop(self):
        self.drive(0, 0)

    def initDefaultCommand(self):
        self.setDefaultCommand(SmoothFollowJoystick())

    def getSpeed(self):
        return self.lastMoveValue

    def getRotate(self):
        return self.lastRotateValue

    def getAngle(self):
        return self.gyro.getAngle()

    def getRotationRate(self):
        return self.gyro.getRate()

    def log(self):
        wpilib.SmartDashboard.putNumber('Speed Output', self.getSpeed())
        wpilib.SmartDashboard.putNumber('Rotate Output', self.getRotate())
        wpilib.SmartDashboard.putNumber('Angle', self.getAngle())
        wpilib.SmartDashboard.putNumber('Rotation Rate', self.getRotationRate())

    def saveOutput(self):
        return 'move: {0}\nturn: {1}\nangle: {2}\n'.format(self.getSpeed(), self.getRotate(), self.getAngle())

    def playFromRecording(self, recording):
        '''
        This plays back a certain recording, but only using
        the values that are useful for the drivetrain
        '''
        
        lines = recording.split('\n')

        for l in lines:
            if l.startswith('move'):
                moveValue = float(l.rstrip()[len('move: '):])
            elif l.startswith('turn'):
                turnValue = float(l.rstrip()[len('turn: '):])
            elif l.startswith('angle'):
                # TODO: Implement turning from recording
                print('TODO: Implement turning from recording')

        self.drive(moveValue, turnValue)