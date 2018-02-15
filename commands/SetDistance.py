from wpilib.command import Command
import wpilib
import subsystems
from math import pi
import time

class SetDistance(Command):
    '''
    Moves the robot a certain distance
    '''

    def __init__(self, target_distance):
        super().__init__('SetDistance')

        self.requires(subsystems.drivetrain)
        self.targetDistance = target_distance
        self.errorCounter = 0
        self.prevAdjust = 0
        self.startTime = 0

    def getError(self):
        return self.targetDistance - subsystems.drivetrain.getRevolutions()*pi*15.24

    def initialize(self):
        subsystems.drivetrain.resetRevolutionCounter()
        self.startTime = time.time()
        
    def execute(self):
        error = self.getError()

        propK = 0.4/50

        adjust = propK * error

        # Magic
        if abs(adjust - self.prevAdjust) < 0.1:
            adjust = self.prevAdjust + (0.11 if adjust > 0 else -0.11)

        if abs(adjust) >= 1:
            adjust = 1 if adjust > 0 else -1

        if abs(self.getError()) <= 5:
            self.errorCounter += 1
        else:
            self.errorCounter = 0

        # Don't take over 1.5 seconds
        # if (time.time() - self.startTime) > 2:
        #     self.shouldEndCount = 101
        #     self.stop()

        subsystems.drivetrain.drive(adjust, 0)

    def stop(self):
        subsystems.drivetrain.stop()

    def isFinished(self):
        if self.errorCounter >= 3:
            self.stop
            return True
        return False