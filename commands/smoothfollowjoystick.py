from wpilib.command import Command

import oi
import subsystems
import utils

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
        joyY = oi.joystick.getY()
        joyX = oi.joystick.getX()
        joyZ = oi.joystick.getZ()

        # Put the values through the sigmoid function
        # to smooth them out
        smoothing = 4
        sigY = 2*utils.sigmoid(joyY, a=smoothing)-1
        sigX = 2*utils.sigmoid(joyX, a=smoothing)-1
        sigZ = 2*utils.sigmoid(joyZ, a=smoothing)-1
        s1   = 2*utils.sigmoid(1, a=smoothing)-1
        sn1  = 2*utils.sigmoid(-1, a=smoothing)-1

        # Make sure out speed goes from -1 to 1
        speed = utils.remap(sigY, sn1, s1, -1, 1)

        # Take the largest of either the X or the Z axis
        # and then ensure that it goes from -1 to 1
        turn = (joyX if abs(joyX) > abs(joyZ) else joyZ)
        turn = utils.remap(turn, sn1, s1, -1, 1)

        # Little bit of debugging
        print('({0}, {1}) -> ({2}, {3})'.format(joyX, joyY, turn, speed))

        # Drive
        subsystems.drivetrain.drive(speed, turn)

    def stop(self):
        subsystems.drivetrain.stop()