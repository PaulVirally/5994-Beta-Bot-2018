* Make the joystick input smoothing an input that can be changed via the SmartDashboard
* Add a notification if something is being recorded on the SmartDashboard
* Add the following commands:
    * preciseDrive
* Make reverseDrive, preciseDrive, etc. toggles on the SmartDashboard as opposed to buttons you have to hold (so that it could be like a button you press once to toggle on and then turn it off but pressing that button again)
* Make the .log() functions actually write to a file so that you have a written reference of something that might have gone wrong. For example, if the robot crashes into a wall, you might want to know why that happened and you might think that the only way to do so is to repeat the incident many times until you figure out the problem. However, if you had a written log file then you could just refer to that to see what subsystem went crazy.
* Docstrings everywhere
* Tests everywhere
* Linting?
* Convert all non-wpi variables to use snake_case naming convention