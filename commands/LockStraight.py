from wpilib.command import Command

import OI
import subsystems
import Utils

class LockStraight(Command):
    '''
    Drives the robot straight with a speed according
    to what the joystick says.
    '''

    def __init__(self):
        super().__init__('Lock Straight')

        self.requires(subsystems.drivetrain)

    def execute(self):
        # Get the values from the joystick
        joySpeed = oi.getJoySpeed()

        # Put the values through the sigmoid function
        # to smooth them out
        smoothing = 4 # TODO: Put this on the smart dashboard?
        sigJoySpeed = 2*utils.sigmoid(joySpeed, a=smoothing)-1
        s1   = 2*utils.sigmoid(1, a=smoothing)-1
        sn1  = 2*utils.sigmoid(-1, a=smoothing)-1

        # Make sure out speed goes from -1 to 1
        speed = utils.remap(sigJoySpeed, sn1, s1, -1, 1)

        # Drive
        subsystems.drivetrain.drive(speed, 0)

    def stop(self):
        subsystems.drivetrain.stop()