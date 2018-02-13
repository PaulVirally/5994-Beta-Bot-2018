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

        # Adjustment should increase over time
        timeAdjust = dt * timeK

        # If timeAdjust is too high, we don't want to robot to get out
        # of control, so force it be at a lower value
        if timeAdjust > 0.35:
            timeAdjust = 0.35

        # If the error is negative, we need to make the time adjust
        # negative too
        if error < 0:
            timeAdjust = -timeAdjust
        
        # Adjustment proportional to the error
        propAdjust = error * propK

        # If the propAdjust is too high, we don't want the robot to
        # get out of control, so force it to be at a lower value
        if abs(propAdjust) > 0.7:
            propAdjust = 0.7 if propAdjust > 0 else -0.7

        # The total adjustment is the sum of timeAdjust and propAdjust
        # This is why we needed timeAdjust to be of the same sign as
        # propAdjust (to not have them add up to a value close to 0)
        adjust = timeAdjust + propAdjust

        # If the adjust is too low, force it to be some minimum
        # value. This ensures that the robot is always moving
        # at least a little bit. We don't want to sit and wait
        # for the timeAdjust to accumulate when we could just
        # force the total adjust to be som minimum value. This
        # minimum value should be lowest value that makes the robot
        # move. It should not make the robot move noticeably.
        if abs(adjust < 0.22):
            adjust = 0.22 if adjust > 0 else adjust = -0.22

        # If we are within our range of error, increment shouldEndCount.
        # This makes sure that we don't just hit our setpoint once while
        # carrying some huge momentum. This forces the robot to slow down
        # to the setpoint. This shouldEndCount will accumulate and the
        # command will only end when this value has hit a certain threshold.
        if abs(subsystems.drivetrain.getError()) <= 1:
            self.shouldEndCount += 1
        else:
            self.shouldEndCount = 0

        # Logging
        wpilib.SmartDashboard.putNumber('PID Time Adjust', timeAdjust)
        wpilib.SmartDashboard.putNumber('PID Prop Adjust', propAdjust)
        wpilib.SmartDashboard.putNumber('PID Adjust', adjust)
        wpilib.SmartDashboard.putNumber('PID Should End Count', self.shouldEndCount)
        wpilib.SmartDashboard.putBoolean('In PID Mode', True)

        # Actually drive with the computed adjust
        subsystems.drivetrain.drive(0, adjust)

    def stop(self):
        subsystems.drivetrain.stop()
        wpilib.SmartDashboard.putBoolean('In PID Mode', False)

    def isFinished(self):
        if self.shouldEndCount > 5:
            self.stop()
            return True
        return False