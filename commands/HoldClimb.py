from wpilib.command import Command

import OI
import subsystems
import Utils

class HoldClimb(Command):
    '''
    Holds a climb
    '''

    def __init__(self):
        super().__init__('Hold Climb')

        self.requires(subsystems.elevator)

    def execute(self):
        subsystems.elevator.hold()

    def stop(self):
        subsystems.drivetrain.stop()