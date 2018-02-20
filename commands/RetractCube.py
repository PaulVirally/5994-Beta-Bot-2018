from wpilib.command import Command

import subsystems

class RetractCube(Command):
    '''
    Ejects a cube from the claw
    '''

    def __init__(self):
        super().__init__('RetractCube')
        
        self.requires(subsystems.claw)

    def initialize(self):
        pass

    def execute(self):
        subsystems.claw.retract()

    def end(self):
        subsystems.claw.hold()