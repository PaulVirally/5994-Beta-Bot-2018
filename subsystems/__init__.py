'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''
from wpilib.robotbase import RobotBase

from .Drivetrain import Drivetrain
from .Climber import Climber

drivetrain = None
subsystems = []

recordedData = ''
shouldRecord = False
toPlayBack = ''
lineBreak = '+=-=-=-=-=-=-=-=-=-=-=+'

def init():
    '''
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    '''
    global drivetrain
    global subsystems

    '''
    Some tests call startCompetition multiple times, so don't throw an error if
    called more than once in that case.
    '''

    drivetrain = Drivetrain(1, 0.1, 0) # PID
    climber = Climber()

    subsystems = [drivetrain, climber]

def stop():
    for subsys in subsystems:
        subsys.stop()

def log():
    for subsys in subsystems:
        subsys.log()

def saveOutput():
    if not shouldRecord:
        return

    global recordedData

    for subsys in subsystems:
        recordedData += subsys.saveOutput()
    recordedData += lineBreak

def writeOutput(filePath):
    with open(filePath, 'w+') as outFile:
        outFile.write(recordedData)

def readRecording(filePath):
    global toPlayBack
    try:
        with open(filePath, 'r') as inFile:
            toPlayBack = inFile.read()
    except FileNotFoundError:
        print('[ERROR] subsystems::__init__::readRecording(...) Could not open {0}'.format(filePath))

def playRecording():
    global toPlayBack
    
    idx = toPlayBack.index(lineBreak)
    miniRecording = toPlayBack[:idx]

    for subsys in subsystems:
        subsys.playFromRecording(miniRecording)

    toPlayBack = toPlayBack[idx+1:]