from cscore import CameraServer

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    frontCam = cs.startAutomaticCapture(dev=0)
    backCam = cs.startAutomaticCapture(dev=1)

    frontCam.setResolution(320, 240)
    backCam.setResolution(320, 240)    

    cs.waitForever()