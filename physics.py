from pyfrc.physics import drivetrains

class PhysicsEngine:
    '''
    Simulates a 4-wheel robot
    '''

    def __init__(self, physics_controller):
        self.physics_controller = physics_controller

    def update_sim(self, hal_data, now, dt):
        lr_motor = hal_data['pwm'][2]['value']
        rr_motor = hal_data['pwm'][3]['value']
        lf_motor = hal_data['pwm'][0]['value']
        rf_motor = hal_data['pwm'][1]['value']

        speed, rotation = drivetrains.four_motor_drivetrain(lr_motor, rr_motor, lf_motor, rf_motor)
        self.physics_controller.drive(speed, rotation, dt)