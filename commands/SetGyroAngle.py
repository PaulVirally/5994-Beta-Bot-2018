from wpilib.command import Command
import subsystems

class SetGyroAngle(Command):
    '''
    Sets the gyro to a specified angle by using a PID control loop.
    '''

    def __init__(self, target_angle):
        super().__init__('SetGyroAngle')

        self.requires(subsystems.drivetrain)
        self.target_angle = target_angle
        # a = subsystems.drivetrain.getAngle()
        # a360 =  a % 360
        # subsystems.drivetrain.setInputRange(a - a360, a + a360)
        # subsystems.drivetrain.setSetpoint(a + target_angle)

    def initialize(self):
        print('SetGyroAngle Initialized')
        subsystems.drivetrain.resetGyro()
        subsystems.drivetrain.setSetpoint(self.target_angle)

    def execute(self):
        subsystems.drivetrain.enablePID()

    def stop(self):
        subsystems.drivetrain.disablePID()

    def isFinished(self):
        if subsystems.drivetrain.onTarget():
            print('Found target angle')
            return True
        return False