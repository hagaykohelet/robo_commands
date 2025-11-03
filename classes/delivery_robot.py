from classes.robot import Robot
from classes.speakable_mixin import SpeakAble
from classes.moveable_mixin import MoveAbility
class DeliveryRobot(SpeakAble,MoveAbility):
    def __init__(self, name):
        super().__init__(name)

    def say(self,s):
        super().speak(s)


    def move(self,x,y):
        super().move(x,y)

    def location(self):
        super().location()