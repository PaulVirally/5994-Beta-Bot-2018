from wpilib.command import Command

import OI
import subsystems
import Utils

class Climb(Command):
    '''
    Activates the elevator subsystem
    '''

    def __init__(self):
        super().__init__('Climb')

        self.requires(subsystems.elevator)

    def execute(self):
        subsystems.elevator.up()

    def end(self):
        subsystems.elevator.hold() # .hold()?