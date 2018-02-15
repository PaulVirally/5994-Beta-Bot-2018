from wpilib.command import Command
import wpilib
import subsystems
from math import pi

class SetDistance(Command):
    '''
    Moves the robot a certain distance
    '''

    def __init__(self, target_distance):
        super().__init__('SetDistance')

        self.requires(subsystems.drivetrain)
        self.targetDistance = target_distance
        self.errorCounter = 0

    def getError(self):
        return self.targetDistance - subsystems.drivetrain.getRevolutions()*pi*15.24

    def initialize(self):
        subsystems.drivetrain.resetRevolutionCounter()
        
    def execute(self):
        error = self.getError()

        propK = 0.4/50

        adjust = propK * error

        if abs(adjust) >= 1:
            adjust = 1 if adjust > 0 else -1

        subsystems.drivetrain.drive(adjust, 0)

    def stop(self):
        subsystems.drivetrain.stop()

    def isFinished(self):
        if self.errorCounter >= 3:
            self.stop
            return True
        return False