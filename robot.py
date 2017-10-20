#!/usr/bin/env python3

import wpilib
from wpilib.command import Scheduler
from commandbased import CommandBasedRobot

import subsystems
import OI
from commands.Autonomous import AutonomousProgram


class Robot(CommandBasedRobot):
    '''
    The CommandBasedRobot base class implements almost everything you need for
    a working robot program. All you need to do is set up the subsystems and
    commands. You do not need to override the "periodic" functions, as they
    will automatically call the scheduler. You may override the "init" functions
    if you want to do anything special when the mode changes.
    '''

    def robotInit(self):
        '''
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        '''

        subsystems.init()

        self.autoChooser = wpilib.SendableChooser()
        self.autoChooser.addDefault('autonomous', AutonomousProgram())
        wpilib.SmartDashboard.putData('Auto Mode', self.autoChooser)
        self.autonomousCommand = None

        '''
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        '''
        oi.init()


    def autonomousInit(self):
        '''
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        '''
        self.autonomousCommand = self.autoChooser.getSelected()
        self.autonomousCommand.start()

    def autonomousPeriodic(self):
        '''This function is called periodically during autonomous'''
        Scheduler.getInstance().run()
        self.log()

    def teleopInit(self):
        '''This function is called at the beginning of operator control.'''
        # This ensures that the autonomous stops running when
        # teleop starts running.
        if self.autonomousCommand is not None:
            print('Cancelling the autonomous command...')
            self.autonomousCommand.cancel()

    def teleopPeriodic(self):
        '''This function is called periodically during operator control.'''
        Scheduler.getInstance().run()
        self.log()

    def disabledInit(self):
        '''This function is called once when the robot is disabled.'''
        subsystems.stop()
        self.log()

    def disabledPeriodic(self):
        '''This function is called periodically while disabled.'''
        self.log()

    def log(self):  
        subsystems.log()
        oi.log()      

if __name__ == '__main__':
    wpilib.run(Robot)