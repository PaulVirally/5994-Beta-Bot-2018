from wpilib.command import InstantCommand

import subsystems

class Record(InstantCommand):
    '''
    Starts/stop recording all output from all subsystems and saves
    it all to a specified file
    '''

    def __init__(self, filePath):
        super().__init__('Record')
        self.filePath = filePath

    def initialize(self):
        global subsystems

        # If it was in recording mode, stop recording and save the output
        if subsystems.shouldRecord:
            subsystems.shouldRecord = False
            subsystems.writeOutput(self.filePath)

        # If it was not in recording mode, set it to recording mode
        else:
            subsystems.shouldRecord = True