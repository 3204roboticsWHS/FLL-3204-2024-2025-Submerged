from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


kd = DriveBase(Motor(Port.A, Direction.COUNTERCLOCKWISE), Motor(Port.E), 56, 84)


kd.use_gyro(True)
kd.straight(600)
kd.settings(300, 150, 300, 150)
kd.curve(40, -210)
kd.settings(800, 250, 800, 250)
kd.straight(700)

kd.straight(660)
kd.turn(150)
kd.straight(185)
kd.straight(280)
kd.straight(-300)
kd.turn(-59)
kd.straight(275)
kd.turn(48)
kd.straight(765)
