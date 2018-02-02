import wpilib
import ctre
from wpilib.command.subsystem import Subsystem
from wpilib.drive.differentialdrive import DifferentialDrive

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

        self.frontLeftMotor.setInverted(True)
        self.rearLeftMotor.setInverted(True)
        self.frontRightMotor.setInverted(True)
        self.rearRightMotor.setInverted(True)
        
        self.leftMotors = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.rightMotors = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)

        self.drivetrain = DifferentialDrive(self.leftMotors, self.rightMotors)

        self.lastMoveValue = 0
        self.lastRotateValue = 0

        self.gyro = wpilib.ADXRS450_Gyro()
        self.setpoint = 0
        
        self.rangeFinder = wpilib.AnalogInput(0)

    def drive(self, moveValue, rotateValue):
        '''Arcade drive'''
        self.drivetrain.arcadeDrive(moveValue, rotateValue)
        self.lastMoveValue = moveValue
        self.lastRotateValue = rotateValue

    def setSetpoint(self, setpoint):
        self.setpoint = setpoint

    def getError(self):
        return self.getAngle() - self.setpoint

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

    def resetGyro(self):
        self.gyro.reset()

    def getRotationRate(self):
        return self.gyro.getRate()

    def getRangeFinderDistance(self):
        # return self.rangeFinder.getVoltage()
        voltage = self.rangeFinder.getAverageVoltage()
        voltage -= 0.28
        distance = 100 * 1.3168135 * voltage # Refer to https://www.maxbotix.com/documents/XL-MaxSonar-EZ_Datasheet.pdf
        return distance

    def log(self):
        wpilib.SmartDashboard.putNumber('Speed Output', self.getSpeed())
        wpilib.SmartDashboard.putNumber('Rotate Output', self.getRotate())
        wpilib.SmartDashboard.putNumber('Absolute Angle', self.getAngle())
        wpilib.SmartDashboard.putNumber('Angle', self.getAngle() % 360)
        wpilib.SmartDashboard.putNumber('Gyro homemade \'PID\' Error', self.getError())
        wpilib.SmartDashboard.putNumber('Ranger Finder Distance', self.getRangeFinderDistance())

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