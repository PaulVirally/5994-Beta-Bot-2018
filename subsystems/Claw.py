import wpilib
import ctre
from wpilib.command.subsystem import Subsystem
from commands.HoldClaw import HoldClaw
import RobotMap

class Claw(Subsystem):
    '''
    This is the claw subsystem. This is the thing responsible for clawing things.
    '''

    def __init__(self):
        '''Instantiates the claw object'''
        
        super().__init__('Claw')

        self.lastValue = 0
        self.motorL = wpilib.VictorSP(RobotMap.claw.leftMotor)
        self.motorR = wpilib.VictorSP(RobotMap.claw.rightMotor)
        self.winchMotor = ctre.wpi_talonsrx.WPI_TalonSRX(RobotMap.claw.winchMotor)

    def initDefaultCommand(self):
        self.setDefaultCommand(HoldClaw())

    def _set(self, value):
        self.lastValue = value
        self.motorL.set(value)
        self.motorR.set(-value)

    def stop(self):
        self._set(0)
        self.winchMotor.set(0)

    def hold(self):
        self._set(0)

    def suck(self):
        self._set(1)
    
    def retract(self):
        self._set(-1)

    def winchUp(self):
        self.winchMotor.set(1)

    def winchDown(self):
        self.winchMotor.set(-1)

    def log(self):
        wpilib.SmartDashboard.putNumber('Claw', self.motorL.get())
        wpilib.SmartDashboard.putNumber('Winch', self.winchMotor.get())

    def update(self):
        pass

    def saveOutput(self):
        return ''

    def playFromRecording(self, recording):
        '''
        This plays back a certain recording, but only using
        the values that are useful for the elevator
        '''
        pass