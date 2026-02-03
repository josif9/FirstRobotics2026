import wpilib
from rev import SparkMax, SparkLowLevel

'''
leftFrontMotor = 0
rightFrontMotor = 1
leftRearMotor = 2
rightRearMotor = 3
intakeMotor = 4
shooterMotor = 5
'''

class MyRobot(wpilib.TimedRobot):
    
    global leftFrontMotor,rightFrontMotor,leftRearMotor,rightRearMotor,intakeMotor,shooterMotor
    
    def robotInit(self):
        
        # Motor controller setup
        self.leftFront = wpilib.SparkMax(0, wpilib.SparkLowLevel.MotorType.kBrushed)
        self.rightFront = wpilib.SparkMax(1, wpilib.SparkLowLevel.MotorType.kBrushed)
        self.leftRear = wpilib.SparkMax(2, wpilib.SparkLowLevel.MotorType.kBrushed)
        self.rightRear = wpilib.SparkMax(3, wpilib.SparkLowLevel.MotorType.kBrushed)
        self.intake = wpilib.SparkMax(4, wpilib.SparkLowLevel.MotorType.kBrushed)
        self.shooter = wpilib.SparkMax(5, wpilib.SparkLowLevel.MotorType.kBrushed)
        
        # Tank drive setup
        self.drive = wpilib.TankDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        
        # Controller setup 
        self.controller = wpilib.XboxController(0)
        
    def teleopPeriodic(self):
        
        left_y = -self.controller.getLeftY()
        right_y = -self.controller.getRightY()
        rightTrigger = self.controller.getRightTriggerAxis()
        
        
        if left_y and right_y < 0.1:
            left_speed = 0
            right_speed = 0
        else:
            left_speed = left_y
            right_speed = right_y

        self.drive.tankDrive(left_speed, right_speed)
        
        if (rightTrigger > 0.2):
            self.shooter.set(0.5)
        else:
            self.shooter.set(0)
            
        if (self.intake > 0.2):
            self.intake.set(0.5)
        else:
            self.intake.set(0)
            
if __name__ == "__main__":
    wpilib.run(MyRobot)
        
        
            
        
        