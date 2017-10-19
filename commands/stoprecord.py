from wpilib.command import Command

import oi

class Record(Command):
    '''
    Stops recording all output from all subsystems and saves
    it all to a specified file
    '''

    def __init__(self, filePath):
        super().__init__('Record')
        oi.shouldRecord = False

    def execute(self):
        pass

    def stop(self):
        pass