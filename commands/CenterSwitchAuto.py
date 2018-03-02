from wpilib.command.command import Command
from commands.CenterToLeft import CenterToLeft
from commands.CenterToRight import CenterToRight
import wpilib
import subsystems

class CenterSwitchAuto(Command):
    '''
    The auto that goes to the switch starting from the center
    '''

    def __init__(self):
        super().__init__('Center Switch Auto')

    def initialize(self):
        print('[AUTO] CenterSwitchAuto running')        

        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        print('[AUTO] Game specific message (msg, repr, type): {0}\n{1}\n{2}'.format(msg, repr(msg), type(msg)))        

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[0] == 'L':
            CenterToLeft().execute()
            
        elif msg[1] == 'R':
            CenterToRight().execute()