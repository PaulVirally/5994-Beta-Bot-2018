from wpilib.command import Command

import OI
import subsystems
import Utils

class DriveClaw(Command):
    '''
    Drives the claw according to the joystick
    '''
    
    def __init__(self):
        super().__init__('DriveClaw')

        self.requires(subsystems.claw)
    
    def execute(self):
        # Get the values from the joystick
        l, r = OI.getClawSpeeds()
        
        # Put the values through the sigmoid function to smooth it out
        lSpeed = 2*Utils.sigmoid(l, a=1)-1
        rSpeed = 2*Utils.sigmoid(r, a=1)-1

        s1Speed = 2*Utils.sigmoid(1, a=1)-1
        sn1Speed = 2*Utils.sigmoid(-1, a=1)-1

        # Make sure out speed goes from -1 to 1
        lSpeed = Utils.remap(lSpeed, sn1Speed, s1Speed, -1, 1)
        rSpeed = -Utils.remap(rSpeed, sn1Speed, s1Speed, -1, 1)

        # Drive
        subsystems.claw.motorL.set(lSpeed)
        subsystems.claw.motorR.set(rSpeed)