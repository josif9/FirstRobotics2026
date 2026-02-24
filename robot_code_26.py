# TODO: insert robot code here
import rev
import wpilib
from cscore import CameraServer
from wpilib.drive import DifferentialDrive

CameraServer.startAutomaticCapture(0)

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        
        # Motor controller setup
        self.leftFront = rev.SparkMax(1, rev.SparkLowLevel.MotorType.kBrushed)
        self.rightFront = rev.SparkMax(2, rev.SparkLowLevel.MotorType.kBrushed)
        self.leftRear = rev.SparkMax(3, rev.SparkLowLevel.MotorType.kBrushed)
        self.rightRear = rev.SparkMax(4, rev.SparkLowLevel.MotorType.kBrushed)
        self.dualMotor = rev.SparkMax(6, rev.SparkLowLevel.MotorType.kBrushed)
        self.singleMotor = rev.SparkMax(5, rev.SparkLowLevel.MotorType.kBrushed)
        
        # Creating motor groups to differentiate the left and right side motors
        self.leftMotorGroup = wpilib.MotorControllerGroup(self.leftFront, self.leftRear)
        self.rightMotorGroup = wpilib.MotorControllerGroup(self.rightFront, self.rightRear)
                                                          
        # Tank drive setup
        self.drive = DifferentialDrive(self.leftMotorGroup, self.rightMotorGroup)
        
        # Controller setup 
        self.controller = wpilib.XboxController(0)
        
    def teleopPeriodic(self):
        
        # Gets the values from the different controller inputs
        left_y = self.controller.getLeftY()
        right_y = -self.controller.getRightY()
        rightTrigger = self.controller.getRightTriggerAxis()
        leftTrigger = self.controller.getLeftTriggerAxis()
        
        # This segment contains the staements that tell the robot how fast and in what direction to drive
        if abs(left_y) < 0.1:
            left_speed = 0
        else:
            left_speed = left_y
        
        if abs(right_y) < 0.1:
            right_speed = 0
        else:
            right_speed = right_y
            
        self.drive.tankDrive(left_speed, right_speed)
        
        # Segment for the functions of the triggers
        if (rightTrigger > 0.2):
            self.singleMotor.set(-1)
            self.dualMotor.set(-1)
        elif(leftTrigger > 0.2):
            self.singleMotor.set(1)
            self.dualMotor.set(-0.5)
        else:
            self.singleMotor.set(0)
            self.dualMotor.set(0)
            
if __name__ == "__main__":
    wpilib.run(MyRobot)
        
        
            
