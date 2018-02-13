import time
import Utils
from wpilib.command import Command
import wpilib
import subsystems

class SetGyroAngle(Command):
    '''
    Sets the gyro to a specified angle by using a "PID" control loop.
    '''

    def __init__(self, target_angle):
        super().__init__('SetGyroAngle')

        self.requires(subsystems.drivetrain)
        self.target_angle = target_angle
        self.shouldEndCount = 0
        wpilib.SmartDashboard.putBoolean('In PID Mode', False)  


    def initialize(self):
        subsystems.drivetrain.resetGyro()
        subsystems.drivetrain.setSetpoint(self.target_angle)
        self.startTime = time.time()
        wpilib.SmartDashboard.putBoolean('In PID Mode', True)  
        

    def execute(self):
        error = subsystems.drivetrain.getError()
        dt = time.time() - self.startTime

        timeK = 1/35
        propK = 1/75

        timeAdjust = dt * timeK
        if timeAdjust > 0.35:
            timeAdjust = 0.35
        if error < 0:
            timeAdjust = -timeAdjust
        propAdjust = error * propK
        if abs(propAdjust) > 0.7:
            propAdjust = 0.7 if propAdjust > 0 else -0.7

        adjust = timeAdjust + propAdjust

        if abs(subsystems.drivetrain.getError()) <= 1:
            self.shouldEndCount += 1
        else:
            self.shouldEndCount = 0

        wpilib.SmartDashboard.putNumber('PID Time Adjust', timeAdjust)
        wpilib.SmartDashboard.putNumber('PID Prop Adjust', propAdjust)
        wpilib.SmartDashboard.putNumber('PID Adjust', adjust)
        wpilib.SmartDashboard.putNumber('PID Should End Count', self.shouldEndCount)
        wpilib.SmartDashboard.putBoolean('In PID Mode', True)

        subsystems.drivetrain.drive(0, adjust)

        
    def stop(self):
        subsystems.drivetrain.stop()
        wpilib.SmartDashboard.putBoolean('In PID Mode', False)

    def isFinished(self):
        if self.shouldEndCount > 5:
            self.stop()
            return True
        return False