from wpilib.command import InstantCommand

import OI
import subsystems
import Utils

class StopClimb(InstantCommand):
    '''
    Stops climbing
    '''

    def __init__(self):
        super().__init__('Stop Climb')
        
        self.requires(subsystems.elevator)

    def initialize(self):
        subsystems.elevator.stop()