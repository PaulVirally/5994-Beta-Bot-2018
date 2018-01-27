from wpilib.command import Command

import OI
import subsystems
import Utils

class SetGyroAngle(Command):
    '''
    Sets the gyro to a specified angle by using a PID control loop.
    '''

    def __init__(self, angle):
        super().__init__('SetGyroAngle')

        self.requires(subsystems.drivetrain)
        self.target = angle

    def execute(self):
        subsystems.drivetrain.enablePID()
        subsystems.drivetrain.setSetpoint(self.target)

    def stop(self):
        subsystems.drivetrain.disablePID()

    def isFinished(self):
        return subsystems.drivetrain.onTarget()