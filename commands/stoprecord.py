from wpilib.command import InstantCommand

import oi

class Record(InstantCommand):
    '''
    Stops recording all output from all subsystems and saves
    it all to a specified file
    '''

    def __init__(self, filePath):
        super().__init__('Stop Record')
        self.filePath = filePath

    def initialize(self):
        oi.shouldRecord = False
        subsystems.writeOutput(self.filePath)