from wpilib.command import Command

import OI
import subsystems
import Utils

class SmoothFollowJoystick(Command):
    '''
    Drives the robot along what the joystick says, but smooth out
    the input from the joystick
    '''

    def __init__(self):
        super().__init__('Smooth Follow Joystick')

        self.requires(subsystems.drivetrain)

    def execute(self):
        # Get the values from the joystick
        joySpeed = OI.getJoySpeed()
        joyTurn = OI.getJoyTurn()

        # Put the values through the sigmoid function
        # to smooth them out
        smoothing = 4 # TODO: Put this on the smart dashboard??
        sigJoySpeed = 2*utils.sigmoid(joySpeed, a=smoothing)-1
        sigJoyTurn = 2*utils.sigmoid(joyTurn, a=smoothing)-1
        s1   = 2*utils.sigmoid(1, a=smoothing)-1
        sn1  = 2*utils.sigmoid(-1, a=smoothing)-1

        # Make sure out speed goes from -1 to 1
        speed = utils.remap(sigJoySpeed, sn1, s1, -1, 1)
        turn = utils.remap(sigJoyTurn, sn1, s1, -1, 1)

        # Little bit of debugging
        print('({0}, {1}) -> ({2}, {3})'.format(joySpeed, joyTurn, speed, turn))

        # Drive
        subsystems.drivetrain.drive(speed, turn)

    def stop(self):
        subsystems.drivetrain.stop()