
"""OOPs object oriented programing says that consider everything as real world object in software development."""

class Computer:

    price = 50000
    company = "HP"

    def myInfo(self):
        print("This is ",self.company," laptop of ",self.price)

    def playMusic(self):
        print("Music is getting played...")


computer1 = Computer()
computer1.price = 45000
computer1.company = "DELL"
computer1.myInfo()
computer1.playMusic()

computer2 = Computer()
computer2.myInfo()
computer2.playMusic()
