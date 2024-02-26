from Brikker import Bonde, Tårn, Springer, Løber, Dronning, Konge

class Skakbræt:
    def __init__(self):
        self.bræt = self.opret_tomt_bræt()
        self.start_position()

    def opret_tomt_bræt(self):
        return [[None for _ in range(8)] for _ in range(8)]

    def start_position(self):
        # Placer sortes brikker
        for i in range(8):
            self.bræt[1][i] = Bonde('Sort')
        self.bræt[0][0] = Tårn('Sort')
        self.bræt[0][7] = Tårn('Sort')
        self.bræt[0][1] = Springer('Sort')
        self.bræt[0][6] = Springer('Sort')
        self.bræt[0][2] = Løber('Sort')
        self.bræt[0][5] = Løber('Sort')
        self.bræt[0][3] = Dronning('Sort')
        self.bræt[0][4] = Konge('Sort')

        # Placer hvides brikker
        for i in range(8):
            self.bræt[6][i] = Bonde('Hvid')
        self.bræt[7][0] = Tårn('Hvid')
        self.bræt[7][7] = Tårn('Hvid')
        self.bræt[7][1] = Springer('Hvid')
        self.bræt[7][6] = Springer('Hvid')
        self.bræt[7][2] = Løber('Hvid')
        self.bræt[7][5] = Løber('Hvid')
        self.bræt[7][3] = Dronning('Hvid')
        self.bræt[7][4] = Konge('Hvid')
