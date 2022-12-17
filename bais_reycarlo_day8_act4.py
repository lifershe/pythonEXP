class House:
    def __init__(self, flrSize, noOfFlr, noOfDoors):
        self.mFlrSize = flrSize
        self.mNoOfFlr = noOfFlr
        self.mNoOfDoors = noOfDoors
    def print_details(self):
        print(f"""The details are:
    Floor Size: {self.mFlrSize} sqm
    No. of Floors: {self.mNoOfFlr}
    No. of Doors: {self.mNoOfDoors}""")
    def switchOn(self):
        print(self.ovenOpen())
        print(self.ligthOpen())

    def ligthOpen(self):
        return "Lights is ON"

    def ovenOpen(self):
        return "Oven is ON"

class TownHouse(House):
    def __init__(self, flrSize, noOfFlr, noOfDoors):
        super().__init__(flrSize, noOfFlr, noOfDoors)

h1 = TownHouse(100, 2, 8)
h1.print_details()
h1.switchOn()