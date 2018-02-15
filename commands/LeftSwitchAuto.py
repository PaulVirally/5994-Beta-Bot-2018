from wpilib.command.commandgroup import CommandGroup
import wpilib
from commands.SetDistance import SetDistance
from commands.SetGyroAngle import SetGyroAngle
import subsystems

class LeftSwitchAuto(CommandGroup):
    '''
    The auto that goes to the switch starting from the left
    '''

    def __init__(self):
        super().__init__('Left Switch Auto')

        msg = wpilib.DriverStation.getGameSpecificMessage()

        if msg[0] == 'L':
            # Go to the left switch

            # Go to switch
            self.addSequential(SetDistance(399.4))

            # Turn right
            self.addSequential(SetGyroAngle(90))

            # Drive right up to the switch
            self.addSequential(SetDistance(8.39))

            # Drop off the cube

        elif msg[1] == 'R':
            # Go to right switch

            # Go to bussing lane
            self.addSequential(SetDistance(137.05))

            # Turn right
            self.addSequential(SetGyroAngle(90))

            # Set up for going to switch
            self.addSequential(SetDistance(576.61))

            # Turn left to go to switch
            self.addSequential(SetGyroAngle(-90))

            # Go up to switch
            self.addSequential(SetDistance(262.35))

            # Turn left to face switch
            self.addSequential(SetGyroAngle(-90))

            # Drive right up to the switch
            self.addSequential(SetDistance(8.39))

            # Drop off the cube