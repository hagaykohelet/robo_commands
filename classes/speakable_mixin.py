from classes.robot import Robot

class SpeakAble(Robot):

    def __init__(self,name):
        super().__init__(name)

    def speak(self,s):
        print(f"{self.name} say {s}")