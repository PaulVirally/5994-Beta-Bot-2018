from wpilib.command import InstantCommand

import oi

class Record(InstantCommand):
    '''
    Starts recording all output from all subsystems and saves
    it all to a specified file
    '''

    def __init__(self, filePath):
        super().__init__('Record')

    def initialize(self):
        oi.shouldRecord = True