from classes.delivery_robot import DeliveryRobot
from classes.guard_robot import GuardRobot



if __name__ == "__main__":

    dora = DeliveryRobot("dora")
    gideon = GuardRobot("gideon")

    while True:
        print("""
    -------------------------
        1. say something
        2.move
        3.where
        4.exit
    -------------------------""")
        try:
            cli = input("choose some num of command: ")
            match cli:
                     case "1":
                         stri = input("please enter some str")
                         dora.say(stri)
                         gideon.say(stri)

                     case "2":
                         location1 = int(input("enter your x point: "))
                         location2 = int(input("enter your y point: "))
                         locatins = (location1,location2)
                         dora.move(location1,location2)
                         gideon.move(location1,location2)


                     case "3":
                         dora.location()
                         gideon.location()



                     case "4":
                        exit()

        except ValueError:
            print("illegal input")