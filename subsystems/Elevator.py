import wpilib
from wpilib.command.subsystem import Subsystem
import RobotMap

class Elevator(Subsystem):
    '''
    This is the elevator subsystem. This is the thing responsible for climbing the rope.
    '''

    def __init__(self):
        '''Instantiates the Elevator object.'''

        super().__init__('Elevator')
        self.limitSwitch = wpilib.DigitalInput(RobotMap.elevator.limitSwitch)
        self.motor = wpilib.VictorSP(RobotMap.elevator.motor)
        self.lastMotorValue = 0

    def _set(self, pwm):
        self.motor.set(pwm)
        self.lastMotorValue = pwm

    def hold(self):
        self._set(0.2)

    def up(self):
        self._set(0.5)

    def down(self):
        self._set(0.05)

    def stop(self):
        self.motor.set(0)
        self.lastMotorValue = 0        

    def log(self):
        wpilib.SmartDashboard.putBoolean('Limit Switch State', self.limitSwitch.get())
        wpilib.SmartDashboard.putBoolean('Elevator PWM', self.lastMotorValue)

    def saveOutput(self):
        return ''

    def playFromRecording(self, recording):
        '''
        This plays back a certain recording, but only using
        the values that are useful for the elevator
        '''
        pass