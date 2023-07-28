
"""OOPs object oriented programing says that consider everything as real world object in software development."""

class Computer:

    price = 50000
    company = "HP"

    def myInfo(self):
        print("This is ",self.company," laptop of ",self.price)


computer  = Computer()
computer.myInfo()
