from wpilib.command import Command
import subsystems

class SetGyroAngle(Command):
    '''
    Sets the gyro to a specified angle by using a PID control loop.
    '''

    def __init__(self, angle):
        super().__init__('SetGyroAngle')

        self.requires(subsystems.drivetrain)
        self.target = angle
        subsystems.drivetrain.setSetpoint((subsystems.drivetrain.getAngle() + self.target) % 360)        

    def execute(self):
        subsystems.drivetrain.enablePID()

    def stop(self):
        subsystems.drivetrain.disablePID()

    def isFinished(self):
        return subsystems.drivetrain.onTarget()