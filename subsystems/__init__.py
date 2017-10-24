'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''
from wpilib.robotbase import RobotBase

from .Drivetrain import Drivetrain
from .Climber import Climber

drivetrain = None
climber = None

recordedData = ''
shouldRecord = False

def init():
    '''
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    '''
    global drivetrain
    global climber

    '''
    Some tests call startCompetition multiple times, so don't throw an error if
    called more than once in that case.
    '''

    if drivetrain is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    if climber is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    drivetrain = Drivetrain()
    climber = Climber()

def stop():
    global drivetrain
    global climber

    drivetrain.stop()
    climber.stop()

def log():
    global drivetrain
    global climber

    drivetrain.log()
    climber.log()

def saveOutput():
    if not shouldRecord:
        return

    global drivetrain
    global climber

    recordedData += drivetrain.saveOutput()
    recordedData += climber.saveOutput()

def writeOutput(filePath):
    with open(filePath, 'w+') as outFile:
        outFile.write(out)