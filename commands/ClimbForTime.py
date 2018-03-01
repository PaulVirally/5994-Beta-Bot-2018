from wpilib.command import TimedCommand

import OI
import subsystems
import Utils

class ClimbForTime(TimedCommand):
    '''
    Activates the elevator subsystem (timed)
    '''

    def __init__(self, timeoutInSeconds):
        super().__init__('ClimbForTime', timeoutInSeconds)

        self.requires(subsystems.elevator)

    def execute(self):
        subsystems.elevator.up()

    def end(self):
        subsystems.elevator.hold() # .hold()?