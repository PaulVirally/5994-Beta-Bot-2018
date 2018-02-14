from wpilib.command import Command
import wpilib
import subsystems

class SetDistance(Command):
    '''
    Moves the robot a certain distance
    '''

    def __init__(self, target_distance):
        super().__init__('SetDistance')

        self.requires(subsystems.drivetrain)
        self.targetDistance = target_distance

    def initialize(self):
        pass
        
    def execute(self):
        pass

    def stop(self):
        subsystems.drivetrain.stop()

    def isFinished(self):
        self.stop()
        return True