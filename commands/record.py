from wpilib.command import Command

import oi

class Record(Command):
    '''
    Starts recording all output from all subsystems and saves
    it all to a specified file
    '''

    def __init__(self, filePath):
        super().__init__('Record')
        oi.shouldRecord = True

    def execute(self):
        pass

    def stop(self):
        pass