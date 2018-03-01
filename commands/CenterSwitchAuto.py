from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import wpilib
from commands.SetDistance import SetDistance
from commands.SetGyroAngle import SetGyroAngle
from commands.ClimbForTime import ClimbForTime
from commands.SuckForTime import SuckForTime
from commands.RetractForTime import RetractCubeForTime
import subsystems

class CenterSwitchAuto(CommandGroup):
    '''
    The auto that goes to the switch starting from the center
    '''

    def __init__(self):
        super().__init__('Center Switch Auto')
        print('[WARNING] CenterSwitchAuto running')        

        msg = wpilib.DriverStation.getInstance().getGameSpecificMessage()

        if not msg:
            print('[WARNING] No game specific message found!')
            return

        if msg[0] == 'L':
            # Go to left switch

            # Go to bussing lane
            self.addSequential(SetDistance(137.05))
            self.addParallel(ClimbForTime(3))
            self.addParallel(SuckForTime(12))         

            # Turn left
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(-90))            

            # Set up for going to switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(309.34))            

            # Turn right
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(90))

            # Drive up to switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(262.35))            

            # Face the switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(90))            

            # Drive right up to the switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(8.39))

            # Drop off cube
            self.addSequential(RetractCubeForTime(3))            
            
        elif msg[1] == 'R':
            # Go to right switch

            # Go to bussing lane
            self.addSequential(SetDistance(137.05))
            self.addParallel(ClimbForTime(3))
            self.addParallel(SuckForTime(12))          

            # Turn right
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(90))            

            # Set up for going to switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(266.27))

            # Turn left
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(-90))            

            # Drive up to switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(262.35))

            # Face the switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetGyroAngle(-90))            

            # Drive right up to the switch
            self.addSequential(WaitCommand(timeout=0.1))            
            self.addSequential(SetDistance(8.39))

            # Drop off cube
            self.addSequential(RetractCubeForTime(3))            