from wpilib.command import Command

import subsystems

class WinchDown(Command):
    '''
    Brings the winch down
    '''

    def __init__(self):
        super().__init__('WinchDown')
        
        self.requires(subsystems.claw)

    def initialize(self):
        pass

    def execute(self):
        subsystems.claw.winchDown()

    def end(self):
        subsystems.claw.stop()