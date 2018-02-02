import wpilib
from wpilib.command.subsystem import Subsystem

import RobotMap

class Elevator(Subsystem):
    '''
    This is the elevator subsystem. This is the thing responsible for climbing the rope.
    '''

    def __init__(self):
        '''Instantiates the Elevator object.'''

        super().__init__('Elevator')
        self.limitSwtich = wpilib.DigitalInput(0)

    def stop(self):
        pass

    def getOutput(self):
        pass

    def log(self):
        wpilib.SmartDashboard.putBoolean('Limit Switch State', self.limitSwtich.get())

    def saveOutput(self):
        pass

    def playFromRecording(self, recording):
        '''
        This plays back a certain recording, but only using
        the values that are useful for the elevator
        '''
        pass