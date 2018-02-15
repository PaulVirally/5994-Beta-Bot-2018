from wpilib.command.commandgroup import CommandGroup
import wpilib
from commands.SetDistance import SetDistance
from commands.SetGyroAngle import SetGyroAngle
import subsystems

class CenterSwitchAuto(CommandGroup):
    '''
    The auto that goes to the switch starting from the center
    '''

    def __init__(self):
        super().__init__('Center Switch Auto')

        msg = wpilib.DriverStation.getGameSpecificMessage()

        if msg[0] == 'L':
            # Go to left switch

            # Go to bussing lane
            self.addSequential(SetDistance(137.05))            

            # Turn left
            self.addSequential(SetGyroAngle(-90))            

            # Set up for going to switch
            self.addSequential(SetDistance(309.34))            

            # Turn right
            self.addSequential(SetGyroAngle(90))

            # Drive up to switch
            self.addSequential(SetDistance(262.35))            

            # Face the switch
            self.addSequential(SetGyroAngle(90))            

            # Drive right up to the switch
            self.addSequential(SetDistance(8.39))

            # Drop off cube
            
        elif msg[1] == 'R':
            # Go to right switch

            # Go to bussing lane
            self.addSequential(SetDistance(137.05))            

            # Turn right
            self.addSequential(SetGyroAngle(90))            

            # Set up for going to switch
            self.addSequential(SetDistance(266.27))

            # Turn left
            self.addSequential(SetGyroAngle(-90))            

            # Drive up to switch
            self.addSequential(SetDistance(262.35))

            # Face the switch
            self.addSequential(SetGyroAngle(-90))            

            # Drive right up to the switch
            self.addSequential(SetDistance(8.39))

            # Drop off cube