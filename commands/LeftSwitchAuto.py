from wpilib.command.command import Command
from wpilib.command.waitcommand import WaitCommand
from commands.LeftToLeft import LeftToLeft
from commands.LeftToRight import LeftToRight
import wpilib
import subsystems

class LeftSwitchAuto(Command):
    '''
    The auto that goes to the switch starting from the left
    '''

    def __init__(self):
        super().__init__('Left Switch Auto')

    def initialize(self):
        print('[AUTO] LeftSwitchAuto running')

        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        print('[AUTO] Game specific message (msg, repr, type): {0}\n{1}\n{2}'.format(msg, repr(msg), type(msg)))

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[0] == 'L':
            LeftToLeft().execute()

        elif msg[1] == 'R':
            LeftToRight().execute()