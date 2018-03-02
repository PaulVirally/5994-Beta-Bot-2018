from wpilib.command import TimedCommand

import subsystems

class RetractCubeForTime(TimedCommand):
    '''
    Ejects a cube from the claw
    '''

    def __init__(self, timeoutInSeconds):
        super().__init__('RetractCube', timeoutInSeconds)
        
        self.requires(subsystems.claw)

    def initialize(self):
        pass

    def execute(self):
        subsystems.claw.retract()

    def end(self):
        subsystems.claw.hold()