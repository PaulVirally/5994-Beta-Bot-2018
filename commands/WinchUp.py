from wpilib.command import Command

import subsystems

class WinchUp(Command):
    '''
    Brings the winch up
    '''

    def __init__(self):
        super().__init__('WinchUp')
        
        self.requires(subsystems.claw)

    def initialize(self):
        pass

    def execute(self):
        subsystems.claw.winchUp()

    def end(self):
        subsystems.claw.stop()