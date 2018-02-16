from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands import SetDistance
from commands import SetGyroAngle
import subsystems

class RightSwitchAuto(CommandGroup):
    '''
    The auto that goes to the switch starting from the right
    '''

    def __init__(self):
        super().__init__('Right Switch Auto')
        
        msg = wpilib.DriverStation.getGameSpecificMessage()

        if msg[0] == 'L':
            # Go to the left switch

            # Go to bussing lane
            self.addSequential(SetDistance(137.05))

            # Go turn left
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetGyroAngle(-90))

            # Set up for going to switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetDistance(576.61))

            # Turn right to go to switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetGyroAngle(-90))

            # Go up to switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetDistance(262.35))

            # Turn right to face switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetGyroAngle(90))

            # Drive right up to the switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetDistance(8.39))

            # Drop off the cube

        elif msg[1] == 'R':
            # Go to right switch

            # Go to switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetDistance(399.4))

            # Turn left
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetGyroAngle(-90))

            # Drive right up to the switch
            self.addSequential(WaitCommand(timeout=0.05))            
            self.addSequential(SetDistance(8.39))

            # Drop off the cube