from wpilib.command.command import Command
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands.RightToRight import RightToRight
from commands.RightToLeft import RightToLeft
import subsystems

class RightSwitchAuto(Command):
    '''
    The auto that goes to the switch starting from the right
    '''

    def __init__(self):
        super().__init__('Right Switch Auto')

    def initialize(self):
        print('[AUTO] RightSwitchAuto running')
        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        print('Game specific message (msg, repr, type): {0}\n{1}\n{2}'.format(msg, repr(msg), type(msg)))

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[0] == 'L':
            RightToLeft()

        elif msg[1] == 'R':
            RightToRight()