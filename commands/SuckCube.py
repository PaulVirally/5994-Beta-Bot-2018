from wpilib.command import Command

import subsystems

class SuckCube(Command):
    '''
    Sucks a cube into the claw
    '''

    def __init__(self):
        super().__init__('SuckCube')
        
        self.requires(subsystems.claw)

    def initialize(self):
        pass

    def execute(self):
        subsystems.claw.suck()

    def stop(self):
        subsystems.claw.stop()