from wpilib.command.commandgroup import CommandGroup
import wpilib

import subsystems

class RightSwitchAuto(CommandGroup):
    '''
    The auto that goes to the switch starting from the right
    '''

    def __init__(self):
        super().__init__('Autonomous Program')
        # self.addSequential(WaitCommand(timeout=1))

        msg = wpilib.DriverStation.getGameSpecificMessage()

        if msg[0] == 'L':
            # Go to left switch
            pass
            
        elif msg[1] == 'R':
            # Go to right switch
            pass