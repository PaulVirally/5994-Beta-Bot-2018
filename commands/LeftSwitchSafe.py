from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands.SetDistance import SetDistance
from commands.SetGyroAngle import SetGyroAngle
from commands.ClimbForTime import ClimbForTime
from commands.SuckForTime import SuckForTime
from commands.RetractForTime import RetractCubeForTime
import subsystems

class LeftSwitchSafe(CommandGroup):
    '''
    The auto that goes to the switch starting from the left
    '''

    def __init__(self):
        super().__init__('Left Switch Auto')

    def initialize(self):
        print('[AUTO] LeftSwitchSafe running')        

        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        print('[AUTO] Game specific message (msg, repr, type): {0}\n{1}\n{2}'.format(msg, repr(msg), type(msg)))        

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[0] == 'L':
            # Go to the left switch

            # Go to switch
            self.addSequential(SetDistance(399.4))
            self.addParallel(ClimbForTime(3))
            self.addParallel(SuckForTime(12))

            # Turn right
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(90))

            # Drive right up to the switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(8.39))

            # Drop off the cube
            self.addSequential(RetractCubeForTime(3))

        elif msg[1] == 'R':
            pass