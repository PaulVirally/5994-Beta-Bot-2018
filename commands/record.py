from wpilib.command import InstantCommand

import subsystems

class Record(InstantCommand):
    '''
    Starts recording all output from all subsystems and saves
    it all to a specified file
    '''

    def __init__(self):
        super().__init__('Record')

    def initialize(self):
        subsystems.shouldRecord = True