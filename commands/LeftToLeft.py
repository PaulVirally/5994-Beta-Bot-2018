from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands.SetDistance import SetDistance
from commands.SetGyroAngle import SetGyroAngle
from commands.ClimbForTime import ClimbForTime
from commands.SuckForTime import SuckForTime
from commands.RetractForTime import RetractCubeForTime
import subsystems

class LeftToLeft(CommandGroup):

    def __init__(self):
        super().__init__('LeftToLeft')
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