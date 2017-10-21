from wpilib.command.commandgroup import CommandGroup

from wpilib.command.waitcommand import WaitCommand

class AutonomousProgram(CommandGroup):
    '''
    Waits for 1 second
    '''

    def __init__(self):
        super().__init__('Autonomous Program')
        self.addSequential(WaitCommand(timeout=1))