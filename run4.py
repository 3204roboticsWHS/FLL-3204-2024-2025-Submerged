from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub()

kd = DriveBase(Motor(Port.E, Direction.COUNTERCLOCKWISE), Motor(Port.B), 56, 84)
kd.settings(900, 800, 900, 800)

kd.straight(200)
left_turn()
kd.straight(200)
kd.turn(42.5)
kd.straight(300)
kd.straight(-200)
