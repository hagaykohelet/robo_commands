from classes.speakable_mixin import SpeakAble

class GuardRobot(SpeakAble):

    def __init__(self, name):
        super().__init__(name)

    def say(self,s):
        super().speak(s)

    def location(self):
        print(f"this robot in 0,0")
    def move(self,x,y):
        print(f"{self.name} robot cannot move")











