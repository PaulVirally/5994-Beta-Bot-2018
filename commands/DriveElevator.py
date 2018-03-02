from wpilib.command import Command

import OI
import subsystems
import Utils

class DriveElevator(Command):
    '''
    Drives the elevator according to the joystick
    '''
    
    def __init__(self):
        super().__init__('DriveElevator')

        self.requires(subsystems.elevator)
    
    def execute(self):
        # Get the values from the joystick
        speed = OI.getJoyElevatorSpeed()

        # Put the values through the sigmoid function to smooth it out
        sigSpeed = 2*Utils.sigmoid(speed, a=1)-1

        s1Speed = 2*Utils.sigmoid(1, a=1)-1
        sn1Speed = 2*Utils.sigmoid(-1, a=1)-1

        # Make sure out speed goes from -1 to 1
        speed = Utils.remap(sigSpeed, sn1Speed, s1Speed, -1, 1)

        # Drive
        subsystems.elevator._set(speed)