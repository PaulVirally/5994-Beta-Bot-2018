from wpilib.command import Command
import OI
import subsystems

class Brake(Command):
    '''
    Brakes
    '''

    def __init__(self):
        super().__init__('Brake')

        self.requires(subsystems.drivetrain)
        self.requires(subsystems.claw)
        self.requires(subsystems.elevator)

    def execute(self):
        subsystems.drivetrain.stop()
        subsystems.claw.stop()
        subsystems.elevator.stop()
        OI.rumble()

    def end(self):
        subsystems.drivetrain.stop()
        subsystems.claw.stop()
        subsystems.elevator.stop()
        OI.stopRumble()        