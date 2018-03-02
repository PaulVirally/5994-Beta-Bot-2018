from wpilib.command.command import Command
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands.RightToRight import RightToRight
import subsystems

class RightSwitchSafe(Command):
    '''
    The auto that goes to the switch starting from the right
    '''

    def __init__(self):
        super().__init__('Right Switch Auto')

    def initialize(self):
        print('[AUTO] RightSwitchSafe running')        
        
        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        print('[AUTO] Game specific message (msg, repr, type): {0}\n{1}\n{2}'.format(msg, repr(msg), type(msg)))        

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[1] == 'R':
            RightToRight().execute()