from wpilib.command.command import Command
from wpilib.command.waitcommand import WaitCommand
from commands.LeftToLeft import LeftToLeft
import wpilib
import subsystems

class LeftSwitchSafe(Command):
    '''
    The auto that goes to the switch starting from the left
    '''

    def __init__(self):
        super().__init__('Left Switch Safe Auto')

    def initialize(self):
        print('[AUTO] LeftSwitchSafe running')        

        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        print('[AUTO] Game specific message (msg, repr, type): {0}\n{1}\n{2}'.format(msg, repr(msg), type(msg)))        

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[0] == 'L':
            LeftToLeft().execute()