from wpilib.command import Command

import OI
import subsystems
import Utils

class HoldClaw(Command):
    '''
    Hold Claw command
    '''

    def __init__(self):
        super().__init__('HoldClaw')

        self.requires(subsystems.claw)

    def execute(self):
        subsystems.claw.hold()

    def end(self):
        subsystems.claw.stop()