from classes.robot import Robot
class MoveAbility(Robot):
    def __init__(self,name):
        super().__init__(name)
        self.place = (0,0)


    def move(self,x,y):
        self.place = (x,y)

    def location(self):
        print(f"{self.name} move to {self.place}")

