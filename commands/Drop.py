from wpilib.command import Command

import OI
import subsystems
import Utils

class Drop(Command):
    '''
    Drop command
    '''

    def __init__(self):
        super().__init__('Drop')

        self.requires(subsystems.elevator)

    def execute(self):
        subsystems.elevator.down()

    def end(self):
        subsystems.elevator.hold()