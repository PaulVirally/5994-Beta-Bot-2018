import time
import Utils
from wpilib.command import Command
import subsystems

class SetGyroAngle(Command):
    '''
    Sets the gyro to a specified angle by using a "PID" control loop.
    '''

    def __init__(self, target_angle):
        super().__init__('SetGyroAngle')

        self.requires(subsystems.drivetrain)
        self.target_angle = target_angle

    def initialize(self):
        subsystems.drivetrain.resetGyro()
        subsystems.drivetrain.setSetpoint(self.target_angle)
        self.startTime = time.time()

    def execute(self):
        error = subsystems.drivetrain.getError()
        dt = time.time() - self.startTime
        maxError = 360

        timeK = 0.01
        propK = 1

        timeAdjust = dt * error * timeK
        propAdjust = error * propK
        adjust = timeAdjust + propAdjust

        maxTimeAdj = dt * maxError * timeK
        maxPropAdjust = maxError * propK
        maxAdjust = maxTimeAdj + maxPropAdjust

        turn = Utils.remap(adjust, 0, maxAdjust, 0, 1)
        if error > 0:
            turn *= -1

        subsystems.drivetrain.drive(0, turn)

    def stop(self):
        subsystems.drivetrain.stop()

    def isFinished(self):
        return abs(subsystems.drivetrain.getError()) <= 1