from wpilib.command import TimedCommand

import subsystems

class SuckForTime(TimedCommand):
    '''
    Sucks a cube into the claw
    '''

    def __init__(self, timeoutInSeconds):
        super().__init__('SuckForTime', timeoutInSeconds)
        
        self.requires(subsystems.claw)

    def initialize(self):
        pass

    def execute(self):
        subsystems.claw.suck()

    def end(self):
        subsystems.claw.stop()