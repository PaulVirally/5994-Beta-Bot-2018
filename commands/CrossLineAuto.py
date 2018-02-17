from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands.SetDistance import SetDistance
import subsystems

class CrossLineAuto(CommandGroup):
    '''
    '''

    def __init__(self):
        super().__init__('Cross Line Auto')

        self.addSequential(SetDistance(350))