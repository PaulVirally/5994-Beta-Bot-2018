import wpilib
import ctre
from wpilib.command.subsystem import Subsystem
from wpilib.drive.differentialdrive import DifferentialDrive

from commands.SmoothFollowJoystick import SmoothFollowJoystick
import RobotMap
import subsystems

class Drivetrain(wpilib.command.PIDSubsystem):
    '''
    This is the drivetrain subsystem
    '''

    def __init__(self, p, i, d):
        '''Instantiates the drivetrain object.'''

        # Pid stuff
        super().__init__(p, i, d, name='Drivetrain')
        self.setAbsoluteTolerance(0.05)
        self.setInputRange(0, 360)
        self.setOutputRange(-1, 1)

        self.frontLeftMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.frontLeftMotor)
        self.frontRightMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.frontRightMotor)
        self.rearLeftMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.rearLeftMotor)
        self.rearRightMotor =  ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.drivetrain.rearRightMotor)

        self.frontLeftMotor.setInverted(True)
        self.rearLeftMotor.setInverted(False)
        self.frontRightMotor.setInverted(True)
        self.rearRightMotor.setInverted(False)
        
        self.leftMotors = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.rightMotors = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearLeftMotor)

        self.drivetrain = DifferentialDrive(self.leftMotors, self.rightMotors)

        self.lastMoveValue = 0
        self.lastRotateValue = 0

        self.gyro = wpilib.ADXRS450_Gyro()

    def returnPIDInput(self):
        return self.getAngle()

    def usePIDOutput(self, output):
        self.drivetrain.arcadeDrive(0, output)
        self.lastMoveValue = 0
        self.lastRotateValue = output

    def enablePID(self):
        self.enable()

    def disablePID(self):
        self.disable()

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
        return self.gyro.getAngle() % 360

    def getRotationRate(self):
        return self.gyro.getRate()

    def log(self):
        wpilib.SmartDashboard.putNumber('Speed Output', self.getSpeed())
        wpilib.SmartDashboard.putNumber('Rotate Output', self.getRotate())
        wpilib.SmartDashboard.putNumber('Angle', self.getAngle())
        wpilib.SmartDashboard.putNumber('Rotation Rate', self.getRotationRate())
        wpilib.SmartDashboard.putNumber('Gyro PID Position', self.getPosition())

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