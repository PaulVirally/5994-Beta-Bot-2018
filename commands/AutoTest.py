from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands import SetDistance
from commands import SetGyroAngle
import subsystems

class AutoTest(CommandGroup):
    '''
    '''

    def __init__(self):
        super().__init__('Auto Test')

        self.addSequential(SetDistance(500))

        self.addSequential(WaitCommand(timeout=0.05))
        self.addSequential(SetGyroAngle(90))

        self.addSequential(WaitCommand(timeout=0.05))
        self.addSequential(SetGyroAngle(90))

        self.addSequential(WaitCommand(timeout=0.05))
        self.addSequential(SetDistance(500))