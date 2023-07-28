
"""OOPs object oriented programing says that consider everything as real world object in software development."""

class Computer:

    def __init__(self,price,company):
        print("hello from init")
        self.price = price
        self.company = company

    def myInfo(self):
        print("This is ",self.company," laptop of ",self.price)

    def playMusic(self):
        print("Music is getting played...")


computer1 = Computer(50000,"DELL")
computer1.myInfo()
computer1.playMusic()

computer2 = Computer(350000,"HP")
computer2.myInfo()
computer2.playMusic()
