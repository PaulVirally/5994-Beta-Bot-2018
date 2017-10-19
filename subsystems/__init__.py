'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''
from wpilib.robotbase import RobotBase

from .drivetrain import Drivetrain

drivetrain = None

def init():
    '''
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    '''
    global drivetrain

    '''
    Some tests call startCompetition multiple times, so don't throw an error if
    called more than once in that case.
    '''

    if drivetrain is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    drivetrain = Drivetrain()

def stop():
    global drivetrain

    drivetrain.stop()

def log():
    global drivetrain

    drivetrain.log()

def saveOutput(filePath):
    global drivetrain

    out = drivetrain.saveOutput()
    # out += someSubsytem.saveOutput()

    with open(filePath, 'w+') as outFile:
        outFile.write(out)